---
fuente: Ejercicios.rar (apuntes de un compañero, notas de Obsidian)
tipo: resoluciones
materia: Algoritmos y Estructura de Datos
tags:
  - AED
  - resoluciones
---

# 📗 Resoluciones de la Guía de Cátedra

Las notas de [[📘 Guía de Cátedra — Índice|la guía]] tienen los **enunciados**. Acá están las
**resoluciones** de una parte de ellos, con la misma numeración.

> [!warning] Leelas con desconfianza
> Esto **no es material de la cátedra**. Son los apuntes personales de alguien que cursó, así
> que las soluciones pueden estar mal, incompletas o desactualizadas. Tres cosas concretas:
>
> 1. **La mayoría está sin terminar de revisar.** El propio autor marcó solo una parte como
>    `#Completed`; el resto quedó en `#InProgress`. En las tablas de abajo eso es ✅ y 🟡.
> 2. **Usan una notación que no es la nuestra.** Ver la sección de abajo.
> 3. **Cinco notas las generó una IA**, no salieron de la cátedra. Están apartadas en su
>    propia carpeta.
>
> Sirven para comparar tu solución contra otra, no como respuesta oficial.

---

## ⚠️ La notación que usan

Todas las resoluciones están escritas en **notación vieja**, sin una sola excepción:
`finSi`, `finMientras`, `finAccion`, `finProcedimiento`. De 83 archivos, **0 usan `FIN_SI`**.
Eso es válido según [[sintaxis-completa|§1 de la sintaxis]] — pero es la otra mitad de la tabla,
no la que veníamos usando.

Además aparecen cosas que **no existen en ningún material de la cátedra** que tengamos:

| Lo que escriben | Problema |
|---|---|
| `finAmbiente` (en 72 de 83 archivos) | El `Ambiente` no se cierra. No figura ni en el libro, ni en las filminas, ni en la guía. |
| `Entonces:` / `Hacer:` / `Es:` con dos puntos | Es justamente el error de tipeo que la extensión marca como diagnóstico. |
| Sentencias terminadas en `;` | La cátedra no usa terminador de sentencia. |
| `Romper` | Un `break`. No existe en el pseudocódigo de la cátedra. |

**Ninguna de estas resoluciones corre en la extensión tal como está.** Si querés ejecutar alguna,
hay que traducirla primero. La conversión es mecánica salvo `finAmbiente` y `Romper`, que hay
que sacar a mano.

---

## 2.1 — Secuencias  · 22 de 32 ejercicios de la guía

| # | Estado | Código | Enunciado |
|---|:--:|:--:|---|
| [[Guía-Ejercicio_2.1.1-AlgoritmosI\|2.1.1]] | 🟡 | sí | Dada una secuencia de letras del alfabeto que finaliza con una marca '*', contar cuantas letras |
| [[Guía-Ejercicio_2.1.2-AlgoritmosI\|2.1.2]] | 🟡 | sí | Dada una secuencia de letras del alfabeto que finaliza con la letra "Z", contar cuantas consona |
| [[Guía-Ejercicio_2.1.3-AlgoritmosI\|2.1.3]] | 🟡 | sí | Se dispone de una secuencia de caracteres y se desea obtener una secuencia de salida que result |
| [[Guía-Ejercicio_2.1.4-AlgoritmosI\|2.1.4]] | 🟡 | sí | Se dispone de una secuencia de números de socios, y se desea saber la cantidad de socios que es |
| [[Guía-Ejercicio_2.1.5-AlgoritmosI\|2.1.5]] | 🟡 | sí | La secuencia de socios del problema anterior tiene el inconveniente de que los números están or |
| [[Guía-Ejercicio_2.1.6-AlgoritmosI\|2.1.6]] | 🟡 | sí | Dada una secuencia de enteros que almacena la cantidad de habitantes de las ciudades capitales  |
| [[Guía-Ejercicio_2.1.7-AlgoritmosI\|2.1.7]] | 🟡 | sí | Se tiene una secuencia de enteros que contiene todos los CUIT de los empleados de una empresa,  |
| [[Guía-Ejercicio_2.1.8-AlgoritmosI\|2.1.8]] | 🟡 | sí | Teniendo en cuenta el ejercicio anterior, se solicita que la secuencia de salida sea una secuen |
| [[Guía-Ejercicio_2.1.9-AlgoritmosI\|2.1.9]] | 🟡 | sí | Se dispone de una secuencia de caracteres. Se desea determinar la cantidad de palabras que comi |
| [[Guía-Ejercicio_2.1.10-AlgoritmosI\|2.1.10]] | 🟡 | sí | Se dispone de una secuencia de caracteres. Se desea contar la cantidad de palabras que comienza |
| [[Guía-Ejercicio_2.1.11-AlgoritmosI\|2.1.11]] | 🟡 | sí | Dada una secuencia de caracteres, determinar la cantidad de palabras de 4 caracteres (letras) |
| [[Guía-Ejercicio_2.1.12-AlgoritmosI\|2.1.12]] | 🟡 | sí | Se dispone de una secuencia de caracteres. Se desea listar las palabras que comiencen con "ALG" |
| [[Guía-Ejercicio_2.1.13-AlgoritmosI\|2.1.13]] | 🟡 | sí | A partir del ejercicio anterior, determinar el porcentaje que representan las palabras que comi |
| [[Guía-Ejercicio_2.1.14-AlgoritmosI\|2.1.14]] | 🟡 | sí | Se dispone de una secuencia de caracteres y se desea saber la cantidad de caracteres (incluidos |
| [[Guía-Ejercicio_2.1.15-AlgoritmosI\|2.1.15]] | 🟡 | sí | Se desea saber la cantidad promedio de palabras que contienen las oraciones de una secuencia de |
| [[Guía-Ejercicio_2.1.16-AlgoritmosI\|2.1.16]] | 🟡 | sí | Se dispone de una secuencia de números de DNI asignados a un circuito electoral, generar otra s |
| [[Guía-Ejercicio_2.1.17-AlgoritmosI\|2.1.17]] | 🟡 | sí | Se desea calcular el costo de un telegrama, que se determina en función del número de palabras  |
| [[Guía-Ejercicio_2.1.18-AlgoritmosI\|2.1.18]] | 🟡 | sí | Escribir un algoritmo que produzca una secuencia de salida que contenga una oración formada por |
| [[Guía-Ejercicio_2.1.22-AlgoritmosI\|2.1.22]] | 🟡 | sí | La empresa Ideas Argentinas S.A. posee datos de sus empleados en dos secuencias de caracteres;  |
| [[Guía-Ejercicio_2.1.30-AlgoritmosI\|2.1.30]] | 🟡 | sí | El siguiente es un ejercicio del primer recuperatorio del primer parcial del año 2017: |
| [[Guía-Ejercicio_2.1.31-AlgoritmosI\|2.1.31]] | 🟡 | sí | El siguiente es un ejercicio del primer parcial del año 2017: La empresa TICKET-TEC ha generado |
| [[Guía-Ejercicio_2.1.32-AlgoritmosI\|2.1.32]] | 🟡 | sí | Se posee una secuencia con los mensajes internos enviados entre los empleados de una empresa, l |

## 2.2 — Archivos Secuenciales  · 25 de 25 ejercicios de la guía

| # | Estado | Código | Enunciado |
|---|:--:|:--:|---|
| [[Guía-Ejercicio_2.2.1-AlgoritmosI\|2.2.1]] | 🟡 | sí | Se dispone de una secuencia con los datos de los alumnos de la facultad: |
| [[Guía-Ejercicio_2.2.2-AlgoritmosI\|2.2.2]] | 🟡 | sí | Se dispone de una secuencia de facturas con los siguientes datos: |
| [[Guía-Ejercicio_2.2.3-AlgoritmosI\|2.2.3]] | 🟡 | sí | Dada la siguiente secuencia de datos con el siguiente formato: |
| [[Guía-Ejercicio_2.2.4-AlgoritmosI\|2.2.4]] | 🟡 | sí | A partir de la secuencia del ejercicio Guía-Ejercicio_2.2.1-AlgoritmosIRegistro de Entrada se d |
| [[Guía-Ejercicio_2.2.5-AlgoritmosI\|2.2.5]] | 🟡 | sí | A partir de la secuencia del ejercicio 2.01 se desea generar un listado con los alumnos que apr |
| [[Guía-Ejercicio_2.2.6-AlgoritmosI\|2.2.6]] | 🟡 | sí | Se cuenta con una secuencia que contiene el Apellido y Nombre y Promedio General de los Graduad |
| [[Guía-Ejercicio_2.2.7-AlgoritmosI\|2.2.7]] | 🟡 | sí | Se dispone de un archivo con los datos de un padrón electoral con la siguiente información: |
| [[Guía-Ejercicio_2.2.8-AlgoritmosI\|2.2.8]] | 🟡 | sí | De los datos del siguiente ejercicio: |
| [[Guía-Ejercicio_2.2.9-AlgoritmosI\|2.2.9]] | 🟡 | sí | Una casa deportiva dispone de un archivo de productos, ordenado por código de producto, que con |
| [[Guía-Ejercicio_2.2.10-AlgoritmosI\|2.2.10]] | 🟡 | sí | Del archivo general de alumnos de la U.T.N. - Facultad Regional Resistencia, ordenado por carre |
| [[Guía-Ejercicio_2.2.11-AlgoritmosI\|2.2.11]] | 🟡 | sí | Se dispone de un archivo con datos de los alumnos de la U.T.N. con la siguiente información par |
| [[Guía-Ejercicio_2.2.12-AlgoritmosI\|2.2.12]] | 🟡 | sí | Dada una secuencia con información de población de un PAIS: |
| [[Guía-Ejercicio_2.2.13-AlgoritmosI\|2.2.13]] | 🟡 | sí | Un Casino de la región ha notado un incremento en los costos de las reparaciones de tragamoneda |
| [[Guía-Ejercicio_2.2.14-AlgoritmosI\|2.2.14]] | 🟡 | sí | Dados el siguiente fichero con datos de un censo de la ciudad de Resistencia: |
| [[Guía-Ejercicio_2.2.15-AlgoritmosI\|2.2.15]] | 🟡 | sí | El organismo del cual dependen las escuelas de un distrito lleva un archivo con los registros p |
| [[Guía-Ejercicio_2.2.16-AlgoritmosI\|2.2.16]] | 🟡 | sí | Construir un algoritmo que a partir de un fichero de películas nuevas conteniendo: |
| [[Guía-Ejercicio_2.2.17-AlgoritmosI\|2.2.17]] | 🟡 | sí | La Secretaria Académica de la Facultad lanza un proyecto para incentivar a aquellos alumnos que |
| [[Guía-Ejercicio_2.2.18-AlgoritmosI\|2.2.18]] | 🟡 | sí | Un supermercado desea conocer la totalidad de unidades existentes de cada artículo a fin de hac |
| [[Guía-Ejercicio_2.2.19-AlgoritmosI\|2.2.19]] | 🟡 | sí | En una Empresa Farmacéutica se posee un archivo MAE_REMEDIOS (ordenado por Clave: Farmacia + Me |
| [[Guía-Ejercicio_2.2.20-AlgoritmosI\|2.2.20]] | 🟡 | sí | Se desea generar una secuencia, a partir de la secuencia del problema Guía-Ejercicio_2.2.1-Algo |
| [[Guía-Ejercicio_2.2.21-AlgoritmosI\|2.2.21]] | 🟡 | sí | En un práctico para la Facultad un grupo de alumnos debe implementar una Red Social llamada UTN |
| [[Guía-Ejercicio_2.2.22-AlgoritmosI\|2.2.22]] | 🟡 | sí | IDEM ejercicio 2.21 pero agregando al enunciado: “Al finalizar el proceso se desea conocer: el  |
| [[Guía-Ejercicio_2.2.23-AlgoritmosI\|2.2.23]] | 🟡 | sí | Una empresa de distribución de energía eléctrica posee un archivo maestro con los siguientes da |
| [[Guía-Ejercicio_2.2.24-AlgoritmosI\|2.2.24]] | 🟡 | sí | Una obra social lleva el control de los costos que le insume cada afiliado. Considerando como c |
| [[Guía-Ejercicio_2.2.25-AlgoritmosI\|2.2.25]] | 🟡 | **no** | IDEM Guía-Ejercicio_2.2.21-AlgoritmosIDescripción de la tarea pero suponiendo que hay mas de un |

## 2.3 — Archivos Indexados  · 1 de 12 ejercicios de la guía

| # | Estado | Código | Enunciado |
|---|:--:|:--:|---|
| [[Guía-Ejercicio_2.3.1.a-AlgoritmosI\|Guía-Ejercicio_2.3.1.a-Algor]] | 🟡 | **no** | Dado un fichero secuencial de Facturas, ordenado por Nro. de Cliente y Nro. de Factura, con la  |

## 4 — Listas  · 11 de 17 ejercicios de la guía

| # | Estado | Código | Enunciado |
|---|:--:|:--:|---|
| [[Clase-29_10_2024-Ejercicio_1-AlgoritmosI\|1]] | 🟡 | sí | Usando las operaciones de Lista, escribir un procedimiento AGRUPA (PRIM, ULT: puntero a nodo; A |
| [[Clase-29_10_2024-Ejercicio_2-AlgoritmosI\|2]] | 🟡 | **no** | Una oficina postal quiere mejorar la organización de los pedidos y envíos diarios. Cada día, re |
| [[Guía-Ejercicio_4.1-AlgoritmosI\|4.1]] | ✅ | sí | Diseñar un algoritmo para acceder, eliminar o insertar el k-ésimo elemento de una lista (siendo |
| [[Guía-Ejercicio_4.2-AlgoritmosI\|4.2]] | ✅ | sí | Se dispone de una lista simplemente encadenada de números enteros, diseñar un algoritmo que a p |
| [[Guía-Ejercicio_4.3-AlgoritmosI\|4.3]] | ✅ | sí | Dada una lista simplemente encadenada de números diseñar un algoritmo que calcule en forma inde |
| [[Guía-Ejercicio_4.4-AlgoritmosI\|4.4]] | ✅ | sí | Se dispone de una lista simplemente encadenada cuyos registros están ordenados en forma ascende |
| [[Guía-Ejercicio_4.5-AlgoritmosI\|4.5]] | ✅ | sí | Dada una lista simplemente encadenada que contiene datos de todas las provincias de la Repúblic |
| [[Guía-Ejercicio_4.6-AlgoritmosI\|4.6]] | ✅ | sí | En el restaurante ÑOQUIS se está pensando en una solución informática para el soporte de datos  |
| [[Guía-Ejercicio_4.7-AlgoritmosI\|4.7]] | ✅ | sí | Genere un algoritmo que recorra una secuencia texto y genere una lista simplemente encadenada c |
| [[Guía-Ejercicio_4.8-AlgoritmosI\|4.8]] | ✅ | sí | Escribir un algoritmo que permita buscar, insertar o borrar un elemento identificado con una cl |
| [[Guía-Ejercicio_4.9-AlgoritmosI\|4.9]] | 🟡 | **no** | Dada una lista circular de 8 elementos que contienen, cada uno, un valor numérico entero para e |

## 5 — Recursividad  · 12 de 28 ejercicios de la guía

| # | Estado | Código | Enunciado |
|---|:--:|:--:|---|
| [[Guia-Ejercicio-5.1.1-AlgoritmosI\|5.1.1]] | ✅ | sí | Calcular el factorial de un número positivo n. Tener en cuenta la definición matemática de n!: |
| [[Guia-Ejercicio-5.1.2-AlgoritmosI\|5.1.2]] | 🟡 | sí | Dado un número n como parámetro de entrada, calcular el n-ésimo número de la serie de Fibonacci |
| [[Guia-Ejercicio-5.1.3-AlgoritmosI\|5.1.3]] | 🟡 | sí | Dados dos números: a y b. Calcule la potencia a^b, usando sólo multiplicaciones sucesivas. |
| [[Guia-Ejercicio-5.1.4-AlgoritmosI\|5.1.4]] | 🟡 | sí | Construir un algoritmo recursivo que permita determinar si los dígitos de un número nn dado son |
| [[Guia-Ejercicio-5.1.5-AlgoritmosI\|5.1.5]] | 🟡 | sí | Dados dos números enteros, divídalos (división entera) y muestre el resultado, usando sólo la o |
| [[Guia-Ejercicio-5.1.6-AlgoritmosI\|5.1.6]] | 🟡 | sí | Determine recursivamente si un número dado es par o impar, usando sólo la operación resta. |
| [[Guia-Ejercicio-5.1.7-AlgoritmosI\|5.1.7]] | 🟡 | sí | El algoritmo de Euclides para encontrar el MCD(máximo común divisor) de dos números enteros pos |
| [[Guia-Ejercicio-5.1.8-AlgoritmosI\|5.1.8]] | 🟡 | sí | Dado un vector de 10 números enteros, calcular la suma de sus elementos |
| [[Guia-Ejercicio-5.2.1-AlgoritmosI\|5.2.1]] | 🟡 | sí | Imprimir las cifras de un número n (siendo n≥0) en orden inverso al original. Por ej.: el inver |
| [[Guia-Ejercicio-5.2.2-AlgoritmosI\|5.2.2]] | 🟡 | sí | Leer una palabra (una cadena de caracteres) y la cantidad de caracteres y generar su palíndromo |
| [[Guia-Ejercicio-5.2.3-AlgoritmosI\|5.2.3]] | 🟡 | sí | Dada una lista de nombres ordenada en forma ascendente, construir un procedimiento recursivo qu |
| [[Guia-Ejercicio-5.2.4-AlgoritmosI\|5.2.4]] | 🟡 | sí | Para convertir un número decimal a binario, simplemente debe dividirse sucesivas veces por dos  |

## 5.3 — Árboles  · 5 notas

| # | Estado | Código | Enunciado |
|---|:--:|:--:|---|
| [[Guia-Ejercicio-5.3.1-AlgoritmosI\|5.3.1]] | 🟡 | sí | Responda las siguientes preguntas para el árbol de la figura: |
| [[Guia-Ejercicio-5.3.2-AlgoritmosI\|5.3.2]] | 🟡 | **no** | ¿Cuántos caminos de longitud 3 hay en el árbol representado en la figura anterior? |
| [[Guia-Ejercicio-5.3.3-AlgoritmosI\|5.3.3]] | 🟡 | sí | Dada la expresión de la siguiente línea, dibujar el árbol equivalente |
| [[Guia-Ejercicio-5.3.4-AlgoritmosI\|5.3.4]] | 🟡 | sí | 1. Indique el resultado del recorrido post-orden |
| [[Guia-Ejercicio-5.3.5-AlgoritmosI\|5.3.5]] | 🟡 | sí | Para las siguientes expresiones: |

## Actualización (extra)  · 2 notas

| # | Estado | Código | Enunciado |
|---|:--:|:--:|---|
| [[Biblioteca-Ejercicio-actualización\|Biblioteca-Ejercicio-actuali]] | ✅ | sí | En la biblioteca de la UTN-FRRe se posee un archivo MAE_LIBROS (ordenado por Clave: ID_Libro) c |
| [[ventaCombustible-Ejercicio-ActualizaciónIndexada-AlgoritmosI\|ventaCombustible-Ejercicio-A]] | 🟡 | sí | Una empresa dedicada a la venta de combustibles para automotores anunció una promoción mediante |

## Generados con IA (NO son de la cátedra)  · 5 notas

| # | Estado | Código | Enunciado |
|---|:--:|:--:|---|
| [[Asignación de Alumnos a Aulas-IA Ejercicios-AlgoritmosI\|Asignación de Alumnos a Aula]] | 🟡 | **no** | Ejercicio 1: Asignación de Alumnos a Aulas (Listas) |
| [[Eliminación Condicional con Listas Doblemente Enlazadas-IA Ejercicios-AlgoritmosI\|Eliminación Condicional con ]] | 🟡 | sí | Dada una lista doblemente enlazada con información sobre los productos en stock de un almacén,  |
| [[Gestion de Socios de Supermercado-Ejercicios IA-AlgoritmosI\|Gestion de Socios de Superme]] | ✅ | sí | Ejercicio 1: Gestión de Socios de Supermercado (Listas) |
| [[Preguntas Sobre Unidad III-Ejercicios IA-Algoritmos I\|Preguntas Sobre Unidad III-E]] | 🟡 | sí | 1. Reconstrucción y propiedades de árboles (3 puntos) |
| [[Validación de Compras con Tarjeta de Crédito-Ejercicios IA-Algoritmos I\|Validación de Compras con Ta]] | 🟡 | sí | Ejercicio 2: Validación de Compras con Tarjeta de Crédito (Recursividad) |

---

## Lo que NO cubre

La guía tiene 275 ejercicios; acá hay 78 resueltos (más 5 generados con IA). Los huecos grandes:

- **Unidad 1** (datos elementales, subacciones): 58 ejercicios, **ninguno resuelto**.
- **Unidad 3** (arreglos): 32 ejercicios, **ninguno resuelto** — justo el tema del parcial.
- **2.3 (indexados)**: 1 de 12.
- **Complementarios**: 66 ejercicios, ninguno.

[[📘 Guía de Cátedra — Índice|← Volver a la Guía]]
