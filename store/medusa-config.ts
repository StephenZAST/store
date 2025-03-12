import { ConfigModule } from '@medusajs/medusa'
import { DataSource } from 'typeorm'

const config: ConfigModule = {
  projectConfig: {
    database_type: "postgres",
    database_url: process.env.DATABASE_URL,
    store_cors: process.env.STORE_CORS,
    admin_cors: process.env.ADMIN_CORS,
    redis_url: process.env.REDIS_URL,
    database_logging: false,
    jwt_secret: process.env.JWT_SECRET,
    cookie_secret: process.env.COOKIE_SECRET
  },
  featureFlags: {},
  modules: {
    eventBus: {
      resolve: "@medusajs/event-bus-local"
    },
    cacheService: {
      resolve: "@medusajs/cache-inmemory"
    }
  },
  plugins: [
    {
      resolve: "@medusajs/admin",
      options: {
        autoRebuild: true
      }
    }
  ]
}

export default config
