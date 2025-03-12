import { Medusa } from "@medusajs/medusa"
import express from "express"

async function start() {
  const app = express()

  try {
    const medusaInstance = new Medusa({
      directories: {
        rootDir: process.cwd(),
      },
      expressApp: app,
      database: {
        type: "postgres",
        url: process.env.DATABASE_URL
      }
    })

    await medusaInstance.load()
    await medusaInstance.start()

    const PORT = process.env.PORT || 9000
    app.listen(PORT, () => {
      console.log(`Server is ready at http://localhost:${PORT}`)
      console.log(`Admin dashboard available at http://localhost:${PORT}/app`)
    })
  } catch (error) {
    console.error("Server initialization error:", error)
    if (error instanceof Error) {
      console.error("Error details:", error.message)
      console.error("Stack trace:", error.stack)
    }
    process.exit(1)
  }
}

start().catch((err) => {
  console.error("Fatal error:", err)
  process.exit(1)
})
