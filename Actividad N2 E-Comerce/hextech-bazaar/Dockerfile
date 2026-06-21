# Hextech Bazaar — imagen de la app (Next.js 14 + SQLite/better-sqlite3).
# Imagen única y robusta: incluye el código, los seeds SQL y las imágenes.
# La base de datos SQLite se crea dentro del contenedor en el build/arranque.
FROM node:20-bookworm-slim
WORKDIR /app

# Herramientas para compilar el módulo nativo better-sqlite3 (si no hay prebuilt).
RUN apt-get update && apt-get install -y --no-install-recommends python3 make g++ ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ENV NEXT_TELEMETRY_DISABLED=1

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

ENV NODE_ENV=production
ENV PORT=3000
ENV HOSTNAME=0.0.0.0
EXPOSE 3000
CMD ["npm", "run", "start"]
