---
name: snowflake-data-modeling
description: Metodología para modelar datos relacionales en esquema snowflake aplicando la teoría de registros y claves (Unidad 2, AyED UTN-FRRe). Usar cuando se diseñe un modelo de datos, esquema de BD, DDL SQL, o cuando se mencione "snowflake", "registro", "clave primaria/foránea/secundaria", "modelo relacional" o "dimensiones normalizadas".
---

# Modelado de datos: esquema Snowflake + teoría de registros y claves

Combina el modelado dimensional **snowflake** con la teoría de la cátedra (registro = entidad con campos; clave = identificador). Objetivo: un modelo que demuestre explícitamente los distintos tipos de clave.

## 1. Conceptos base (Unidad 2)
- **Registro**: estructura que agrupa campos heterogéneos y representa una entidad del mundo real (Cliente, Producto, Pedido).
- **Campo**: unidad mínima; se define con **nombre + tipo + tamaño**. Puede ser *contenido* (simple, un dato elemental) o *continente* (compuesto, agrupa subcampos).
- **Selector de campo**: acceso con `.` → `Registro.Campo`.

## 2. Tipos de clave (a demostrar en el modelo)
| Clave | Definición | Cómo se ve en SQL |
|---|---|---|
| **Primaria (PK)** | Identifica de forma única e irrepetible un registro | `PRIMARY KEY` |
| **Foránea (FK)** | Puente hacia otra tabla/archivo distinto | `FOREIGN KEY ... REFERENCES` |
| **Secundaria** | No identifica único; sirve para agrupar/ordenar/buscar | `INDEX` sobre columna no-única |
| **Simple** | Formada por un único campo contenido | PK/clave de 1 columna |
| **Compleja / compuesta** | Formada por un campo continente (varios campos) | PK o UNIQUE de varias columnas |

Un modelo bien hecho debe contener **al menos un ejemplo de cada tipo** y justificar la elección de la clave del registro maestro.

## 3. Esquema Snowflake
Variante normalizada del star schema:
- **Tabla de hechos (fact)** en el centro: registra eventos medibles (p.ej. `hecho_venta` / `pedido_item`). Su clave suele ser **compuesta** (FKs a las dimensiones) o una surrogate PK con FKs.
- **Dimensiones** alrededor, **normalizadas en sub-dimensiones** (eso es lo que lo hace snowflake, no star): p.ej. `producto → categoria → familia`, `cliente → ciudad → provincia → pais`.
- Cada dimensión y sub-dimensión es un **registro** con su **PK simple** (surrogate) y atributos.
- Las relaciones jerárquicas normalizadas (categoria→familia) exhiben **FKs en cadena**.

### Reglas de diseño
1. Surrogate keys numéricas (`SERIAL`/`IDENTITY`) como PK de cada dimensión → claves simples estables.
2. Mantener la **clave de negocio** (DNI, SKU, email) como `UNIQUE` (clave candidata natural) además de la surrogate.
3. La **fact table** referencia dimensiones por FK; su grano (granularidad) debe declararse explícitamente (1 fila = 1 ítem de un pedido).
4. Normalizar las jerarquías de dimensión en tablas separadas (el "copo de nieve").
5. Tipos de dato y tamaños explícitos por campo (alineado con la teoría: nombre+tipo+tamaño).

## 4. Cardinalidades
- Documentar cada relación (1:1, 1:N, N:1, N:M).
- N:M se resuelve con tabla puente (que suele coincidir con la fact table o una bridge).
- Indicar el registro **maestro** del modelo y su orientación (¿qué entidad es el eje?).

## 5. Entregable de modelado
1. Diagrama (texto/ASCII o mermaid `erDiagram`) con tablas, PK/FK y cardinalidades.
2. **Diccionario del registro maestro**: tabla de campos con nombre, tipo, tamaño, descripción, y marca de clave.
3. **DDL SQL** (PostgreSQL) con PK, FK, UNIQUE, INDEX comentados por tipo de clave.
4. **Seed** mínimo coherente para poder navegar la app.
5. Justificación escrita de la clave del registro maestro (por qué esa y no otra).

## 6. Checklist de calidad
- [ ] ¿Hay fact table con grano declarado?
- [ ] ¿Las dimensiones están normalizadas (snowflake real, no star)?
- [ ] ¿Aparecen los 5 tipos de clave con ejemplo concreto?
- [ ] ¿El registro maestro tiene clave justificada?
- [ ] ¿Coherencia entre el dominio (e-commerce) y el modelo?
