import { ExecArgs } from "@medusajs/framework/types"
import { 
  TransactionBaseService,
  EntityManager
} from "@medusajs/medusa"

export default async function verifySetup({ container }: ExecArgs) {
  const logger = container.resolve("logger")
  const manager = container.resolve<TransactionBaseService>("manager")

  await manager.withTransaction(async (transactionManager: EntityManager) => {
    try {
      // 1. Verify and create FCFA region
      const regionRepository = transactionManager.getRepository("region")
      let fcfaRegion = await regionRepository.findOne({
        where: { currency_code: "xof" }
      })

      if (!fcfaRegion) {
        fcfaRegion = await regionRepository.save({
          name: "Afrique de l'Ouest",
          currency_code: "xof",
          tax_rate: 18,
          automatic_taxes: true
        })
        logger.info("✅ FCFA Region created:", fcfaRegion.id)
      }

      // 2. Update store settings
      const storeRepository = transactionManager.getRepository("store")
      const store = await storeRepository.findOne({})
      if (store) {
        await storeRepository.update(store.id, {
          default_currency_code: "xof",
          currencies: ["xof"]
        })
        logger.info("✅ Store settings updated")
      }

      // 3. Add or update countries
      const countryRepository = transactionManager.getRepository("country")
      const countries = [
        { iso_2: "bj", display_name: "Bénin" },
        { iso_2: "bf", display_name: "Burkina Faso" },
        { iso_2: "ci", display_name: "Côte d'Ivoire" },
        { iso_2: "gw", display_name: "Guinée-Bissau" },
        { iso_2: "ml", display_name: "Mali" },
        { iso_2: "ne", display_name: "Niger" },
        { iso_2: "sn", display_name: "Sénégal" },
        { iso_2: "tg", display_name: "Togo" }
      ]

      for (const country of countries) {
        const existingCountry = await countryRepository.findOne({
          where: { iso_2: country.iso_2 }
        })
        
        if (!existingCountry) {
          await countryRepository.save({
            ...country,
            region_id: fcfaRegion.id
          })
        } else if (existingCountry.region_id !== fcfaRegion.id) {
          await countryRepository.update(existingCountry.id, {
            region_id: fcfaRegion.id
          })
        }
      }

      // 4. Configure payment providers
      const paymentProviderRepository = transactionManager.getRepository("payment_provider")
      const providers = ["manual", "cash-on-delivery"]
      
      for (const provider of providers) {
        const existingProvider = await paymentProviderRepository.findOne({
          where: { id: provider }
        })
        
        if (!existingProvider) {
          await paymentProviderRepository.save({
            id: provider,
            is_installed: true
          })
        }
      }

      logger.info("✅ Base configuration completed successfully")

    } catch (error) {
      logger.error("Error during verification:", error)
      throw error
    }
  })
}
