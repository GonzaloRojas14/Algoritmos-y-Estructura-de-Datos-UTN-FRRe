"""
Genera las lecturas simuladas de una estación de monitoreo de temperatura
ambiente en Resistencia (Chaco), un día de octubre.

- M sensores, N lecturas por sensor (una cada 10 minutos -> N = 144 en 24 h).
- Patrón realista: ciclo diario (mínima de madrugada, máxima a media tarde)
  alrededor de los valores normales de octubre (17 °C de mínima media y 29 °C de
  máxima media, normales 1991-2020 de Resistencia Aero) más ruido de medición.
- El sensor 3 se comporta distinto: está descalibrado (deriva lenta hacia arriba)
  y tiene más ruido que los demás.
- Se inyectan rachas de valores fuera de rango (falla del sensor) en posiciones
  conocidas, que quedan documentadas como "verdad conocida".

Salida:
- lecturas.csv           una línea por lectura: sensor,nro,valor
- verdad_conocida.csv    las rachas inyectadas: sensor,inicio,longitud

Solo usa la biblioteca estándar de Python. La semilla es fija para que el
CSV salga siempre igual y se pueda validar contra la tabla.
"""

import csv
import math
import random

M = 5            # cantidad de sensores
N = 144          # lecturas por sensor: 24 h x 6 lecturas por hora (cada 10 min)
SEMILLA = 2026

# Parámetros de cada sensor: temperatura media del día, amplitud del ciclo
# diario, desvío del ruido y deriva por lectura (descalibración).
SENSORES = {
    1: {"media": 23.0, "amplitud": 6.0, "ruido": 0.3, "deriva": 0.00},  # abrigo meteorológico
    2: {"media": 22.5, "amplitud": 5.5, "ruido": 0.3, "deriva": 0.00},  # a la sombra
    3: {"media": 23.0, "amplitud": 6.0, "ruido": 1.2, "deriva": 0.03},  # descalibrado: ruido y deriva
    4: {"media": 24.0, "amplitud": 6.5, "ruido": 0.4, "deriva": 0.00},  # zona más expuesta
    5: {"media": 22.0, "amplitud": 5.0, "ruido": 0.3, "deriva": 0.00},  # cerca de vegetación
}

# Rachas inyectadas (falla del sensor: valores imposibles para el ambiente).
# La del sensor 5 es más corta a propósito, para ver si el algoritmo la detecta.
RACHAS = [
    {"sensor": 2, "inicio": 61, "longitud": 8},
    {"sensor": 4, "inicio": 97, "longitud": 6},
    {"sensor": 5, "inicio": 31, "longitud": 3},
]


def temperatura_base(sensor: int, nro: int) -> float:
    """Ciclo diario: mínima de madrugada y máxima a media tarde (cerca de las 15 h)."""
    p = SENSORES[sensor]
    hora = (nro - 1) * 10 / 60                     # la lectura 1 es a las 00:00
    # coseno centrado en las 15 h; el segundo término achata la curva de noche
    # para que la mínima quede de madrugada
    ciclo = math.cos(2 * math.pi * (hora - 15) / 24)
    ciclo += 0.25 * math.cos(4 * math.pi * (hora - 15) / 24)
    return p["media"] + p["amplitud"] * ciclo / 1.25 + p["deriva"] * nro


def generar() -> list[tuple[int, int, float]]:
    random.seed(SEMILLA)
    valores = {}
    for sensor in SENSORES:
        for nro in range(1, N + 1):
            ruido = random.gauss(0, SENSORES[sensor]["ruido"])
            valores[(sensor, nro)] = temperatura_base(sensor, nro) + ruido

    for racha in RACHAS:
        for k in range(racha["longitud"]):
            valores[(racha["sensor"], racha["inicio"] + k)] = random.uniform(45.0, 60.0)

    # la estación registra cada 10 minutos la lectura de todos los sensores,
    # así que el archivo queda ordenado por número de lectura y después por sensor
    return [(s, n, round(valores[(s, n)], 1)) for n in range(1, N + 1) for s in SENSORES]


def main() -> None:
    lecturas = generar()

    with open("lecturas.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sensor", "nro", "valor"])
        w.writerows(lecturas)

    with open("verdad_conocida.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sensor", "inicio", "longitud"])
        for r in RACHAS:
            w.writerow([r["sensor"], r["inicio"], r["longitud"]])

    print(f"lecturas.csv: {len(lecturas)} lecturas ({M} sensores x {N})")
    for r in RACHAS:
        print(f"  racha inyectada: sensor {r['sensor']}, desde la lectura {r['inicio']}, {r['longitud']} lecturas")


if __name__ == "__main__":
    main()
