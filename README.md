# E-Shop - Modern E-commerce Platform

## Overview
E-Shop is a modern and performant e-commerce platform built with Medusa and Next.js 15. This project leverages Next.js App Router architecture and provides a seamless shopping experience with multi-region support.

## 🚀 Features

- **Modern Stack**: Built with Next.js 15 and Medusa.js
- **Performance Optimized**: Server-side rendering and static generation
- **Multi-Region Support**: Automatic region detection and currency switching
- **Responsive Design**: Mobile-first approach using TailwindCSS
- **Shopping Cart**: Real-time cart management
- **Product Management**: Dynamic product catalog
- **Secure Checkout**: Integrated with Stripe
- **SEO Optimized**: Built-in SEO best practices

## 🛠 Tech Stack

- Next.js 15
- Medusa.js
- TypeScript
- TailwindCSS
- Headless UI
- React 19
- Node.js

## 📦 Installation

```bash
# Clone the repository
git clone <repository-url>

# Navigate to project directory
cd store-storefront

# Install dependencies
yarn install

# Set up environment variables
cp .env.template .env.local
```

## ⚙️ Environment Variables

```env
MEDUSA_BACKEND_URL=http://localhost:9000
NEXT_PUBLIC_MEDUSA_PUBLISHABLE_KEY=your_publishable_key
NEXT_PUBLIC_DEFAULT_REGION=fr
```

## 🚀 Development

```bash
# Start development server
yarn dev

# Build for production
yarn build

# Start production server
yarn start
```

## 📁 Project Structure

```
store-storefront/
├── src/
│   ├── app/                   # Next.js App Router pages
│   ├── modules/              # Feature modules
│   │   ├── layout/          # Layout components
│   │   ├── common/          # Shared components
│   │   └── products/        # Product related components
│   ├── lib/                 # Utilities and helpers
│   └── types/              # TypeScript type definitions
├── public/                  # Static assets
└── package.json
```

## 🌐 Multi-Region Support

The store supports multiple regions with:
- Automatic region detection
- Currency conversion
- Region-specific pricing
- Shipping rules by region

## 🔒 Security

- Secure payment processing
- HTTPS enforcement
- Data encryption
- Input validation

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Credits

- Built with [Medusa](https://www.medusajs.com/)
- Powered by [Next.js](https://nextjs.org/)
- UI Components from [Headless UI](https://headlessui.dev/)

## 📝 Notes

- This project is actively maintained
- Requires Node.js 16 or higher
- Backend Medusa server must be running
- Testing implementation in progress

---

⭐ If you found this project helpful, please consider giving it a star!
