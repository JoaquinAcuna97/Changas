# React + FastAPI

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

## FastAPI Commands

- cd fastapi-backend
- docker-compose up --build
- docker-compose run --rm backend_test

## React Commands

- cd fastapi-frontend
- npm run dev

## Docker Commands

- docker-compose down -v --remove-orphans
- docker system prune -af

- docker-compose build --no-cache
- docker-compose up

# ✅ Tecnologías recomendadas para una PWA mantenible y escalable
## 🧠 Frontend: React + TypeScript
React es ampliamente adoptado, bien documentado y soporta el desarrollo de componentes reutilizables.

TypeScript mejora la mantenibilidad y escalabilidad al evitar errores comunes en JS puro.

Librerías recomendadas:

Vite (alternativa a Next.js si quieres algo más liviano y rápido en dev)

## 🧱 Backend: FastAPI
Si ya tienes experiencia con Django, es excelente para una app robusta y segura.

Si buscas performance + flexibilidad en microservicios → FastAPI

Ambos ofrecen APIs fácilmente consumibles por el frontend React.

## 📦 PWA Capabilities:
Next.js PWA plugin: next-pwa

Maneja service workers, caching, offline-first.

O puedes usar Workbox directamente si tienes un setup personalizado con Vite o Webpack.

## 🐳 Infraestructura y DevOps:
### Docker: contenerizar todo el proyecto (frontend + backend + DB)

Docker Compose: entorno local consistente

###  CI/CD: GitHub Actions para pruebas y despliegues automáticos

###  Infra recomendada:

- Antel para hosting

- PostgreSQL como base de datos

##  📱 Extras para calidad y escalabilidad:
- Jest + React Testing Library para testeo de frontend

- Pytest para backend en Django/FastAPI

- Prettier + ESLint + Husky para mantener el código limpio

- i18n si planeas escalar a múltiples idiomas