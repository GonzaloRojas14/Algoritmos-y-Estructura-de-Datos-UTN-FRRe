# Actividad Formativa N.º 3 — Estación de Monitoreo: Vectores y Matrices en Acción

**Algoritmos y Estructuras de Datos — ISI — UTN-FRRe — 2026**
**Alumno:** Rojas Gonzalo — **Legajo:** 28838 — **Comisión:** K1.4

> **Cómo está armado este borrador.** Las Partes 0 a 4 están completas. Falta la
> **Reflexión**, marcada `[A REDACTAR]`. Antes de pasar a PDF hay que borrar este
> recuadro.

---

## Parte 0 — Investigación previa

**1. Qué es una estación de monitoreo y qué datos produce.**
Una estación de monitoreo es un conjunto de sensores que miden una magnitud, en este caso la temperatura ambiente, cada cierto tiempo, y registran cada lectura con su hora. Cada sensor entrega sus datos por separado: por ejemplo, el Sensirion SHT3x mide de −40 °C a 125 °C con una precisión típica de ±0,2 °C y entrega cada lectura en forma digital. Así, lo que produce la estación es una lista de lecturas con tres datos: qué sensor, en qué momento y qué valor. Esos datos sirven para seguir cómo evoluciona la temperatura y, junto con muchas otras lecturas, para ayudar a predecir cómo puede estar el clima en los días siguientes.
*Fuente: Sensirion, datasheet SHT3x-DIS — https://sensirion.com/file/datasheet_sht3x_digital*

**2. Rango de valores y umbral.**
Según las normales 1991–2020 de la estación Resistencia Aero, en octubre la temperatura máxima media es de 29 °C y la mínima media de 17 °C. Elegí 40 °C como umbral de falla, y me convence por la desviación estándar de las temperaturas. En mi dataset, las lecturas normales tienen un promedio de 23,3 °C y un desvío estándar de 3,8 °C. El valor normal más alto (33,7 °C) está a 2,7 desvíos del promedio, mientras que 40 °C está a 4,4. Una lectura por encima de 40 °C se aleja tanto de la variación normal que es mucho más probable que sea una falla del sensor que una temperatura real.
*Fuente: normales CLINO 1991–2020 de la OMM, Resistencia Aero — https://www.climate-zone.com/climate/ar/resistencia*

**3. Qué es un CSV y por qué se usa.**
Un CSV es un archivo de texto plano con un registro por línea y los campos separados por comas, como lo define la RFC 4180. Lo usé porque es más legible y más óptimo para guardar datos que después se van a procesar con código: se puede abrir y leer directamente, y en el pseudocódigo cada línea se lee como un registro de tres campos (sensor, nro y valor).
*Fuente: RFC 4180 — https://www.rfc-editor.org/info/rfc4180*

**4. Frecuencia de muestreo y N.**
Elegí una lectura cada 10 minutos, lo que da N = 144 lecturas por sensor en un día. La guía de instrumentos de la OMM trabaja con promedios de temperatura de 1 a 10 minutos en estaciones automáticas. Tomar lecturas cada 10 minutos da más detalle de cómo cambia la temperatura a lo largo del día que, por ejemplo, una lectura por hora, que daría solo 24. También permite ver fallas cortas: una racha de 5 lecturas dura 50 minutos.
*Fuente: Branzov, "Influence of the averaging period on temperature measurements", OMM (TECO-2012) — https://old.wmo.int/extranet/pages/prog/www/IMOP/publications/IOM-109_TECO-2012/Session3/P3_03_Branzov_Influence_averaging_period_Temp_measur.pdf*

---

## Parte 1 — Generación de datos con IA

**Decisiones (salen de la Parte 0):** temperatura ambiente en Resistencia, un día
de octubre; M = 5 sensores; N = 144 lecturas por sensor (una cada 10 minutos).

### Prompt utilizado

> Escribí un script en Python, usando solo la biblioteca estándar, que simule una
> estación de monitoreo de temperatura ambiente en Resistencia (Chaco) durante un
> día de octubre. Tiene que haber 5 sensores con 144 lecturas cada uno (una cada
> 10 minutos). Cada sensor sigue un ciclo diario realista, con la mínima de
> madrugada cerca de 17-18 °C y la máxima a media tarde cerca de 29 °C, más ruido
> de medición chico. El sensor 3 tiene que comportarse distinto: descalibrado,
> con una deriva lenta hacia arriba y más ruido. Inyectá rachas de valores fuera
> de rango (entre 45 y 60 °C) en posiciones fijas: sensor 2 desde la lectura 61
> (8 lecturas), sensor 4 desde la 97 (6 lecturas) y sensor 5 desde la 31
> (3 lecturas). Exportá un CSV con encabezado y las columnas sensor, nro y valor,
> una línea por lectura, y otro CSV con las rachas inyectadas. Usá una semilla
> fija para que el resultado sea reproducible.

`[Si usaste más de un prompt o fuiste corrigiendo, poné acá los que usaste realmente, en orden.]`

### Script

Archivo `generar_lecturas.py` (va completo en el anexo del PDF). Resumen de lo que hace:

| Sensor | Comportamiento |
|---|---|
| 1 | Abrigo meteorológico: ciclo diario normal, ruido ±0,3 °C |
| 2 | A la sombra: un poco más fresco |
| **3** | **Distinto: descalibrado.** Deriva de +0,03 °C por lectura (+4,3 °C al final del día) y ruido ±1,2 °C |
| 4 | Zona más expuesta: ciclo más amplio |
| 5 | Cerca de vegetación: más fresco y con menos amplitud |

### Muestra del CSV generado (`lecturas.csv`, 720 lecturas)

```
sensor,nro,valor
1,1,19.9
2,1,19.5
3,1,18.6
4,1,20.2
5,1,19.0
1,2,19.8
...
```

La estación registra los 5 sensores cada 10 minutos, así que el archivo viene
ordenado por número de lectura y no por sensor. Los procedimientos de carga no
dependen de ese orden: cada registro dice a qué sensor y a qué posición pertenece.

### Anomalías inyectadas (verdad conocida)

| Sensor | Posición (nro de inicio) | Longitud | Horario | Valores |
|---|---|---|---|---|
| 2 | 61 | 8 | 10:00 a 11:10 | 46,8 a 59,5 °C |
| 4 | 97 | 6 | 16:00 a 16:50 | 51,0 a 58,4 °C |
| 5 | 31 | 3 | 05:00 a 05:20 | 51,6 a 53,9 °C |

La racha del sensor 5 es **más corta que la longitud mínima** que va a usar el
algoritmo (5 lecturas), a propósito, para ver qué pasa en la validación.

---

## Parte 2 — Vector: kit de análisis reutilizable

Declaraciones (el registro del CSV y el archivo que lo contiene):

```
M = 5;              // cantidad de sensores
N = 144;            // lecturas por sensor: 24 h, una cada 10 minutos
UMBRAL = 40.0;      // °C: más de 10 °C por encima de la máxima normal de octubre
LONG_MIN = 5;       // lecturas seguidas sobre el umbral para hablar de racha

lectura = registro
    sensor: entero;
    nro: entero;
    valor: real;
fin_reg;

archLecturas: ARCHIVO de lectura;
lecturas: ARREGLO[1..N] de real;
```

Los cuatro procedimientos reciben **todo por parámetro**: el vector, su tamaño, el
umbral y la longitud mínima. Ninguno tiene un valor fijo adentro, y por eso se
pueden reutilizar sin cambios en la Parte 3.

### Carga

```
// Recorre el archivo completo y se queda con las lecturas de un sensor:
// cada valor va a la posición que indica su campo nro.
Procedimiento CargarSensor(nroSensor: entero; var v: ARREGLO[1..N] de real);
Ambiente
    reg: lectura;
Proceso
    ABRIR E(archLecturas);
    LEER(archLecturas, reg);
    MIENTRAS NFDA(archLecturas) HACER
        SI reg.sensor = nroSensor ENTONCES
            v[reg.nro] := reg.valor;
        FIN_SI;
        LEER(archLecturas, reg);
    FIN_MIENTRAS;
    CERRAR(archLecturas);
fin_proc;
```

### Estadísticas

```
// Una sola pasada: máximo y mínimo con sus posiciones, y el promedio de las tam posiciones.
Procedimiento Estadisticas(v: ARREGLO[1..N] de real; tam: entero;
                           var max: real; var posMax: entero;
                           var min: real; var posMin: entero;
                           var prom: real);
Ambiente
    i: entero;
    suma: real;
Proceso
    max := v[1];
    posMax := 1;
    min := v[1];
    posMin := 1;
    suma := v[1];
    PARA i := 2 HASTA tam HACER
        SI v[i] > max ENTONCES
            max := v[i];
            posMax := i;
        FIN_SI;
        SI v[i] < min ENTONCES
            min := v[i];
            posMin := i;
        FIN_SI;
        suma := suma + v[i];
    FIN_PARA;
    prom := suma / tam;
fin_proc;
```

Arranca con el primer elemento como máximo y mínimo provisorios, en vez de con un
valor inventado como 0 o 9999. Así funciona con cualquier rango de valores.

### Búsqueda por umbral

```
// Posición de la primera lectura que supera el umbral; 0 si ninguna lo supera.
Procedimiento BuscarSupera(v: ARREGLO[1..N] de real; tam: entero;
                           umbral: real; var pos: entero);
Ambiente
    i: entero;
Proceso
    pos := 0;
    i := 1;
    MIENTRAS (i <= tam) Y (pos = 0) HACER
        SI v[i] > umbral ENTONCES
            pos := i;
        FIN_SI;
        i := i + 1;
    FIN_MIENTRAS;
fin_proc;
```

El 0 sirve como "no encontrado" porque ninguna posición válida del vector es 0.
Se usa MIENTRAS y no PARA porque hay que cortar apenas aparece la primera.

### Detección de racha

```
// Busca longMin lecturas seguidas por encima del umbral. El contador suma 1
// con cada lectura que lo supera y vuelve a 0 apenas una no lo supera.
// Si llega a longMin hay racha, y empezó longMin - 1 lecturas antes.
Procedimiento DetectarRacha(v: ARREGLO[1..N] de real; tam: entero;
                            umbral: real; longMin: entero;
                            var hay: logico; var inicio: entero);
Ambiente
    i, contador: entero;
Proceso
    hay := falso;
    inicio := 0;
    contador := 0;
    i := 1;
    MIENTRAS (i <= tam) Y (NO hay) HACER
        SI v[i] > umbral ENTONCES
            contador := contador + 1;
            SI contador = longMin ENTONCES
                hay := verdadero;
                inicio := i - longMin + 1;
            FIN_SI;
        SINO
            contador := 0;
        FIN_SI;
        i := i + 1;
    FIN_MIENTRAS;
fin_proc;
```

### Prueba con un sensor (sensor 2)

```
sensorElegido := 2;
CargarSensor(sensorElegido, lecturas);
Estadisticas(lecturas, N, maximo, posMax, minimo, posMin, promedio);
BuscarSupera(lecturas, N, UMBRAL, posSupera);
DetectarRacha(lecturas, N, UMBRAL, LONG_MIN, hayRacha, inicioRacha);
```

| Resultado | Valor | Verificación a mano contra el CSV |
|---|---|---|
| Máximo | 59,5 en la lectura 63 | Es un valor de la racha inyectada (61 a 68) |
| Mínimo | 18,7 en la lectura 2 | 00:10, de madrugada: tiene sentido |
| Promedio | 24,15 °C | Algo alto para un sensor a la sombra: las 8 lecturas de la racha lo inflan |
| Primera lectura sobre 40 °C | 61 | La lectura 60 vale 22,5 y la 61 vale 54,0 |
| Racha de 5 o más | Sí, desde la 61 | Coincide con la verdad conocida |

---

## Parte 3 — Matriz: extracción y reutilización

```
matriz: ARREGLO[1..M, 1..N] de real;
fila: ARREGLO[1..N] de real;
promedioPorSensor: ARREGLO[1..M] de real;
```

### Carga de la matriz

```
// Un solo recorrido: cada registro ya trae su fila (sensor) y su columna (nro).
Procedimiento CargarMatriz(var mat: ARREGLO[1..M, 1..N] de real);
Ambiente
    reg: lectura;
Proceso
    ABRIR E(archLecturas);
    LEER(archLecturas, reg);
    MIENTRAS NFDA(archLecturas) HACER
        mat[reg.sensor, reg.nro] := reg.valor;
        LEER(archLecturas, reg);
    FIN_MIENTRAS;
    CERRAR(archLecturas);
fin_proc;
```

### Extracción de fila

```
// Copia la fila de un sensor a un vector, para tratarlo con el kit de la Parte 2.
Procedimiento ExtraerFila(mat: ARREGLO[1..M, 1..N] de real;
                          fila: entero; var v: ARREGLO[1..N] de real);
Ambiente
    j: entero;
Proceso
    PARA j := 1 HASTA N HACER
        v[j] := mat[fila, j];
    FIN_PARA;
fin_proc;
```

### Reutilización del kit, vector de promedios y sensor máximo

```
CargarMatriz(matriz);
PARA s := 1 HASTA M HACER
    ExtraerFila(matriz, s, fila);
    Estadisticas(fila, N, maximo, posMax, minimo, posMin, promedio);
    promedioPorSensor[s] := promedio;
    DetectarRacha(fila, N, UMBRAL, LONG_MIN, hayRacha, inicioRacha);
    // se informan los resultados del sensor s
FIN_PARA;

// el mismo Estadisticas sobre el vector de promedios: la posición del máximo
// es directamente el número de sensor
Estadisticas(promedioPorSensor, M, maximo, posMax, minimo, posMin, promedio);
```

La Parte 3 no tiene lógica de análisis propia. Solo carga la matriz, saca filas y
llama a `Estadisticas` y `DetectarRacha` **sin modificarlos**. La única diferencia
entre analizar un sensor y analizar los promedios es el valor de `tam`: N en un
caso y M en el otro.

### Resultados

| Sensor | Máximo (posición) | Mínimo (posición) | Promedio | ¿Racha? |
|---|---|---|---|---|
| 1 | 29,3 (92) | 18,3 (28) | 22,96 | No |
| 2 | 59,5 (63) | 18,7 (2) | 24,15 | Sí, desde la 61 |
| 3 | 33,7 (88) | 17,7 (22) | **25,22** | No |
| 4 | 58,4 (97) | 19,3 (14) | 25,07 | Sí, desde la 97 |
| 5 | 53,9 (32) | 18,3 (30) | 22,73 | No |

`promedioPorSensor = [22,96; 24,15; 25,22; 25,07; 22,73]`

**Sensor con mayor promedio: el 3** (25,22 °C). No es el más caluroso: es el
descalibrado, y la deriva de +4,3 °C a lo largo del día sube su promedio. Los
sensores 2 y 4 también tienen el promedio inflado, en su caso por las rachas de
falla. El promedio solo no distingue un lugar más caluroso de un sensor que mide mal.

Las estadísticas del sensor 2 dan igual en la Parte 2 (carga directa desde el
archivo) y en la Parte 3 (matriz y extracción de fila). Esto confirma que la
extracción de fila y la reutilización no cambian los datos.

---

## Parte 4 — Validación

Parámetros de detección: **UMBRAL = 40 °C**, **LONG_MIN = 5** lecturas.

| Sensor | Inyectado (inicio, longitud) | Detectado | Resultado |
|---|---|---|---|
| 1 | — | — | Correcto: no había y no detectó |
| 2 | 61, 8 | Desde la 61 | **Acierto** |
| 3 | — | — | Correcto: no había y no detectó |
| 4 | 97, 6 | Desde la 97 | **Acierto** |
| 5 | 31, 3 | — | **Falso negativo** |

- **Aciertos: 2 de 3.** En los dos casos la posición de inicio detectada coincide
  exactamente con la inyectada.
- **Falsos negativos: 1 (sensor 5).** La racha tiene 3 lecturas y el algoritmo
  pide 5 seguidas: el contador llega a 3 y vuelve a 0 con la lectura 34. No es un
  error del algoritmo, es la longitud mínima elegida. `BuscarSupera` sí la
  encuentra (primera lectura sobre 40 °C: la 31), así que la falla queda a la
  vista aunque no cuente como racha. Bajar LONG_MIN a 3 la detectaría, a cambio de
  marcar como racha fallas más cortas, como un pico aislado de 2 o 3 lecturas.
- **Falsos positivos: 0.** El valor normal más alto de todo el dataset es 33,7 °C
  (sensor 3, por la deriva), lejos de 40 °C. Con un umbral más bajo, por ejemplo
  31 °C, la deriva del sensor 3 ya daría un falso positivo a la tarde.
- **Limitación conocida:** `DetectarRacha` informa la primera racha de cada sensor.
  Como inyectamos una sola por sensor, eso no afecta la validación; con dos rachas
  en el mismo sensor, la segunda no se reportaría.

---

## Reflexión

Investigar antes de programar me sirvió para elegir los valores con fundamento: el umbral de 40 °C salió de comparar las temperaturas normales de Resistencia con la desviación estándar de mis datos, y el N de 144 lecturas, de la frecuencia de muestreo. Escribir la solución en pseudocódigo me ayudó a entender mejor la secuencia de cómo se tiene que ejecutar y cómo pensar la solución paso a paso. Reutilizar el kit de vector en la matriz, extrayendo cada fila, me pareció una buena idea porque evita reprocesar la información y ahorra tiempo y esfuerzo en el código: la Parte 3 no necesitó lógica de análisis nueva. En la detección, el algoritmo encontró las dos rachas largas en la posición exacta, pero no la del sensor 5, que era más corta que la longitud mínima; para ese caso adoptaría un margen mínimo de desviación, para que esas mediciones entren pero marcadas con una bandera distinta. Por último, que el sensor con mayor promedio fuera el descalibrado me mostró que el promedio solo no alcanza: también hay que mirar cómo se comporta cada sensor en el tiempo, porque una deriva se nota en que la diferencia con los demás va creciendo.

---

## Anexo — Archivos

- `generar_lecturas.py`: script de generación de datos.
- `lecturas.csv`: dataset (720 lecturas).
- `verdad_conocida.csv`: rachas inyectadas.
- `estacion.frre`: el pseudocódigo completo (Partes 2 y 3 en un solo programa).
