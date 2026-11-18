# Integrante 3 — Simulación Dinámica, Caja Negra y Telemetría (Punto D)

**Proyecto:** Simulador Artemis (Situación 4) · **Lenguaje:** C99 **Documento general (leer primero):** 00_DOCUMENTO_GENERAL.md

## 0. Tu misión en una frase

Programar el **ciclo de simulación paso a paso (1 segundo por vuelta)** que "hace caer" la cápsula y va guardando en la **caja negra** (un arreglo) el tiempo, la altitud, la velocidad y las fuerzas G; decidir si el **ángulo de reingreso** es seguro (Punto D) y **mostrar la telemetría** con el pico máximo de G.

Es la parte **más compleja** del proyecto: usa bucles, arreglos de estructuras, punteros y funciones matemáticas. Leé este documento con calma y avanzá función por función.

## 1. Qué tenés que entregar

| **#** | **Función** | **Archivo** | **Responde** | **Retorna** |
|---|---|---|---|---|
| 1 | `ejecutar_simulacion_dinamica` | `simulador.c` (**sección ROL 3**) | Pregunta **D** + llena la caja negra | `int` (cantidad de filas cargadas) |
| 2 | `mostrar_telemetria` | `simulador.c` | imprime D, tabla y pico G | nada (`void`) |
| 3 | `mostrar_reporte_completo` | `simulador.c` | arma el reporte entero | nada (`void`) |
| 4 | Programa de prueba | `pruebas/test_rol3.c` | — | — |
| 5 | Sección "Modelo de simulación y limitaciones" del `README.md` | `README.md` | — | — |

**No tocás:** `main.c`, `simulador.h`, `validaciones.*`, ni las secciones ROL 1 y ROL 2.

**Lo que necesitás de los demás:**

- Tu `mostrar_reporte_completo` llama a `mostrar_resultados_analiticos` (**Integrante 2**). Mientras no la tenga hecha, el esqueleto tiene una versión vacía: tu código compila igual.

- Para probar **no necesitás** al Integrante 1 ni al 4: llenás la estructura `entradas` a mano.

## 2. Conceptos que necesitás (explicados desde cero)

### 2.1 El modelo físico (simplificado)

La cápsula cae atravesando la atmósfera siguiendo una **línea recta** con ángulo γ respecto del horizonte. Cada segundo (`dt = 1`):

1. **Densidad del aire** a la altura actual `h` (decae exponencialmente al subir): `rho = DENSIDAD_BASE * exp(-h / CONSTANTE_ALTURA)` (a 120 km casi no hay aire; a nivel del mar, 1,225 kg/m³).

2. **Desaceleración por arrastre** (resistencia del aire): `a_inst = (0.5 * rho * v * v * COEF_ARRASTRE_AREA) / masa`

3. **Fuerzas G** (cuántas veces la gravedad): `fuerzas_g = a_inst / GRAVEDAD`

4. **Actualizar velocidad:** `v = v - a_inst * dt`

5. **Actualizar altitud:** la cápsula avanza `v` por segundo, pero solo la componente **vertical** hace perder altura: `h = h - v * sin(rad) * dt`

6. Avanzar el reloj: `t = t + dt`.

Este método (recalcular "un pasito" por vez) se llama **integración numérica** (método de Euler). No hace falta saber más.

### 2.2 Ángulo en grados vs. radianes

La función `sin()` de C trabaja en **radianes**, pero el usuario ingresa **grados**. Conversión: `rad = grados * PI / 180.0`

### 2.3 Punto D: las 3 posibles "ventanas"

| **Ángulo γ** | **Qué pasa físicamente** | `estado_mision` | **Constante** |
|---|---|---|---|
| γ < **5,5°** | Muy tangencial: la cápsula "rebota" en la atmósfera como una piedra en el agua y vuelve al espacio | `3` | `ESTADO_REBOTE` |
| γ > **7,0°** | Muy empinado: desaceleración excesiva (G gigantes) y calentamiento extremo: la nave se destruye | `2` | `ESTADO_DESINTEGRACION` |
| 5,5° ≤ γ ≤ 7,0° | Reingreso seguro | `1` | `ESTADO_NOMINAL` |

Las constantes `VENTANA_ANGULO_MIN` (5.5) y `VENTANA_ANGULO_MAX` (7.0) están en `simulador.h`.

### 2.4 Arreglos de estructuras (la "caja negra")

`main` declara `instante_vuelo caja_negra[LIMITE_ARREGLO];` = **1000 filas**, cada fila con 4 `double`: `t_actual`, `h_actual`, `v_actual`, `fuerzas_g`.

Cuando un arreglo se pasa a una función, **llega como puntero a su primer elemento** (`instante_vuelo *caja_negra`). Aun así, se usa con corchetes como si fuera arreglo:

```c
caja_negra[pasos].t_actual = t;     // fila número "pasos", campo t_actual
```

Fijate: con `[ ]` se usa el **punto** (`.`), porque `caja_negra[pasos]` ya es una estructura (no un puntero). Con el puntero `res` se usa la **flecha** (`res->estado_mision`).

**Los índices van de 0 a 999.** Escribir en `caja_negra[1000]` rompe la memoria. Por eso el bucle chequea `pasos < LIMITE_ARREGLO`.

### 2.5 Funciones matemáticas

Hay que tener `#include <math.h>` (ya está en el esqueleto) y compilar con `-lm` al final:

- `exp(x)` → eˣ

- `sin(x)` → seno (x en **radianes**)

### 2.6 Cadenas de texto en C: snprintf

`res->mensaje_falla` es un `char[100]` (**máximo 99 letras + el terminador**). Para copiar un texto ahí **de forma segura**:

```c
snprintf(res->mensaje_falla, sizeof(res->mensaje_falla), "texto...");
```

`snprintf` **corta** el texto si es muy largo (en cambio `strcpy` desbordaría la memoria). No uses tildes ni `ñ`.

### 2.7 Bucle while con varias condiciones y break

`while (A && B && C)` repite mientras **todas** sean verdaderas. `break;` sale del bucle de inmediato.

### 2.8 Valor de retorno int

`return pasos;` entrega al `main` cuántas filas llenaste. Esa cantidad se usa luego para recorrer el arreglo **solo hasta donde hay datos válidos** (el resto contiene basura).

## 3. Preparación

1. `git clone <URL>` y `cd` a la carpeta.

2. `git checkout -b feature/rol3-simulacion`

3. Compilá el esqueleto: `make`.

4. En `simulador.c`, ubicá el cartel `ROL 3 - Simulacion dinamica y telemetria (Punto D)`. **Solo escribís ahí.**

## 4. Paso a paso por función

### 4.1 ejecutar_simulacion_dinamica

|  |  |
|---|---|
| **Firma** | `int ejecutar_simulacion_dinamica(const entradas *mision, instante_vuelo *caja_negra, resultados *res)` |
| **Entradas** | `mision`: datos (solo lectura) · `caja_negra`: arreglo donde guardás filas · `res`: registro donde escribís `estado_mision` y `mensaje_falla` |
| **Retorna** | `int`: cantidad exacta de filas cargadas en `caja_negra` |
| **Campos que lee de** `mision` | `angulo_reingreso`, `h_inicial`, `v_inicial`, `h_paracaidas`, `v_paracaidas`, `masa` |
| **Campos que escribe en** `res` | `estado_mision`, `mensaje_falla` (**solo esos dos**) |

#### Parte 1 — Variables locales

1. `double rad = mision->angulo_reingreso * PI / 180.0;` (ángulo en radianes)

2. `double t = 0.0;` (tiempo)

3. `double dt = 1.0;` (paso: 1 segundo)

4. `double h = mision->h_inicial;` (altitud actual)

5. `double v = mision->v_inicial;` (velocidad actual)

6. `double rho;` y `double a_inst;` (se calculan en cada vuelta)

7. `int pasos = 0;` (contador = próxima fila libre del arreglo)

8. `int rebotando = 0;` (bandera: 0 = descenso normal, 1 = ya está subiendo por rebote)

#### Parte 2 — Evaluar el ángulo (Punto D)

Con `if / else if / else`:

1. Si `mision->angulo_reingreso < VENTANA_ANGULO_MIN` → `res->estado_mision = ESTADO_REBOTE;` y copiar con `snprintf` el mensaje de rebote.

2. Si no, si `mision->angulo_reingreso > VENTANA_ANGULO_MAX` → `res->estado_mision = ESTADO_DESINTEGRACION;` y mensaje de desintegración.

3. Si no → `res->estado_mision = ESTADO_NOMINAL;` y mensaje de éxito.

Mensajes sugeridos (< 99 caracteres, sin tildes):

- `REBOTE ATMOSFERICO: angulo menor a 5.5 grados, la capsula rebota al espacio.`

- `DESINTEGRACION: angulo mayor a 7.0 grados, G excesivas y sobrecarga termica.`

- `MISION EXITOSA: reingreso dentro de la ventana segura (5.5 a 7.0 grados).`

#### Parte 3 — Ciclo de integración

Escribir un `while` con **3 condiciones** (todas con `&&`):

```text
while (h > mision->h_paracaidas && v > mision->v_paracaidas && pasos < LIMITE_ARREGLO)
```

Es decir: "mientras no se haya llegado a la altura de los paracaídas, ni bajado de la velocidad de los paracaídas, ni llenado el arreglo".

Dentro de cada vuelta, **en este orden exacto**:

| **#** | **Instrucción** | **Para qué** |
|---|---|---|
| 1 | Si `res->estado_mision == ESTADO_REBOTE` **y** `pasos >= PASOS_TOTAL_REBOTE` → `break;` | En un rebote, cortar la simulación a los 60 pasos |
| 2 | `rho = DENSIDAD_BASE * exp(-h / CONSTANTE_ALTURA);` | densidad del aire a la altura actual |
| 3 | `a_inst = (0.5 * rho * v * v * COEF_ARRASTRE_AREA) / mision->masa;` | desaceleración por arrastre |
| 4 | Guardar la fila: `caja_negra[pasos].t_actual = t;` `.h_actual = h;` `.v_actual = v;` `.fuerzas_g = a_inst / GRAVEDAD;` | **registrar el estado ANTES de actualizarlo** |
| 5 | Si `res->estado_mision == ESTADO_REBOTE` **y** `pasos >= PASOS_ANTES_REBOTE` → `rebotando = 1;` | a partir del paso 30, empieza a subir |
| 6 | `v = v - a_inst * dt;` | actualizar velocidad |
| 7 | Si `v < mision->v_paracaidas` → `v = mision->v_paracaidas;` | la velocidad no puede quedar por debajo del mínimo |
| 8 | Si `rebotando` → `h = h + v * sin(rad) * dt;` **si no** → `h = h - v * sin(rad) * dt;` | la altitud sube (rebote) o baja (normal) |
| 9 | `t = t + dt;` | avanzar el reloj |
| 10 | `pasos++;` | próxima fila |

Al terminar el `while`: `return pasos;`.

**Por qué el rebote cambió respecto al otro documento:** allá el `break` ocurría inmediatamente después de subir `h`, y esa altitud nueva **nunca se guardaba** en la tabla; el rebote no se veía. Acá se registran 30 pasos de bajada y 30 de subida (60 filas) y se ve el "arco".

#### Código completo

```c
int ejecutar_simulacion_dinamica(const entradas *mision, instante_vuelo *caja_negra, resultados *res)
{
    double rad = mision->angulo_reingreso * PI / 180.0;
    double t = 0.0;
    double dt = 1.0;
    double h = mision->h_inicial;
    double v = mision->v_inicial;
    double rho;
    double a_inst;
    int pasos = 0;
    int rebotando = 0;

    /* --- Punto D: evaluar la ventana del angulo de reingreso --- */
    if (mision->angulo_reingreso < VENTANA_ANGULO_MIN) {
        res->estado_mision = ESTADO_REBOTE;
        snprintf(res->mensaje_falla, sizeof(res->mensaje_falla),
                 "REBOTE ATMOSFERICO: angulo menor a 5.5 grados, la capsula rebota al espacio.");
    } else if (mision->angulo_reingreso > VENTANA_ANGULO_MAX) {
        res->estado_mision = ESTADO_DESINTEGRACION;
        snprintf(res->mensaje_falla, sizeof(res->mensaje_falla),
                 "DESINTEGRACION: angulo mayor a 7.0 grados, G excesivas y sobrecarga termica.");
    } else {
        res->estado_mision = ESTADO_NOMINAL;
        snprintf(res->mensaje_falla, sizeof(res->mensaje_falla),
                 "MISION EXITOSA: reingreso dentro de la ventana segura (5.5 a 7.0 grados).");
    }

    /* --- Ciclo de integracion paso a paso --- */
    while (h > mision->h_paracaidas && v > mision->v_paracaidas && pasos < LIMITE_ARREGLO) {

        if (res->estado_mision == ESTADO_REBOTE && pasos >= PASOS_TOTAL_REBOTE) {
            break;
        }

        rho = DENSIDAD_BASE * exp(-h / CONSTANTE_ALTURA);
        a_inst = (0.5 * rho * v * v * COEF_ARRASTRE_AREA) / mision->masa;

        caja_negra[pasos].t_actual = t;
        caja_negra[pasos].h_actual = h;
        caja_negra[pasos].v_actual = v;
        caja_negra[pasos].fuerzas_g = a_inst / GRAVEDAD;

        if (res->estado_mision == ESTADO_REBOTE && pasos >= PASOS_ANTES_REBOTE) {
            rebotando = 1;
        }

        v = v - a_inst * dt;
        if (v < mision->v_paracaidas) {
            v = mision->v_paracaidas;
        }

        if (rebotando) {
            h = h + v * sin(rad) * dt;
        } else {
            h = h - v * sin(rad) * dt;
        }

        t = t + dt;
        pasos++;
    }

    return pasos;
}
```

#### Seguimiento a mano de las primeras vueltas (datos oficiales, 6,2°)

```text
sin(6,2°) = 0,10800
```

| **Vuelta (**`pasos`**)** | `h` **al empezar** | `v` **al empezar** | `rho` | `a_inst` | **Fila guardada (**`fuerzas_g`**)** |
|---|---|---|---|---|---|
| 0 | 120 000,00 | 11 000,0000 | 9,0557e-07 | 0,079019 | 0,008063 |
| 1 | 118 812,02 | 10 999,9210 | 1,0414e-06 | 0,090871 | 0,009273 |
| 2 | 117 624,04 | 10 999,8301 | 1,1976e-06 | 0,104500 | 0,010663 |

Si tu código reproduce esos números en el programa de prueba, vas por el buen camino.

### 4.2 mostrar_telemetria

|  |  |
|---|---|
| **Firma** | `void mostrar_telemetria(const resultados *res, const instante_vuelo *caja_negra, int cantidad_pasos)` |
| **Entradas** | `res` (para `mensaje_falla`), `caja_negra` (la tabla), `cantidad_pasos` (filas válidas) |
| **Retorna** | nada (imprime) |

**Pasos:**

1. Declarar `int i;` · `int indice_pico = 0;` (posición de la fila con más G) · `int salto;` (de a cuántas filas se imprime).

2. Imprimir el subtítulo `PUNTO D: Analisis del angulo de reingreso` y debajo `res->mensaje_falla` con `%s`.

3. **Protección:** si `cantidad_pasos <= 0` → imprimir "No hay datos de telemetria" y `return;` (sale de la función).

4. Calcular `salto = cantidad_pasos / FILAS_TABLA;` y si `salto < 1` → `salto = 1;` (así la tabla muestra ~20 filas aunque haya 739).

5. Imprimir el encabezado de la tabla: **Tiempo (s) | Altitud (m) | Velocidad (m/s) | Fuerzas G**.

6. Un `for (i = 0; i < cantidad_pasos; i++)` que recorre **todas las filas válidas** y en cada vuelta:

1. **Busca el pico:** si `caja_negra[i].fuerzas_g > caja_negra[indice_pico].fuerzas_g` → `indice_pico = i;`

2. **Imprime la fila** solo si `i % salto == 0` **o** si es la última (`i == cantidad_pasos - 1`). (`%` es el resto de la división: `i % 36 == 0` es verdadero en 0, 36, 72, …)

7. Terminado el `for`, imprimir el **pico máximo de G**, su altitud y su instante, usando `caja_negra[indice_pico]`.

La búsqueda del pico recorre **todas** las filas (no solo las impresas), por eso el pico mostrado (29,36 g) puede ser mayor que las filas de la tabla.

```c
void mostrar_telemetria(const resultados *res, const instante_vuelo *caja_negra, int cantidad_pasos)
{
    int i;
    int indice_pico = 0;
    int salto;

    printf("\n--- PUNTO D: Analisis del angulo de reingreso ---\n");
    printf("  %s\n", res->mensaje_falla);

    if (cantidad_pasos <= 0) {
        printf("\n  (No hay datos de telemetria registrados)\n");
        return;
    }

    salto = cantidad_pasos / FILAS_TABLA;
    if (salto < 1) {
        salto = 1;
    }

    printf("\n--- CAJA NEGRA: TELEMETRIA ---\n");
    printf("  %10s | %14s | %15s | %10s\n", "Tiempo (s)", "Altitud (m)", "Velocidad (m/s)", "Fuerzas G");
    printf("  -----------+----------------+-----------------+-----------\n");

    for (i = 0; i < cantidad_pasos; i++) {
        if (caja_negra[i].fuerzas_g > caja_negra[indice_pico].fuerzas_g) {
            indice_pico = i;
        }
        if (i % salto == 0 || i == cantidad_pasos - 1) {
            printf("  %10.1f | %14.1f | %15.2f | %10.2f\n",
                   caja_negra[i].t_actual, caja_negra[i].h_actual,
                   caja_negra[i].v_actual, caja_negra[i].fuerzas_g);
        }
    }

    printf("\n  Pico maximo de fuerzas G: %.2f g a %.1f m de altitud (t = %.1f s)\n",
           caja_negra[indice_pico].fuerzas_g, caja_negra[indice_pico].h_actual,
           caja_negra[indice_pico].t_actual);
}
```

(`%10s` = texto alineado a la derecha en 10 columnas; `%14.1f` = decimal con 1 cifra en 14 columnas. Sirven para que la tabla quede alineada.)

### 4.3 mostrar_reporte_completo

|  |  |
|---|---|
| **Firma** | `void mostrar_reporte_completo(const entradas *mision, const resultados *res, const instante_vuelo *caja_negra, int cantidad_pasos)` |
| **Entradas** | las 4 cosas que necesitan A, B, C y D |
| **Retorna** | nada |

Es un **coordinador**: arma el marco y delega.

**Pasos:**

1. Imprimir un encabezado con líneas de `=` y el título **REPORTE DE MISION ARTEMIS - REINGRESO**.

2. Llamar a `mostrar_resultados_analiticos(mision, res);` (del Integrante 2: Puntos A, B, C).

3. Llamar a `mostrar_telemetria(res, caja_negra, cantidad_pasos);` (tuya: Punto D, tabla y pico).

4. Imprimir una línea de cierre.

```c
void mostrar_reporte_completo(const entradas *mision, const resultados *res, const instante_vuelo *caja_negra, int cantidad_pasos)
{
    printf("\n==============================================\n");
    printf("   REPORTE DE MISION ARTEMIS - REINGRESO\n");
    printf("==============================================\n");
    mostrar_resultados_analiticos(mision, res);
    mostrar_telemetria(res, caja_negra, cantidad_pasos);
    printf("\n==============================================\n");
}
```

## 5. Cómo probar tu parte (sin esperar a nadie)

Creá `pruebas/test_rol3.c`:

```c
#include <stdio.h>
#include "simulador.h"

static void probar(const char *titulo, double angulo)
{
    entradas m = {10400.0, 120000.0, 11000.0, 0.0, 400.0, 2500.0, 25.0, 8.0, 1.50};
    instante_vuelo caja[LIMITE_ARREGLO];
    resultados res;
    int pasos;

    m.angulo_reingreso = angulo;
    pasos = ejecutar_simulacion_dinamica(&m, caja, &res);

    printf("=== %s (angulo %.1f) ===\n", titulo, angulo);
    printf("  pasos  = %d\n", pasos);
    printf("  estado = %d\n", res.estado_mision);
    printf("  msg    = %s\n", res.mensaje_falla);
    printf("  fila 0 : t=%.1f h=%.1f v=%.2f g=%.4f\n", caja[0].t_actual, caja[0].h_actual, caja[0].v_actual, caja[0].fuerzas_g);
    printf("  ultima : t=%.1f h=%.1f v=%.2f g=%.4f\n", caja[pasos-1].t_actual, caja[pasos-1].h_actual, caja[pasos-1].v_actual, caja[pasos-1].fuerzas_g);
    mostrar_telemetria(&res, caja, pasos);
}

int main(void)
{
    probar("NOMINAL", 6.2);
    probar("REBOTE", 5.0);
    probar("DESINTEGRACION", 10.0);
    return 0;
}

gcc -Wall -Wextra -std=c99 -pedantic -I. pruebas/test_rol3.c simulador.c validaciones.c -o test_rol3 -lm
./test_rol3
```

### Resultados esperados

| **Caso** | `pasos` | `estado` | **Fila 0** | **Última fila** | **Pico G** |
|---|---|---|---|---|---|
| **6,2°** (nominal) | **739** | `1` | t=0,0 · h=120000,0 · v=11000,00 · g=0,0081 | t=738,0 · h=20892,6 · v=25,01 | **29,36 g** a 41837,4 m (t = 70,0 s) |
| **5,0°** (rebote) | **60** | `3` | igual | t=59,0 · h=118967,7 · v=10960,28 | 0,24 g a 91252,3 m (t = 30,0 s) |
| **10°** (desintegración) | **467** | `2` | igual | t=466,0 · h=16970,6 · v=25,02 | **47,71 g** a 38580,7 m (t = 45,0 s) |

Mensajes esperados: `MISION EXITOSA: ...` / `REBOTE ATMOSFERICO: ...` / `DESINTEGRACION: ...`.

**Cómo comprobar que el comportamiento físico tiene sentido:**

- En el caso nominal, las G suben hasta ~29 g y luego bajan (la cápsula ya perdió velocidad).

- En el **rebote**, la altitud **baja** hasta ≈91 252 m y **después sube** (filas con t = 33, 36, … muestran altitudes mayores).

- En la **desintegración**, el pico de G es **mayor** que en el nominal (47,7 vs 29,4): ángulo más empinado ⇒ más G.

Tabla esperada (caso nominal, primeras filas impresas):

```text
  Tiempo (s) |    Altitud (m) | Velocidad (m/s) |  Fuerzas G
  -----------+----------------+-----------------+-----------
         0.0 |       120000.0 |        11000.00 |       0.01
        36.0 |        77296.2 |        10920.65 |       1.21
        72.0 |        40486.2 |         6112.82 |      28.76
       108.0 |        29581.9 |         1200.94 |       4.00
       ...
```

## 6. Errores frecuentes

| **Síntoma** | **Causa** | **Solución** |
|---|---|---|
| `undefined reference to 'exp'` / `'sin'` | Falta `-lm` | Poné `-lm` **al final** del comando `gcc` |
| Seno da valores raros | Pasaste grados a `sin()` | Convertí a radianes con `PI / 180.0` |
| Segmentation fault | Escribiste fuera del arreglo (`pasos >= 1000`) | Mantené `pasos < LIMITE_ARREGLO` en el `while` |
| Bucle infinito | Olvidaste `pasos++` o `t = t + dt` | Revisá los pasos 9 y 10 |
| La simulación termina en 0 pasos | Pusiste `<` en vez de `>` en el `while` | `h > h_paracaidas` y `v > v_paracaidas` |
| Texto del mensaje cortado | El mensaje supera 99 caracteres | Acortalo; `snprintf` lo recorta por seguridad |
| Error `request for member 't_actual' in something not a structure` | Usaste `->` con corchetes | `caja_negra[pasos].t_actual` (punto) |
| `error: 'res' is a pointer; did you mean to use '->'?` | Escribiste `res.estado_mision` | `res->estado_mision` |
| Imprime filas con basura | Recorriste hasta 1000 en vez de `cantidad_pasos` | El `for` va hasta `i < cantidad_pasos` |
| El pico G siempre es la fila 0 | `indice_pico` mal actualizado | Debe comparar con `>` y asignar `indice_pico = i;` |
| La tabla no se ve alineada | Falta ancho en los `%` | Usá `%10.1f`, `%14.1f`, `%15.2f`, `%10.2f` |
| Rebote no se ve en la tabla | `break` demasiado pronto | Respetá `PASOS_TOTAL_REBOTE` (60), no 30 |

## 7. Sección del README que redactás

Título: **"Modelo de simulación, estados de la misión y limitaciones"**. Incluí:

1. Las 6 ecuaciones del ciclo (sección 2.1) y el significado de `dt = 1 s`.

2. La tabla de ventanas de ángulo (sección 2.3) y qué se muestra en cada caso.

3. Explicación de la caja negra (arreglo de `instante_vuelo` de 1000 posiciones) y el pico de G.

4. Las **limitaciones** (ver sección 11 del documento general): modelo balístico sin sustentación, ángulo constante, Euler con paso de 1 s, el ciclo no coincide exactamente con los Puntos A y B porque son modelos distintos, límite de 1000 filas.

## 8. Checklist y commits sugeridos

- [ ] `ejecutar_simulacion_dinamica` devuelve 739 / 60 / 467 pasos en los 3 casos de prueba

- [ ] Estados correctos (1, 3, 2) y mensajes cargados con `snprintf`

- [ ] Ninguna escritura fuera del arreglo (`pasos < LIMITE_ARREGLO`)

- [ ] `mostrar_telemetria` imprime ~20 filas, la última fila y el pico de G correcto

- [ ] `mostrar_reporte_completo` llama a `mostrar_resultados_analiticos` y a `mostrar_telemetria`

- [ ] Constantes usadas en lugar de números mágicos (`ESTADO_*`, `PASOS_*`, `FILAS_TABLA`, etc.)

- [ ] Sin warnings con `-Wall -Wextra -std=c99 -pedantic`

- [ ] Cada función comentada

- [ ] `pruebas/test_rol3.c` agregado

- [ ] Sección del README redactada

- [ ] Pull Request abierto hacia `main`

```text
Rol3: evalua ventana de angulo y carga estado_mision en ejecutar_simulacion_dinamica
Rol3: agrega ciclo de integracion y llenado de la caja negra
Rol3: agrega logica de rebote atmosferico
Rol3: implementa mostrar_telemetria con busqueda de pico de G
Rol3: implementa mostrar_reporte_completo
Rol3: agrega programa de prueba test_rol3 y seccion de README
```

## 9. Preguntas de práctica para el coloquio

1. ¿Por qué se convierte el ángulo a radianes?

2. ¿Qué hace cada una de las 3 condiciones del `while`? ¿Qué pasa si saco `pasos < LIMITE_ARREGLO`?

3. ¿Por qué la fila se guarda **antes** de actualizar `v` y `h`?

4. ¿Por qué `caja_negra[pasos].t_actual` usa punto y `res->estado_mision` usa flecha?

5. ¿Qué devuelve la función y por qué es importante que devuelva `pasos`?

6. ¿Por qué se usa `snprintf` en vez de `strcpy`? ¿Qué es un desbordamiento de buffer?

7. ¿Por qué el pico de G es mayor con ángulos más empinados?

8. ¿Cómo se simula el rebote? ¿Qué es la bandera `rebotando`?

9. ¿Qué es la integración de Euler? ¿Qué error introduce `dt = 1`?

10. ¿Por qué la simulación termina a ≈20,9 km y no a 2,5 km? (Respuesta: el modelo solo tiene arrastre —sin gravedad en la ecuación de velocidad—, y la velocidad cae a 25 m/s antes de bajar a 2,5 km; ver limitaciones.)

11. ¿Qué significa `i % salto == 0`?

12. ¿Por qué el arreglo se declara en `main` y no acá?
