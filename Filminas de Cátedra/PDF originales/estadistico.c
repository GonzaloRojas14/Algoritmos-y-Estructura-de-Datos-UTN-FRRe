/* ============================================================
   estadistico.c
   Algoritmos y Estructuras de Datos - UTN FRRe
   Procesos Estadisticos: cuadro estadistico con arreglo bidimensional

   Lee el archivo VENTAS (ventas.csv) y arma una matriz
   A[Sucursal, Rubro] con el total vendido ($) de la semana,
   agregando fila y columna de totales (igual que el pseudocodigo
   "Accion ESTAD" visto en clase).

   Compilar:  gcc -Wall -std=c99 estadistico.c -o estadistico
   Ejecutar:  ./estadistico ventas.csv
   ============================================================ */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SUC_MAX   5   /* sucursales:      1..5           */
#define RUBRO_MAX 7   /* rubros:          1..7           */
#define FILA_TOT  (SUC_MAX + 1)    /* fila   de totales -> 6 */
#define COL_TOT   (RUBRO_MAX + 1)  /* columna de totales -> 8 */

typedef struct {
    long  id;
    int   cod_prod;
    int   dia, mes, anio;
    int   suc;
    int   rubro;
    double cant;
    double precio_unitario;
} Venta;

const char *nombre_sucursal[SUC_MAX + 1] = {
    "-", "Resistencia", "Barranqueras", "Fontana", "Pto. Vilelas", "M. Belen"
};

const char *nombre_rubro[RUBRO_MAX + 1] = {
    "-", "Almacen", "Bebidas", "Lacteos", "Panificados",
    "Limpieza", "Congelados", "Perfumeria"
};

/* Poner_Cero_Arreglo */
void poner_cero(double A[FILA_TOT + 1][COL_TOT + 1]) {
    for (int i = 1; i <= FILA_TOT; i++)
        for (int j = 1; j <= COL_TOT; j++)
            A[i][j] = 0.0;
}

/* Leer(Arch, Reg) — lee un renglon del CSV. Devuelve 0 al llegar a FDA. */
int leer_registro(FILE *arch, Venta *reg) {
    char linea[256];
    if (!fgets(linea, sizeof(linea), arch)) return 0;   /* FDA(Arch) */

    int leidos = sscanf(linea, "%ld,%d,%d,%d,%d,%d,%d,%lf,%lf",
                         &reg->id, &reg->cod_prod,
                         &reg->dia, &reg->mes, &reg->anio,
                         &reg->suc, &reg->rubro,
                         &reg->cant, &reg->precio_unitario);
    return (leidos == 9) ? 1 : leer_registro(arch, reg); /* salta lineas invalidas */
}

void mostrar_arreglo(double A[FILA_TOT + 1][COL_TOT + 1]) {
    printf("\n%-14s", "Sucursal/Rubro");
    for (int j = 1; j <= RUBRO_MAX; j++) printf("%12s", nombre_rubro[j]);
    printf("%12s\n", "TOTAL");

    for (int i = 1; i <= FILA_TOT; i++) {
        printf("%-14s", (i == FILA_TOT) ? "TOTAL" : nombre_sucursal[i]);
        for (int j = 1; j <= COL_TOT; j++)
            printf("%12.2f", A[i][j]);
        printf("\n");
    }
}

void mostrar_salida_solicitada(double A[FILA_TOT + 1][COL_TOT + 1]) {
    int suc_max = 1, suc_min = 1, rubro_top = 1;

    for (int i = 1; i <= SUC_MAX; i++) {
        if (A[i][COL_TOT] > A[suc_max][COL_TOT]) suc_max = i;
        if (A[i][COL_TOT] < A[suc_min][COL_TOT]) suc_min = i;
    }
    for (int j = 1; j <= RUBRO_MAX; j++)
        if (A[FILA_TOT][j] > A[FILA_TOT][rubro_top]) rubro_top = j;

    printf("\n--- Informe solicitado ---\n");
    printf("Sucursal con MAYOR venta en la semana : %-14s ($ %.2f)\n",
           nombre_sucursal[suc_max], A[suc_max][COL_TOT]);
    printf("Sucursal con MENOR venta en la semana : %-14s ($ %.2f)\n",
           nombre_sucursal[suc_min], A[suc_min][COL_TOT]);
    printf("Rubro con mayor venta en la semana    : %-14s ($ %.2f)\n",
           nombre_rubro[rubro_top], A[FILA_TOT][rubro_top]);
    printf("Total general de ventas de la semana  : $ %.2f\n",
           A[FILA_TOT][COL_TOT]);
}

int main(int argc, char *argv[]) {
    const char *nombre_archivo = (argc > 1) ? argv[1] : "ventas.csv";

    FILE *arch = fopen(nombre_archivo, "r");
    if (!arch) {
        fprintf(stderr, "No se pudo abrir el archivo %s\n", nombre_archivo);
        return 1;
    }

    char cabecera[256];
    fgets(cabecera, sizeof(cabecera), arch);   /* descarta encabezado del CSV */

    static double A[FILA_TOT + 1][COL_TOT + 1];
    poner_cero(A);

    Venta reg;
    while (leer_registro(arch, &reg)) {
        double lin = reg.cant * reg.precio_unitario;

        A[reg.suc][reg.rubro] += lin;   /* celda sucursal-rubro     */
        A[reg.suc][COL_TOT]   += lin;   /* total de la sucursal     */
        A[FILA_TOT][reg.rubro]+= lin;   /* total del rubro          */
        A[FILA_TOT][COL_TOT]  += lin;   /* total general            */
    }
    fclose(arch);

    printf("Cuadro estadistico - Ventas de la semana por Sucursal y Rubro\n");
    mostrar_arreglo(A);
    mostrar_salida_solicitada(A);

    return 0;
}
