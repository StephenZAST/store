import {
  createRegionsWorkflow,
  createTaxRegionsWorkflow,
} from "@medusajs/medusa/core-flows"
import { ExecArgs } from "@medusajs/framework/types"

export default async function seedFCFAData({ container }: ExecArgs) {
  const logger = container.resolve("logger")

  logger.info("Seeding FCFA region data...")
  
  try {
    const { result: regionResult } = await createRegionsWorkflow(container).run({
      input: {
        regions: [
          {
            name: "Afrique de l'Ouest",
            currency_code: "xof",
            countries: ["bj", "bf", "ci", "gw", "ml", "ne", "sn", "tg"],
            payment_providers: ["manual"],
            tax_rate: 18,
            includes_tax: true
          },
        ],
      },
    })

    // Add tax rates
    await createTaxRegionsWorkflow(container).run({
      input: ["bj", "bf", "ci", "gw", "ml", "ne", "sn", "tg"].map((country_code) => ({
        country_code,
        rate: 18,
      })),
    })

    logger.info("Successfully seeded FCFA regions.")
  } catch (error) {
    logger.error("Error seeding FCFA data:", error)
    throw error
  }
}
