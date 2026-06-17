# Registro cronológico de prompts (interacción con la IA)

> Requisito de la Actividad N.º 2: documentar **todos** los prompts usados con la IA,
> incluyendo explícitamente el pedido del **diseño del registro** y la **definición de la
> clave**. IA utilizada: **Claude (Claude Code / Opus 4.8)**.

---

## Prompt 0 — Contexto teórico (registro y clave)
**Fecha:** 2026-06-17
El estudiante aportó a la IA la teoría de la Unidad 2 sobre la anatomía de los registros
(campos contenidos/continentes, selector de campo) y el poder de las claves (simple,
compleja, primaria, secundaria, foránea), y su aplicación en corte de control y archivos
indexados. Objetivo: que la IA modele en base a esos conceptos.

## Prompt 1 — Encargo general del e-commerce
**Fecha:** 2026-06-17
> "En este workspace hay una carpeta 'actividad dos' con un PDF de requerimientos para
> crear una página e-commerce con IA. Gestioná las skills necesarias (diseño front y
> modelaje), generalas e instalalas tras un research si hace falta. El e-commerce elegido
> es **RetroVerse**. Vamos a armar un **modelo de datos relacional en esquema snowflake**
> para usar diferentes claves. En el server hay un Docker corriendo: armá un **container
> distinto** para alojar esto y, mientras tanto, usá un **túnel Cloudflare** para tener una
> URL random gratis. El **registro maestro será orientado a cliente-comprador** con
> cardinalidad **N:1** (muchos compradores compran a un vendedor). La página debe ser
> **funcional visualmente** entre ventanas e ítems, pero **sin pago real** (es un modelo,
> no producción). Andá documentando en un PDF y guardando los prompts cronológicamente."

## Prompt 2 — Definiciones de arquitectura (respuestas a la IA)
**Fecha:** 2026-06-17
La IA repreguntó dos puntos y el estudiante eligió:
- **Stack/datos:** Next.js + **PostgreSQL real** (esquema snowflake en BD real, app que lee
  de la BD; containers app + db).
- **Estética:** **Synthwave / Y2K neón**.

---

### Diseño del registro y definición de la clave (entregado a la IA en el modelado)
El pedido explícito a la IA fue: *"Diseñá el registro principal de RetroVerse orientado al
cliente-comprador, indicando nombre de cada campo, su tipo de dato y tamaño, e identificá
la clave del registro justificando su elección; integralo a un esquema snowflake con
dimensiones normalizadas que muestre claves primaria, foránea, secundaria, simple y
compleja."*

Resultado producido por la IA → ver [`modelo-datos.md`](modelo-datos.md) y
[`db/schema.sql`](../db/schema.sql).

## Prompt 4 — Construcción y despliegue (ejecución autónoma de la IA)
**Fecha:** 2026-06-17
A partir de los lineamientos, la IA ejecutó de forma autónoma: generó las skills de diseño
y modelaje, el esquema snowflake (DDL + seed), la app Next.js + PostgreSQL con estética
synthwave, la containerización (docker-compose: app + db + cloudflared) y el despliegue en
el servidor sin tocar los contenedores existentes.

**Resultado del despliegue:**
- 3 contenedores arriba: `retroverse-db` (healthy), `retroverse-app`, `retroverse-tunnel`.
- Base poblada: 14 productos, 6 compradores, 3 vendedores, 6 ventas.
- URL pública (Cloudflare Quick Tunnel): **https://seeks-gif-log-ringtones.trycloudflare.com**
  *(URL efímera; cambia si el contenedor del túnel se reinicia).*

## Prompt 5 — Cambio de túnel (problema de DNS) y carga de imágenes reales
**Fecha:** 2026-06-17

**5.a — El Quick Tunnel de Cloudflare no abría para el alumno.** Daba `ERR_NAME_NOT_RESOLVED`
en wifi y en datos móviles, aunque funcionaba para terceros y desde el servidor. Diagnóstico:
el dominio `trycloudflare.com` está marcado como abusado y lo filtran a nivel DNS los clientes
de Cloudflare del lado del usuario (app **1.1.1.1/WARP**, DNS privado, **1.1.1.1 for Families**,
Zero Trust/Gateway). Al ser config del dispositivo, falla en cualquier red. **Solución:** se
reemplazó `cloudflared` por **`bore`** (relay HTTP comunitario en `bore.pub`, otro dominio no
filtrado), integrado al `docker-compose` con puerto remoto fijo. **URL pública estable:**
**http://bore.pub:63304**. No se abrieron puertos entrantes (el túnel es saliente).

**5.b — Imágenes reales en las publicaciones.** Pedido: *"ponele imágenes a las publicaciones,
buscá los objetos en internet y usalos para los items"*. La IA descargó una foto representativa
de cada uno de los 14 productos desde **Wikipedia / Wikimedia Commons** (uso educativo) mediante
el endpoint soportado `Special:FilePath?width=800` —ver [`scripts/fetch_images.py`](../scripts/fetch_images.py)—,
las guardó en `public/img/<sku>.<ext>` y pobló `dim_producto.imagen_url` en el seed. El front
(`ProductCard` y detalle de producto) ahora muestra la foto con el gradiente neón como *fallback*.

**Resultado:** 14/14 productos con imagen; la app sirve los archivos (`image/jpeg` / `image/png`);
catálogo y detalle renderizan las fotos. Stack final: `retroverse-db` (healthy), `retroverse-app`,
`retroverse-bore`.

---
*(Este archivo se actualiza cronológicamente a medida que avanza el desarrollo.)*
