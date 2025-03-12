import { ExecArgs } from "@medusajs/framework/types"

export default async function setupFCFA({ container }: ExecArgs) {
  const logger = container.resolve("logger")
  const manager = container.resolve("manager")

  try {
    await manager.query(`
      WITH new_region AS (
        INSERT INTO "region" (
          name, 
          currency_code,
          tax_rate,
          created_at,
          updated_at
        ) 
        VALUES (
          'Afrique de l''Ouest',
          'xof',
          18,
          NOW(),
          NOW()
        )
        RETURNING id
      ),
      store_update AS (
        UPDATE store 
        SET 
          default_currency_code = 'xof',
          updated_at = NOW()
        WHERE id IN (SELECT id FROM store LIMIT 1)
      )
      INSERT INTO store_currencies (store_id, currency_code)
      SELECT id, 'xof'
      FROM store
      WHERE NOT EXISTS (
        SELECT 1 FROM store_currencies 
        WHERE currency_code = 'xof' 
        AND store_id = store.id
      );
    `)

    logger.info("✅ Configuration FCFA de base terminée")

  } catch (error) {
    logger.error("Erreur lors de la configuration:", error)
    throw error
  }
}
