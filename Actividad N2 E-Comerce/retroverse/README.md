# RetroVerse 🕹️

Tienda digital de objetos vintage, coleccionables y tecnología retro.
**Demo académica** — Actividad Formativa N.º 2, Algoritmos y Estructuras de Datos (UTN-FRRe, ISI 2026).

> Página funcional a nivel de navegación entre vistas, ítems y carrito.
> **No procesa pagos reales.** Es un modelo para demostrar los conceptos de
> **registro** y **clave** (Unidad 2).

## 🌐 Demo en vivo
URL pública (Cloudflare Quick Tunnel — efímera):
**https://seeks-gif-log-ringtones.trycloudflare.com**

## 🧱 Stack
- **Next.js 14** (App Router, TypeScript) — Server Components que consultan la BD en vivo.
- **PostgreSQL 16** — esquema `retroverse` en modelo **snowflake**.
- **Cliente `pg`** — sin ORM; el SQL es el artefacto académico.
- **Docker Compose** — `app` + `db` + `cloudflared`.
- Estética **Synthwave / Y2K neón**.

## 🗂️ Estructura
```
retroverse/
├── app/                  # Next.js App Router (vistas y componentes)
│   ├── page.tsx          # Catálogo + filtros (familia, década, búsqueda)
│   ├── producto/[id]/    # Detalle de producto
│   ├── tienda/[id]/      # Vendedor (muestra la relación N:1)
│   ├── carrito/          # Carrito (client, sin pago real)
│   └── modelo/           # Explicación del modelo de datos (en vivo)
├── lib/                  # Pool de Postgres y queries
├── db/
│   ├── schema.sql        # DDL del esquema snowflake (todos los tipos de clave)
│   └── seed.sql          # Datos de ejemplo
├── docs/
│   ├── modelo-datos.md   # Diseño del registro maestro + claves + diagrama ER
│   ├── prompts.md        # Registro cronológico de prompts con la IA
│   └── gen_pdf.py        # Generador del PDF de entrega
├── Dockerfile
└── docker-compose.yml
```

## 🔑 Registro maestro y claves
- **Registro maestro:** `dim_comprador` (cliente-comprador).
- **Cardinalidad N:1:** muchos compradores → un vendedor (`dim_comprador.id_vendedor`).
- **Clave primaria:** `id_comprador` (surrogate simple); DNI y email como candidatas `UNIQUE`.
- Ver detalle completo en [`docs/modelo-datos.md`](docs/modelo-datos.md).

## ▶️ Cómo correrlo (en el servidor)
```bash
# 1) Construir la imagen de la app (buildx < 0.17 -> build directo)
sudo docker build -t retroverse-app:latest .

# 2) Levantar el stack (carga schema.sql + seed.sql automáticamente)
sudo docker compose up -d --no-build

# 3) Obtener la URL del túnel
sudo docker logs retroverse-tunnel | grep trycloudflare.com
```
El stack no publica puertos en el host (no colisiona con otros servicios del server);
`cloudflared` expone la app vía un Quick Tunnel.

## 💻 Desarrollo local
```bash
npm install
# Requiere un PostgreSQL con el esquema cargado y DATABASE_URL apuntando a él
DATABASE_URL=postgresql://retroverse:retroverse@localhost:5432/retroverse npm run dev
```
