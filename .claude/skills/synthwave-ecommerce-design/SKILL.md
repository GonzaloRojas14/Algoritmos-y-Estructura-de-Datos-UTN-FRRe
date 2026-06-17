---
name: synthwave-ecommerce-design
description: Sistema de diseño front-end con estética Synthwave / Y2K neón para e-commerce (RetroVerse y similares). Usar cuando se construyan vistas, componentes, paletas, tipografía o layouts de una tienda online retro-futurista, o cuando se pida "diseño front", "estética neón", "synthwave" o "look retro tech".
---

# Synthwave / Y2K E-commerce Design System

Estética retro-futurista 80s/90s: neón, gradientes, grids en perspectiva, glow. Pensado para tiendas de objetos vintage / tecnología retro (RetroVerse).

## Principios
1. **Fondo oscuro siempre** (#0a0a1f → #1a0b2e). El neón solo brilla sobre oscuro.
2. **Dos acentos neón** dominantes: magenta/rosa (#ff2e97) y cyan (#05d9e8). Un tercero opcional: violeta (#b537f2) o amarillo (#ffe600).
3. **Glow, no sombra dura**: usar `box-shadow`/`text-shadow` con color del acento y blur alto, baja opacidad.
4. **Grid en perspectiva** (synthwave horizon) como recurso de fondo/hero, no en todas las vistas.
5. **Contraste alto y legibilidad**: el texto de cuerpo va en blanco/gris claro (#e7e7f0), nunca neón puro en párrafos largos.
6. **Menos es más con el glow**: 2-3 elementos con glow por viewport, el resto sobrio.

## Tokens (CSS variables)
```css
:root {
  --bg-900:#0a0a1f; --bg-800:#12082b; --bg-700:#1a0b2e; --surface:#1e1140;
  --neon-pink:#ff2e97; --neon-cyan:#05d9e8; --neon-violet:#b537f2; --neon-yellow:#ffe600;
  --text:#e7e7f0; --text-dim:#9a96c4; --border:#3a2a6e;
  --grad-main:linear-gradient(135deg,#ff2e97 0%,#b537f2 50%,#05d9e8 100%);
  --glow-pink:0 0 12px rgba(255,46,151,.6), 0 0 32px rgba(255,46,151,.3);
  --glow-cyan:0 0 12px rgba(5,217,232,.6), 0 0 32px rgba(5,217,232,.3);
  --radius:14px; --radius-sm:8px;
}
```

## Tipografía
- **Display/títulos**: fuente geométrica retro — `"Orbitron"`, `"Audiowave"` o `"Press Start 2P"` (esta última solo para acentos cortos, no títulos largos). Mayúsculas, `letter-spacing` amplio.
- **Cuerpo/UI**: sans legible — `"Inter"`, `"Rajdhani"` o `system-ui`.
- Cargar por `next/font/google` (Orbitron + Inter) para evitar FOUT.

## Componentes clave
- **Navbar**: sticky, fondo translúcido con `backdrop-filter: blur`, logo con `--grad-main` en `background-clip:text`, links con underline neón en hover.
- **Card de producto**: surface oscura, borde 1px `--border`, en hover sube borde a `--neon-cyan` + `--glow-cyan` y `transform: translateY(-4px)`. Imagen con leve saturación/contraste. Badge de "estado/condición" (Nuevo, Restaurado, Vintage) con chip neón.
- **Botón primario**: fondo `--grad-main`, texto oscuro/blanco, glow en hover. Botón secundario: outline neón.
- **Precio**: tipografía display, color `--neon-yellow` o cyan.
- **Hero**: grid en perspectiva (CSS `linear-gradient` repetido + `transform: perspective` o SVG), sol/gradiente, título grande con glow.
- **Footer**: oscuro, líneas neón finas como separadores.

## Layout
- Grid de catálogo responsive: `repeat(auto-fill, minmax(260px,1fr))`, gap 24px.
- Container máx 1200px, padding lateral 24px.
- Mobile-first; el glow se reduce en mobile por performance.

## Recursos sin assets externos (todo CSS/SVG)
- Grid synthwave: gradientes lineales repetidos con `mask` de perspectiva.
- Scanlines sutiles: `repeating-linear-gradient` con opacidad muy baja, opcional.
- Evitar imágenes pesadas; usar placeholders con gradiente si falta foto de producto.

## Anti-patrones (NO hacer)
- Fondo claro/blanco.
- Neón en párrafos largos o en muchos elementos a la vez (cansa la vista).
- Sombras grises tradicionales (rompen la estética).
- Más de 3 colores neón compitiendo en una misma vista.

## Aplicación en Next.js
- `globals.css` con los tokens en `:root`.
- Componentes en `app/` (App Router), Server Components por defecto; client solo donde haya interacción (hover ya es CSS, carrito visual sí es client).
- Reutilizar clases utilitarias o CSS Modules; mantener consistencia con los tokens.
