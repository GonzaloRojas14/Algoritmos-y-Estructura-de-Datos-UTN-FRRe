---
tipo: filminas-anterior
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 6
titulo_original: 6-PROCESOS ESTADÍSTICOS
diapositivas: 13
fuente: PDF publicado por la cátedra
tags:
  - AED
  - filminas-anterior
  - teoria
  - arreglos
  - archivos
  - procesos-estadisticos
---

# 6 — Procesos Estadísticos

> [!warning] Versión anterior — reemplazada
> Esta es la transcripción de la presentación **vieja** (la que había antes de la revisión 2026 que subió el profesor a la carpeta Presentaciones). La vigente es [[6 — Procesos Estadísticos]]. Se conserva para comparar.


> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 13 diapositivas de **6-PROCESOS ESTADÍSTICOS** — *procesos que combinan el uso de Archivos y Arreglos* (Algoritmos y Estructuras de Datos 2026).
> Buena parte de esta presentación son **imágenes**: tablas, la consigna del ejemplo y el pseudocódigo resuelto. Todo eso está transcripto a texto acá. El PDF original queda en la misma carpeta: [[6 — Procesos Estadísticos (filminas).pdf]].

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

**PROCESOS ESTADÍSTICOS**

Procesos que combinan el uso de **Archivos** y **Arreglos**

Algoritmos y Estructuras de Datos — 2026

---

## 2 · Ejemplos

Cuadro estadístico de ejemplo (es una imagen en la filmina):

**Proporción del total de energía consumida, por sectores (en tantos por ciento)**
*Irlanda, 1980-2003*

| | 1980 | 1985 | 1990 | 1995 | 2000 | 2002 | 2003 |
|---|---|---|---|---|---|---|---|
| Transporte | 27,8 | 27,9 | 28,2 | 31,1 | 36,8 | 39,5 | 39,1 |
| Residencial | 34,1 | 33,9 | 30,4 | 27,6 | 24,3 | 23,7 | 24,0 |
| Industria | 31,5 | 27,2 | 23,6 | 22,1 | 21,4 | 19,5 | 18,8 |
| Agricultura | n/a¹ | n/a¹ | 3,5 | 3,7 | 3,1 | 2,9 | 2,8 |
| Servicio | 9,6 | 11,0 | 14,0 | 15,5 | 14,3 | 14,4 | 15,3 |
| **Total** | **100,0** | **100,0** | **100,0** | **100,0** | **100,0** | **100,0** | **100,0** |

¹ Los datos recogidos de la energía consumida por el sector agrícola no han sido recopilados hasta 1990.
*Fuente: Ministerio de Empresa Pública, Irlanda.*

---

## 3 · Qué son los INFORMES ESTADÍSTICOS

> [!important] Definición
> Es un informe que presenta un **conjunto de resultados cuantitativos** organizados de manera **tabular**, que permite obtener **información estadística** en términos de **cantidades, relaciones y porcentajes**.

Esquema de la diapositiva:

```
   ENTRADAS                                            SALIDAS
      │                    ┌──────────────┐               │
      ├──────────────────► │   PROCESO    │ ──────────────┤
      │                    │  (la matriz  │               │
      │                    │  estadística)│               ▼
      ▼                    └──────────────┘      Informe Estadístico
Entrada de datos desde un
terminal (otro programa,
una persona cargando
datos, un archivo, ….)
```

---

## 4 · Qué son los CUADROS ESTADÍSTICOS

> [!important] Definición
> Es una **matriz** dispuesta de modo tal que se puedan **presentar y organizar** los datos para clasificarlos adecuadamente a fin de poder **comparar e interpretar** las características de **dos o más variables**.

> La presentación de un cuadro tiene mucha importancia para el usuario, por lo tanto un **buen diseño transmite la calidad de los procedimientos previos** realizados en la recopilación, elaboración y análisis de los datos.

---

## 5 · Transición

*Ahora sí… veamos un* **PROCESO ESTADÍSTICO**

---

## 6 · TIPS — ¿Cuándo aplicar Procesos Estadísticos?

1. Necesito organizar información de **manera tabular**
2. Cuento con los **datos desordenados** desde un archivo u otra fuente de origen
3. Necesito obtener **información cuantitativa** clasificando por categorías
4. Necesito **totales generales**

> [!example] Ejemplo de la diapositiva
> Se cuenta con datos almacenados en un archivo que consta de: **id viaje, Ciudad de Origen, Ciudad Destino, Cantidad de pasajeros**. Se cuenta con **6 ciudades origen** y **10 ciudades destino**; los nombres se encuentran almacenados en vectores cuyo código se corresponde con el código de ciudad.
>
> Se quiere conocer:
> 1. La ciudad destino preferida por tener la mayor cantidad de pasajeros
> 2. La ciudad de origen menos elegida
> 3. La combinación ciudad origen-ciudad destino con menos pasajeros.

---

## 7 · METODOLOGÍA DE TRABAJO: CUADROS ESTADÍSTICOS

> [!important] Los 7 pasos — esto es la receta del tema
> 1. **Poner a 0** la matriz estadística
> 2. Iniciar **procesamiento** del archivo
> 3. **Recuperar datos** desde el registro
> 4. De acuerdo al valor **actualizar la matriz**
>    → Por ejemplo: `A[Reg.BD, Reg.Prob] := A[Reg.BD, Reg.Prob] + 1`
> 5. **Verificar** si se requiere actualizar filas/columnas totalizadoras
> 6. Continuar procesando el archivo **hasta el final**
> 7. **Mostrar la matriz** e informar los datos específicos que se soliciten

---

## 8 · El escenario resuelto — Tablas

**Tablas** (ordenado por BD, Cod_Tabla) — formato del registro del archivo:

| BD | COD_TABLA | DSC_TABLA | OWNER | FCH_CREACION | CANT_REG | AUDITADA | COD_PROBL |
|---|---|---|---|---|---|---|---|
| N(2) | N(6) | AN(30) | AN(30) | FECHA | N(10) | (SI – NO) | N(2) |

**Consigna:**

> Solo **30 problemas** pueden reportarse, y su detalle (AN (60)) se encuentra almacenado en un vector.
> Donde el Código del Problema se corresponde a la posición del mismo en el arreglo.
> El archivo cuenta con información de **50 Base de Datos**. Teniendo en cuenta esto, realizar un algoritmo que permita:
> - Informar el Problema más reportado.
> - Informar la Base de Datos con menor cantidad de problemas reportados.
> - Informar cuántas bases de datos reportaron problemas con el Código 22.
> - Qué cantidad de problemas fueron reportados en total.

---

## 9 · RESULTADO — la matriz estadística

La matriz es de **51 × 31**: 50 filas de bases de datos **+ una fila más** de totales, y 30 columnas de problemas **+ una columna más** de totales. La intersección final es el **total general**.

| | PROBLEMA 1 | PROBLEMA 2 | PROBLEMA 3 | … | PROBLEMA 29 | PROBLEMA 30 | **TOTAL x BD** |
|---|---|---|---|---|---|---|---|
| **BD 1** | 125 | 230 | 22 | … | 650 | 320 | **5236** |
| **BD 2** | 236 | 564 | 0 | … | 0 | 0 | **3256** |
| **BD 3** | 851 | 0 | 563 | … | 563 | 585 | **5620** |
| **BD 4** | 0 | 0 | 0 | … | 0 | 10 | **4562** |
| ⋮ | ⋮ | ⋮ | ⋮ | | ⋮ | ⋮ | ⋮ |
| **BD 49** | 2300 | 45 | 27 | … | 22 | 22 | **4502** |
| **BD 50** | 5 | 12 | 31 | … | 0 | 0 | **1000** |
| **TOTAL x PROBLEMA** | TOTAL PROB 1 | TOTAL PROBL 2 | TOTAL PROBL 3 | … | | | **TOTAL GENERAL** |

> [!tip] La clave del tema
> **Una fila más** (la 51) acumula el total por problema.
> **Una columna más** (la 31) acumula el total por base de datos.
> La celda `M[51,31]` es el **total general**.

---

## 10 · El algoritmo resuelto

En la diapositiva, junto al código, la cátedra pone: *"Animate a completar este algoritmo que resuelve el escenario…. volvé a hacerlo vos desde 0"*.

```
PROCESO
 Abrir E/(A)
 Leer(A, R_A)

 Para i:= 1 hasta 51 hacer
   Para j:= 1 hasta 31 hacer
     M[i,j]:=0
   FinPara
 FinPara

 Mientras NFDA(A) Hacer
   //se actualiza en 1 cada vez que aparece la BD y CodProb en el archivo
   M[R_A.BD,R_A.Cod_prob]:= M[R_A.BD,R_A.Cod_prob] + 1

   //se actualiza el total acumulado por BD
   M[R_A.BD,31]:= M[R_A.BD,31] + 1

   //se actualiza el total acumulado por PROBL
   M[51,R_A.Cod_prob]:= M[51,R_A.Cod_prob] + 1

   //se actualiza el total acumulado de problemas reportados
   M[51,31]:=M[51,31]+1

   Leer(A, R_A)
 FinMientras

 //item a
 mayor := 0
 Para j:= 1 hasta 30 hacer
  Si M[51,J] > mayor entonces
    mayor:=M[51,j]
    prob:=j
  FinSi
 FinPara
 Esc("El problema ", prob, "es el mas reportado con ", mayor, "errores")

 //item b
 menor:=HV
 Para j:= 1 hasta 50 hacer
   Si M[j, 31] < menor entonces
     menor:=M[j,31]
     BDmenor:=j
   FinSi
 FinPara
 Esc("La BD con menor cantidad de errores reportados es ",BDmenor)

 Esc("La cantidad de errores reportados para el Problema 22:", M[51,22])
 Esc("El total de errores es", M[51,31])
```

> [!info] Cómo leer este algoritmo
> - `M` es la matriz de **51 × 31** de la diapositiva 9.
> - El primer doble `Para` es el **paso 1** de la metodología: poner la matriz a 0.
> - Dentro del `Mientras` se hacen **cuatro actualizaciones** por cada registro leído: la celda del cruce, el total de la fila (columna 31), el total de la columna (fila 51) y el total general (`M[51,31]`).
> - `menor:=HV` inicializa con el **mayor valor posible** (High Value) para que la primera comparación siempre entre.
> - Los ítems c y d de la consigna se resuelven con un simple acceso directo: `M[51,22]` y `M[51,31]`.

> [!bug] Detalles de la filmina
> - En el ítem a escribe `M[51,J]` con **J mayúscula** y en la línea siguiente `M[51,j]` en minúscula. Es la misma variable del `Para`; en el parcial usá una sola forma.
> - `mayor`, `menor`, `prob`, `BDmenor`, `i`, `j` y la matriz `M` **no están declaradas** — la filmina muestra sólo el bloque `PROCESO`, sin `AMBIENTE`. Al resolverlo vos, declaralos.
>
> Ver [[errores-y-trampas]].

---

## 11 · PARA REPASAR

*(diapositiva de transición)*

---

## 12 · PROBLEMA 1

> Una tienda de comercio electrónico cuenta con información de ventas de **25 productos estrellas** de su negocio, almacenada en un **archivo desordenado** cuyo registro presenta el siguiente formato:
>
> `FECHA_TRANSACCION | COD_PRODUCTO | CANTIDAD_VENDIDA | PCIO_UNIT`
>
> Las ventas corresponden al período que va desde **Marzo a Agosto de 2020**.
> El nombre del producto se encuentra almacenado en un **vector de 25 posiciones**, donde la posición se corresponde con el código del producto (Cod 01 → Posición 1, Cod 02 → Posición 2, … Cod 25 → Posición 25).
>
> Se solicita un algoritmo que procese las **ventas diarias del Mes de Agosto** e informe:
> - La venta más alta informando día y producto
> - El total de ventas de Agosto
> - El total de ventas por producto
> - Qué día se recaudó más
> - Qué día se recaudó menos que el promedio de ventas diario

> [!tip] Pista de dimensionamiento
> Agosto tiene 31 días y hay 25 productos → matriz de **31 × 25**, más la fila y la columna totalizadoras → **32 × 26**.

---

## 13 · PROBLEMA 2

> Una empresa inmobiliaria requiere el seguimiento de **transacciones online válidas** de acuerdo al **origen** y **nivel** de cada una. Para ello se cuenta con un archivo que **no está ordenado** y cuyo formato de registro es como sigue:

| DEPARTAMENTO | ORIGEN | NIVEL | VALIDA |
|---|---|---|---|
| N(6) | (1: Web – 2: Mobile – 3: Call Center) | (1…5) | (SI-NO) |

> **Se pide:**
> a) En qué nivel y cuál origen se registró la menor cantidad de transacciones.
> b) Cuál es el nivel con mayor cantidad de transacciones
> c) Qué porcentaje de transacciones representa cada nivel sobre el total.
> d) Qué niveles tienen un total de transacciones que superan en un 10% al de mayor cantidad de transacciones.
> e) Cuál es el origen que menor transacciones válidas ha registrado

> [!tip] Pista de dimensionamiento
> 3 orígenes × 5 niveles → matriz de **3 × 5**, más fila y columna totalizadoras → **4 × 6**.
> Ojo con el filtro: sólo cuentan las transacciones con `VALIDA = SI` (ítem e lo dice explícito).

---

## 🔗 Notas relacionadas

- [[4 — Arreglos]] · [[5 — Búsqueda y Ordenamiento]] — las dos presentaciones anteriores
- [[6 — Procesos Estadísticos (filminas).pdf]] — el PDF original, con las imágenes tal cual
- [[Corte de Control]] · [[Actualización]] — teoría del sitio de la cátedra sobre procesamiento de archivos
- [[plantillas]] — las plantillas canónicas de procesamiento secuencial de archivos
- [[2.2 — Archivos Secuenciales]] · [[2.3 — Archivos Indexados]] — ejercicios de archivos de la Guía de Cátedra
