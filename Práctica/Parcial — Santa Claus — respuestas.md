# Respuestas — Santa Claus

Calculadas aparte, sin la extensión. Abrilo **después** de resolverlo.

---

## Errores que tiene que informar (4)

| id_pais | id_niño | cod_evento | error |
|--:|--:|--:|---|
| 2 | 202 | 15 | ACTUALIZACION de un nino inexistente |
| 2 | 203 | 0 | ALTA de un nino que ya existe |
| 3 | 305 | 99 | RETIRO de un nino inexistente |
| 3 | 308 | 0 | ALTA de un nino que ya existe |

---
## a) Niños nuevos registrados

**2**

(los otros dos eventos con cod_evento = 0 son errores: el niño ya existía)

---
## b) Niño con mejor puntaje

**Helena Cruz**, con **74** puntos

> Ojo: los niños retirados (cod 99) ¿entran en la comparación? Acá los dejé
> afuera. Si tu algoritmo los incluye, el resultado cambia — es una decisión
> que conviene dejar comentada.

---
## Cómo queda el maestro

| id_pais | id_niño | nombre | puntaje | regalo | retirado |
|--:|--:|---|--:|---|:--:|
| 1 | 101 | Ana Perez | 60 | Telescopio |  |
| 1 | 102 | Bruno Diaz | -37 | Pelota |  |
| 1 | 103 | (nuevo 103) | 0 | Pelota |  |
| 1 | 105 | Carla Ruiz | 88 | Telescopio | sí |
| 2 | 201 | Diego Sosa | 27 | Autito |  |
| 2 | 203 | Elena Vega | 62 | Patineta |  |
| 2 | 207 | Facundo Lima | -16 | Libro |  |
| 3 | 301 | Gaston Mora | 30 | Rompecabezas | sí |
| 3 | 302 | Helena Cruz | 74 | Telescopio |  |
| 3 | 308 | Ivan Rojas | 15 | Pelota |  |
| 4 | 401 | Julia Nieto | 33 | Patineta |  |
| 4 | 404 | Kevin Ortiz | 10 | Libro |  |
| 4 | 407 | (nuevo 407) | 0 | Muneca |  |
| 4 | 409 | Lucia Paz | 19 | Libro |  |
