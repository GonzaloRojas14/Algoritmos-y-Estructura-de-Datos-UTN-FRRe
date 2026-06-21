# Registro cronológico de prompts (interacción con la IA)

> Requisito de la Actividad N.º 2: documentar **todos** los prompts usados con la IA,
> incluyendo explícitamente el pedido del **diseño del registro** y la **definición de la
> clave**. IA utilizada: **Claude**.

---

## Prompt 0 — Contexto teórico (registro y clave)
**Fecha:** 2026-06-17
El estudiante aportó a la IA la teoría de la Unidad 2 sobre la anatomía de los registros
(campos contenidos/continentes, selector de campo) y los tipos de clave (simple, compleja,
primaria, secundaria, foránea), con su aplicación en corte de control y archivos indexados.
Objetivo: que la IA modele en base a esos conceptos.

## Prompt 1 — Encargo general del e-commerce
**Fecha:** 2026-06-17
> "El e-commerce elegido es **RetroVerse**. Armá un **modelo de datos relacional en esquema
> snowflake** para usar diferentes tipos de clave. El **registro maestro será orientado a
> cliente-comprador** con cardinalidad **N:1** (muchos compradores compran a un vendedor). La
> página debe ser **funcional visualmente** entre vistas e ítems, pero **sin pago real** (es un
> modelo académico, no producción). Andá documentando el proceso y guardando los prompts
> cronológicamente."

## Prompt 2 — Definiciones de diseño (respuestas a la IA)
**Fecha:** 2026-06-17
La IA repreguntó y el estudiante eligió:
- **Datos:** implementar el modelo (esquema snowflake) en una **base de datos relacional real**,
  con una aplicación que la consume.
- **Estética:** **Synthwave / Y2K neón**, coherente con la temática retro.

## Prompt 3 — Diseño del registro y la clave (pedido explícito a la IA)
**Fecha:** 2026-06-17
> *"Diseñá el registro principal de RetroVerse orientado al cliente-comprador, indicando nombre
> de cada campo, su tipo de dato y tamaño, e identificá la clave del registro justificando su
> elección; integralo a un esquema snowflake con dimensiones normalizadas que muestre claves
> primaria, foránea, secundaria, simple y compleja."*

Resultado producido por la IA → ver [`modelo-datos.md`](modelo-datos.md).

## Prompt 4 — Imágenes reales en las publicaciones
**Fecha:** 2026-06-17
> *"Ponele imágenes a las publicaciones; buscá los objetos en internet y usalos para los ítems."*

La IA obtuvo una foto representativa de cada uno de los 14 productos desde repositorios de
imágenes de **uso educativo** (Wikipedia / Wikimedia Commons) y las integró al catálogo. Cada
publicación muestra ahora la foto del objeto, con el gradiente neón como *fallback* si faltara
la imagen.

---
*(Este archivo se actualiza cronológicamente a medida que avanza el desarrollo.)*
