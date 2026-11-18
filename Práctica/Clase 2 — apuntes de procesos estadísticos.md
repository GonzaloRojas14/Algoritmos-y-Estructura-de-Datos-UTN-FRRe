---
tipo: apuntes
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
clase: 2
origen: Clase 2 despues de la organizacion
tags:
  - AED
  - practica
  - arreglos
  - archivos
  - procesos-estadisticos
  - InProgress
---

# Clase 2 — apuntes de procesos estadísticos

> [!abstract] Qué es esta nota
> Tus apuntes de la segunda clase después de la reorganización: el algoritmo `ESTAD`, un **proceso estadístico** clásico (archivo de ventas → matriz de sucursales × rubros). El apunte crudo venía de una captura de pantalla compartida, así que traía **ruido de OCR** además de las erratas propias.
>
> Acá está el código reconstruido, contrastado contra [[6 — Procesos Estadísticos]] y [[SKILL — pseudocodigo-utn|la notación de cátedra]].

[[💻 Algoritmos — Índice|← Materia]] · [[6 — Procesos Estadísticos|Filminas de la cátedra sobre este tema]] · [[Clase 1 — apuntes de arreglos|← Clase anterior]]

---

## 🎯 De qué tema es esta clase

`ESTAD` es un **proceso estadístico**: el tema que combina **archivos + arreglos**, filminas [[6 — Procesos Estadísticos]]. Entra en el segundo parcial junto con corte de control y actualización (lo anotaste en [[Clase 1 — apuntes de arreglos#🎯 Alcance del segundo parcial|la clase 1]]).

Los 7 pasos de la metodología (filmina 7) mapeados sobre este algoritmo:

| # | Paso de la metodología | Dónde está en `ESTAD` |
|---|---|---|
| 1 | Poner a 0 la matriz | `Poner_Cero_Arreglo` |
| 2 | Iniciar procesamiento del archivo | `ABRIR E/(Arch)` + lectura anticipada |
| 3 | Recuperar datos del registro | `Reg.Suc`, `Reg.Rubro`, `Reg.Cant`, `Reg.Precio_Unitario` |
| 4 | Actualizar la matriz | `A[Reg.Suc, Reg.Rubro] := … + Lin` |
| 5 | Actualizar filas/columnas totalizadoras | las tres líneas de `A[…,8]`, `A[6,…]` y `A[6,8]` |
| 6 | Procesar hasta el final | `MIENTRAS NFDA(Arch)` con el `LEER` al final |
| 7 | Mostrar la matriz e informar | `Mostrar_Arreglo` + `Mostrar_Salida_Solicitada` |

---

## 📐 El dimensionamiento — la parte que se corrige primero

```
A: ARREGLO [1..6, 1..8] de Real
```

- **Filas** → 5 sucursales (`Suc: 1..5`) **+ 1 fila** de totales → la fila **6**
- **Columnas** → 7 rubros (`Rubro: 1..7`) **+ 1 columna** de totales → la columna **8**
- `A[6,8]` → **total general**

✅ Está bien dimensionado. Es exactamente el patrón de la filmina 9: *una fila más, una columna más, y la intersección es el total general*.

| | Rubro 1 | Rubro 2 | … | Rubro 7 | **Total x Suc (col 8)** |
|---|---|---|---|---|---|
| **Suc 1** | | | | | |
| **Suc 2** | | | | | |
| ⋮ | | | | | |
| **Suc 5** | | | | | |
| **Total x Rubro (fila 6)** | | | | | **`A[6,8]`** |

> [!tip] La cuenta del parcial
> Sucursales + 1, rubros + 1. Si la consigna dice "5 sucursales y 7 rubros", la matriz **nunca** es `[1..5, 1..7]`. Mismo error que evita la pista de dimensionamiento de las filminas 12 y 13.

---

## 📄 Lo que quedó en el apunte

Tal cual salió de la captura, con el ruido incluido:

```
Accion ESTAD ES;
    Ambiente
        Venta = Registro
            Id: N(9); Cod_Prod: N(6) ;
            Fecha_Venta = Registro
                Dia:1..31; Mes:1..12; Anio:N(4);
            Fin Regi
            Suc: 1..5;
            ant: Reali
            Rubro: 1..7;
            Precio_Unitario: Real;
        Fin_Reg:
        Arch: archivo de Venta ordenado por Id;
        Reg: Venta;
        A: ARREGLO [1..6, 1..8] de Real;
        Lin: Real;

    Proceso
        Abrir E (Arch) ;
        Leer (Arch, Reg) ;
        Poner_Cero Arreglo;
        Mientras No FDA (Arch) hacer
            Lin := Reg.Cant * Reg.Precio_Unitario;
            A[Reg. Suc, Reg.Rubro] := A[Reg. Suc, Reg.Rubro] + Lin;
            ALReg. Suc, 8]  := A[Reg. Suc, 8]  + Lin;
            A[6, Reg. Rubro] := A[6, Reg. Rubro] + Lin;
            A[6, 8]          :- A[6, 8]         + Lin;
            Leer (Arch, Reg) ;
        Fin_Mientras;
        Mostrar_Arreglo;
        Mostrar_Salida Solicitada;
        Cerrar (Arch);
```

> [!note] Ruido de OCR, no errores tuyos
> `ant: Reali` → `Cant: Real` · `Fin Regi` → `FIN_REGISTRO` · `ALReg.Suc, 8]` → `A[Reg.Suc, 8]` · `:-` → `:=` · `Mostrar_Salida Solicitada` → `Mostrar_Salida_Solicitada` · los `Reg. Suc` con espacio → `Reg.Suc`.
> También se coló en el medio del código la barra de *"Está compartiendo la pantalla · Dejar de compartir"* — la saqué.

---

## 🐛 Errores reales a corregir

> [!bug] Seis cosas
> 1. **`ACCION ESTAD ES;` con punto y coma.** La cabecera **no lleva** `;`. Va `ACCION ESTAD ES`.
> 2. **Falta `FIN_ACCION`.** El apunte termina en `Cerrar(Arch)`. En la notación de cátedra el bloque `PROCESO` cierra con `FIN_ACCION` — no existe `FIN_PROCESO` (es la misma errata que en [[Clase 1 — apuntes de arreglos#Ejercicio de ejemplo — `ej_3.2`|`ej_3.2`]]).
> 3. **`Fin_Reg:` con dos puntos** y `Fin Regi` sin cerrar. Los registros cierran con `FIN_REGISTRO`, uno por cada `= REGISTRO` abierto. Acá hay **dos** anidados: `Fecha_Venta` adentro de `Venta`.
> 4. **`Abrir E (Arch)`** → la forma de cátedra es **`ABRIR E/(Arch)`** (con la barra). Ver la tabla de verbos en [[SKILL — pseudocodigo-utn]].
> 5. **`Mientras No FDA(Arch)`** → existe el verbo **`NFDA(Arch)`**, que *es* "no fin de archivo". No se escribe `NO FDA`.
> 6. **`Poner_Cero Arreglo`, `Mostrar_Arreglo` y `Mostrar_Salida_Solicitada` no están declarados.** Las subacciones se declaran en el `AMBIENTE`. Y ojo con `Poner_Cero Arreglo`: con el espacio parecen dos cosas; es **un** procedimiento, `Poner_Cero_Arreglo`.

> [!warning] Dos campos declarados que nunca se usan
> `Id`, `Cod_Prod` y todo `Fecha_Venta` se declaran pero el proceso no los toca. **No es un error** — el formato del registro lo da la consigna, no vos. Pero si la consigna pedía algo por mes o por producto, te está faltando un inciso: contá los incisos uno por uno antes de entregar.

> [!info] "ordenado por Id" es una pista falsa
> `Arch: archivo de Venta ordenado por Id` — el orden **no importa** en un proceso estadístico. Ese es justamente el contraste con **corte de control**, que exige el archivo ordenado por la clave de corte. En un proceso estadístico la matriz acumula por índice, así que el archivo puede venir desordenado (las filminas 12 y 13 dicen explícitamente *"archivo desordenado"*).

---

## ✅ Versión corregida

```
ACCION ESTAD ES
    AMBIENTE
        Venta = REGISTRO
            Id: N(9)
            Cod_Prod: N(6)
            Fecha_Venta = REGISTRO
                Dia: 1..31
                Mes: 1..12
                Anio: N(4)
            FIN_REGISTRO
            Suc: 1..5
            Cant: REAL
            Rubro: 1..7
            Precio_Unitario: REAL
        FIN_REGISTRO

        Arch: ARCHIVO DE Venta ORDENADO POR Id
        Reg: Venta
        A: ARREGLO DE [1..6, 1..8] DE REAL
        Lin: REAL
        i, j: ENTERO

        PROCEDIMIENTO Poner_Cero_Arreglo
            PARA i := 1 A 6, 1 HACER
                PARA j := 1 A 8, 1 HACER
                    A[i, j] := 0
                FIN_PARA
            FIN_PARA
        FIN_PROCEDIMIENTO

        PROCEDIMIENTO Mostrar_Arreglo
            PARA i := 1 A 6, 1 HACER
                PARA j := 1 A 8, 1 HACER
                    ESCRIBIR(A[i, j])
                FIN_PARA
            FIN_PARA
        FIN_PROCEDIMIENTO

    PROCESO
        Poner_Cero_Arreglo

        ABRIR E/(Arch)
        LEER(Arch, Reg)

        MIENTRAS NFDA(Arch) HACER
            Lin := Reg.Cant * Reg.Precio_Unitario

            # celda del cruce sucursal-rubro
            A[Reg.Suc, Reg.Rubro] := A[Reg.Suc, Reg.Rubro] + Lin
            # total de la fila: lo facturado por esa sucursal
            A[Reg.Suc, 8]         := A[Reg.Suc, 8]         + Lin
            # total de la columna: lo facturado por ese rubro
            A[6, Reg.Rubro]       := A[6, Reg.Rubro]       + Lin
            # total general
            A[6, 8]               := A[6, 8]               + Lin

            LEER(Arch, Reg)
        FIN_MIENTRAS

        CERRAR(Arch)

        Mostrar_Arreglo
        Mostrar_Salida_Solicitada
FIN_ACCION
```

> [!tip] Tres detalles de orden que sí se corrigen en el parcial
> 1. **`Poner_Cero_Arreglo` va antes de abrir el archivo.** En el apunte quedó *después* de la lectura anticipada. Funciona igual, pero el paso 1 de la metodología es poner la matriz a 0 — hacerlo primero deja el algoritmo alineado con la receta.
> 2. **La lectura anticipada va pegada al `ABRIR`**, y el `LEER` es la **última instrucción del ciclo**. Eso sí está bien en tu apunte. ✅
> 3. **`CERRAR(Arch)` puede ir apenas termina el ciclo**, no hace falta esperar a mostrar. Todo lo que se abre se cierra.

---

## 🔍 Cómo se cambia el "+ Lin" por "+ 1"

Comparado con el algoritmo de la filmina 10, la única diferencia es **qué se acumula**:

| | Filmina 10 (BD × Problemas) | `ESTAD` (Sucursales × Rubros) |
|---|---|---|
| Qué acumula | `+ 1` — **cuenta ocurrencias** | `+ Lin` — **acumula importes** |
| Tipo de la matriz | ENTERO | **REAL** |
| Cálculo previo | ninguno | `Lin := Cant * Precio_Unitario` |

Todo lo demás — las cuatro actualizaciones por registro, la fila y columna extra, el total general — es **idéntico**. Es la misma plantilla.

> [!important] Siempre son 4 actualizaciones por registro
> Cruce, total de fila, total de columna, total general. Si en el parcial escribís sólo la del cruce, el cuadro sale con los márgenes en 0. Si escribís las cuatro pero olvidás una, el cuadro no cierra.

---

## ❓ Lo que falta — `Mostrar_Salida_Solicitada`

`Mostrar_Salida_Solicitada` es un placeholder: el apunte **no tiene la consigna**, así que no sabemos qué informa. En un proceso estadístico las salidas típicas se resuelven todas después del ciclo, recorriendo los márgenes de la matriz:

| Lo que suele pedirse | Cómo se resuelve |
|---|---|
| Sucursal que más facturó | máximo sobre la **columna 8**, `PARA i := 1 A 5` |
| Rubro que menos facturó | mínimo sobre la **fila 6**, `PARA j := 1 A 7`, con `menor := HV` |
| Total facturado | acceso directo a `A[6,8]` |
| Total de un rubro puntual | acceso directo a `A[6, k]` |
| % que representa cada rubro | `A[6,j] * 100 / A[6,8]` — **verificar que `A[6,8] > 0`** antes de dividir |
| Combinación suc-rubro con menos ventas | doble `PARA` sobre `1..5 × 1..7`, sin tocar la fila 6 ni la columna 8 |

> [!todo] Pendiente
> 1. **Recuperar la consigna del ejercicio** y escribir `Mostrar_Salida_Solicitada` completo.
> 2. Ojo con los recorridos de búsqueda: van **hasta 5 y hasta 7**, no hasta 6 y 8. Si incluís la fila/columna de totales en la búsqueda del máximo, el máximo siempre va a ser el total. Es el error más común del tema.
> 3. Rehacé el algoritmo desde 0 sin mirar — la cátedra lo pide literalmente en la filmina 10.

---

## 🔁 Repaso (flashcards)

¿De qué tamaño es la matriz de un proceso estadístico con N categorías de fila y M de columna?::`[1..N+1, 1..M+1]` — una fila y una columna extra para los totales; la intersección `[N+1, M+1]` es el total general.

¿Cuántas actualizaciones se hacen por cada registro leído?::Cuatro: la celda del cruce, el total de la fila, el total de la columna y el total general.

¿El archivo de un proceso estadístico necesita estar ordenado?::No. El orden sólo importa en corte de control; acá la matriz acumula por índice.

¿Con qué se inicializa una variable para buscar un mínimo?::Con `HV` (High Value), para que la primera comparación siempre entre.

¿Con qué cierra el bloque PROCESO de una ACCION?::Con `FIN_ACCION`. `FIN_PROCESO` no existe en la notación de cátedra.

---

## 🔗 Notas relacionadas

- [[6 — Procesos Estadísticos]] — la teoría de cátedra de este mismo tema, con el algoritmo resuelto y dos problemas de práctica
- [[4 — Arreglos]] — arreglos bidimensionales, el sustrato de este tema
- [[5 — Búsqueda y Ordenamiento]] — los máximos y mínimos sobre los márgenes de la matriz
- [[Clase 1 — apuntes de arreglos]] — la clase anterior
- [[plantillas]] — plantilla canónica de procesamiento secuencial de archivos
- [[errores-y-trampas]] · [[sintaxis-completa]] · [[SKILL — pseudocodigo-utn]]
