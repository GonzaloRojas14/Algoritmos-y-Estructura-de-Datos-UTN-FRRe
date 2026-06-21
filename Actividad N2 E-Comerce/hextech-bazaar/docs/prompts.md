# Registro cronológico de prompts (interacción con la IA)

> Requisito de la Actividad N.º 2: documentar **todos** los prompts usados con la IA, incluyendo
> explícitamente el pedido del **diseño del registro** y la **definición de la clave**.
> **IA utilizada:** Claude (Claude Code, modelo Opus).

---

## Prompt 0 — Contexto teórico (registro y clave) · *Unidad 2*

El estudiante aportó a la IA la teoría de la Unidad 2: anatomía de los **registros** (campos
*contenidos* y *continentes*, selector de campo `Registro.Campo`) y los **tipos de clave**
(simple, compleja/compuesta, primaria, secundaria, foránea), con su aplicación en **corte de
control** y archivos indexados. Objetivo: que la IA modele en base a esos conceptos.

## Prompt 1 — Encargo general del e-commerce (prompt principal)

> *"Necesito que leas el PDF de la Actividad 2, que tiene los requerimientos para crear una página
> e-commerce, y que gestiones las skills necesarias. El e-commerce va a ser el de la **Opción 5 –
> Fantasy Shop**. Siguiendo las consignas del PDF y los conceptos de la Unidad 2, **diseñá el modelo
> de datos en un esquema snowflake; el registro maestro tiene que estar orientado a
> cliente-comprador. Generá la estructura del registro detallando: nombre del campo, tipo de dato, y
> justificá teóricamente la elección de claves.** Después, en lo visual, que sea sobre el juego
> **League of Legends**: descargá ítems o 'productos' del juego y agregalos a la página. Tiene que
> ser un prototipo funcional visualmente (navegación entre ventanas, catálogo, vista de un
> producto); vas a necesitar skills de diseño front y de modelaje. Debe contar estrictamente con
> todo lo que pide el PDF. Publicá la app en una URL pública para poder visualizar el trabajo (es una
> página modelo para un ejercicio). Mientras desarrollás, documentá lo relevante según lo que pide el
> PDF, creá un PDF con esa información y guardá los prompts en orden."*

Este prompt contiene **explícitamente** el pedido del diseño del registro y la definición/justificación
de la clave, tal como exige la consigna.

## Prompt 2 — Definiciones de diseño (respuestas del estudiante a la IA)

La IA repreguntó por la dirección creativa y el estudiante eligió:

- **Productos:** *Mezcla* → campeones y aspectos (coleccionables, en RP) **+** ítems de juego
  (equipo, en oro). El modelo debe cubrir ambos con la jerarquía `familia → categoria → producto`.
- **Estética:** **Hextech / Piltóver** (fondo azul-noche de Runeterra, oro hextech `#c8aa6e` y cian
  `#0ac8b9`), la más fiel al cliente y a la tienda del juego.

## Prompt 3 — Diseño del registro y la clave (pedido explícito a la IA)

> *"Diseñá el registro principal de Hextech Bazaar orientado al cliente-comprador (el Invocador),
> indicando nombre de cada campo, su tipo de dato y tamaño, e identificá la clave del registro
> justificando su elección. Integralo a un esquema snowflake con dimensiones normalizadas que
> muestre los cinco tipos de clave: primaria, foránea, secundaria, simple y compleja/compuesta."*

Resultado producido por la IA → ver [`modelo-datos.md`](modelo-datos.md) y el DDL comentado
[`db/schema.sql`](../db/schema.sql). Decisión de clave: PK surrogate `id_comprador`; email y Riot ID
(`nick_invocador#riot_tag`) como claves candidatas `UNIQUE`.

## Prompt 4 — Productos e imágenes reales del juego

> *"Necesito que descargues ítems o 'productos' del juego League of Legends y los agregues a la
> página, con sus imágenes."*

La IA obtuvo **datos e imágenes oficiales del juego** (campeones, aspectos e ítems) y los integró al
catálogo, mapeando cada producto a su **categoría**, **rareza** y **región de Runeterra**. El catálogo
quedó poblado con productos reales del universo de League of Legends.

## Prompt 5 — Prototipo funcional + publicación

> *"Armá el prototipo funcional (portada, catálogo con filtros, detalle de producto y carrito) y
> publicá la app en una URL pública para poder visualizarla."*

Resultado: un sitio navegable entre vistas (portada → catálogo con filtros y búsqueda → detalle de
producto → carrito), coherente con la temática y el registro diseñado, y una **URL pública** para la
demostración.

## Prompt 6 — Documentación y PDF de entrega

> *"Documentá lo relevante según el PDF y generá un PDF de entrega con todo (descripción, registro,
> clave, prompts y reflexión). Guardá los prompts en orden."*

Artefactos: este `prompts.md`, `modelo-datos.md`, `README.md` y el generador `docs/gen_pdf.py` que
produce el PDF de entrega.

---
*(Este archivo se actualiza cronológicamente a medida que avanza el desarrollo.)*
