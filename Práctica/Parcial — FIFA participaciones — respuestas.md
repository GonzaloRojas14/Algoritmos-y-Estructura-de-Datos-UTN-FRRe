# Respuestas — Ejercicio FIFA (Mundial de Clubes)

Calculadas aparte, sin usar la extensión. Abrí esto **después** de resolverlo.

---

## 1 y 2 — Goles y jugadores con roja

| Confederación | Equipo | Goles del equipo | Jugadores con ≥1 roja |
|---|---|--:|--:|
| CONCACAF | Monterrey | 12 | 1 |
| CONCACAF | Seattle | 17 | 1 |
| CONMEBOL | Boca | 17 | 2 |
| CONMEBOL | Palmeiras | 11 | 1 |
| CONMEBOL | River | 21 | 1 |
| UEFA | Bayern | 22 | 1 |
| UEFA | Real Madrid | 27 | 2 |

**Totales por confederación**

| Confederación | Goles |
|---|--:|
| CONCACAF | 29 |
| CONMEBOL | 49 |
| UEFA | 49 |

**Total del torneo: 127 goles**

---
## 3 — Archivo DESTACADOS

Goles de delanteros por equipo, y si el equipo entra (≥ 15):

| Confederación | Equipo | Goles de delanteros | ¿Entra? |
|---|---|--:|:--:|
| CONCACAF | Monterrey | 8 | no |
| CONCACAF | Seattle | 15 | sí |
| CONMEBOL | Boca | 16 | sí |
| CONMEBOL | Palmeiras | 9 | no |
| CONMEBOL | River | 18 | sí |
| UEFA | Bayern | 14 | no |
| UEFA | Real Madrid | 21 | sí |

Y el archivo queda con un registro por confederación:

| confederacion | goles |
|---|--:|
| CONCACAF | 15 |
| CONMEBOL | 34 |
| UEFA | 21 |

> Ojo con las confederaciones donde **ningún** equipo llega a 15: igual va el
> registro, con 0. Si tu algoritmo no las emite, fijate dónde grabás.
