const dotenv = require('dotenv')

let ENV_FILE_NAME = '';
switch (process.env.NODE_ENV) {
  case 'production':
    ENV_FILE_NAME = '.env.production';
    break;
  case 'staging':
    ENV_FILE_NAME = '.env.staging';
    break;
  case 'test':
    ENV_FILE_NAME = '.env.test';
    break;
  case 'development':
  default:
    ENV_FILE_NAME = '.env';
    break;
}

dotenv.config({ path: process.cwd() + '/' + ENV_FILE_NAME });

const config = {
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

module.exports = config
