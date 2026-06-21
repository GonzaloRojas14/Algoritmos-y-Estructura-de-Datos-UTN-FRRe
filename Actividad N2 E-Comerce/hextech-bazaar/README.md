# Hextech Bazaar ⚔️✨

**Fantasy Shop** (Opción 5) temático de **League of Legends** — mercado del universo de Runeterra.
**Demo académica** — Actividad Formativa N.º 2, Algoritmos y Estructuras de Datos (UTN-FRRe, ISI 2026).

> Página funcional a nivel de navegación entre vistas, productos y carrito.
> **No procesa pagos reales.** Es un modelo para demostrar los conceptos de **registro** y **clave**
> (Unidad 2).

## 🌐 Demo en vivo
URL pública (túnel Cloudflare, temporal): se imprime al iniciar `cloudflared` (formato
`https://<aleatorio>.trycloudflare.com`).

## 🧱 Stack
- **Next.js 14** (App Router, TypeScript) — Server Components que consultan la BD en vivo.
- **SQLite** vía `better-sqlite3` — esquema en modelo **snowflake**; el SQL es el artefacto académico.
- **Riot Data Dragon** (v16.12.1) — datos e imágenes oficiales de campeones, aspectos e ítems.
- **cloudflared** — túnel para publicar una URL gratuita.
- Estética **Hextech / Piltóver** (oro + cian sobre azul-noche).

## 🗂️ Estructura
```
hextech-bazaar/
├── app/                  # Next.js App Router (vistas y componentes)
│   ├── page.tsx          # Portada (hero + familias + destacados)
│   ├── catalogo/         # Catálogo con filtros (familia, categoría, rareza, región) y búsqueda
│   ├── producto/[id]/    # Detalle de producto
│   ├── carrito/          # Carrito (client, sin pago real)
│   ├── modelo/           # Modelo de datos en vivo (registro, claves, corte de control)
│   └── components/       # Navbar, Footer, ProductCard, carrito, UI
├── lib/                  # Conexión SQLite (db.ts) y queries (queries.ts)
├── db/
│   ├── schema.sql            # DDL snowflake (comentado por tipo de clave)
│   ├── seed-dimensiones.sql  # Dimensiones estáticas + registro maestro (compradores)
│   └── seed-productos.sql    # Productos (autogenerado desde Data Dragon)
├── scripts/fetch-ddragon.mjs # Descarga datos+imágenes y genera el seed de productos
├── docs/
│   ├── modelo-datos.md   # Registro maestro + claves + diagrama ER
│   ├── prompts.md        # Registro cronológico de prompts con la IA
│   └── gen_pdf.py        # Generador del PDF de entrega
└── public/img/           # Imágenes descargadas (loading/splash/item)
```

## 🔑 Registro maestro y claves
- **Registro maestro:** `dim_comprador` (cliente-comprador, el *Invocador*).
- **Cardinalidad N:1:** muchos compradores → un servidor (`dim_comprador.id_servidor`).
- **Clave primaria:** `id_comprador` (surrogate simple); email y Riot ID (`nick_invocador`+`riot_tag`)
  como candidatas `UNIQUE`.
- Ver detalle completo en [`docs/modelo-datos.md`](docs/modelo-datos.md).

## ▶️ Cómo correrlo localmente
```bash
npm install
npm run fetch:data   # descarga imágenes y genera db/seed-productos.sql (ya incluido)
npm run build && npm run start   # http://localhost:3000
# La BD SQLite (db/hextech.sqlite) se crea y siembra sola en el primer arranque.
```

## 🌩️ Publicar con túnel
```bash
cloudflared tunnel --url http://localhost:3000
# Copiá la URL https://<aleatorio>.trycloudflare.com que imprime.
```

## 📄 Generar el PDF de entrega
```bash
python3 docs/gen_pdf.py   # requiere reportlab
```
