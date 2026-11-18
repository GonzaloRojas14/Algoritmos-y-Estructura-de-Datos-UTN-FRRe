---
fuente: https://aed-frre.github.io/practica/x/
tipo: guia-catedra
bloque: Práctica
materia: Algoritmos y Estructura de Datos
tags:
  - AED
  - guia-catedra
  - practica
---

> [!info] Guía de Trabajos Prácticos — cátedra AED UTN-FRRe
> Transcripción íntegra de [https://aed-frre.github.io/practica/x/](https://aed-frre.github.io/practica/x/), sin resumir ni alterar.
> Bajada el 24/08/2026.

---
# X. Parcial


### Ejercicio 1


---



La Municipalidad de Resistencia desea actualizar los valores de los terrenos luego de una rezonificación de los mismos. El valor final de cada terreno se calcula de la siguiente manera

Valor del Terreno = Superficie terreno (en M<sup>2</sup>) * valor del M<sup>2</sup> * coeficiente de incremento

Para ello cuenta con la siguiente información:

1.

Un archivo maestro de los terrenos con los siguientes datos:

**MAESTRO** Ordenado por Nro_Terreno

  - Nro_Terreno
  - Zona
  - Ubicacion
  - Superficie
  - Valor



Zona: codificadas de A a F
 Ubicación: codificada de 1 a 10
2.

Un arreglo V que contiene los valores del M<sup>2</sup> por zona.
3.

Un archivo de movimientos

**MOVIMIENTO** Ordenado por Nro_Terreno

  - Nro_Terreno
  - Zona
  - Ubicacion
  - Superficie
  - Cod_Mov



Se solicita actualizar (Alta Baja y Modificacion) los valores del archivo maestro, teniendo en cuenta que los unicos valores que se pueden actualizar es la zona y su valor.
