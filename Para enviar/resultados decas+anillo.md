# RESULTADOS: DECAVANADATO + ANILLO AROMÁTICO (híbrido deca·adenina)

## Docking contra variantes de BRAF (kcal/mol)

| Receptor | V10 solo | Híbrido deca·adenina | Δ        | Mejora |
|----------|----------|----------------------|----------|--------|
| 3OG7     | -7.36    | -8.29                | -0.93    | ✓      |
| 4G9C     | -6.95    | -6.62                | +0.33    |        |
| 4WO5     | -7.45    | -8.53                | -1.08    | ✓      |
| 4XV2     | -6.26    | -7.31                | -1.05    | ✓      |
| 5C9C     | -8.04    | -7.80                | +0.24    |        |
| 6U2G     | -2.07    | -6.16                | -4.09    | ✓      |

## Modo de unión (3OG7): superficie vs bolsillo ATP

| Caja              | Energía  | Dist. al bolsillo ATP      | vdW   | Electrostatic |
|-------------------|----------|----------------------------|-------|---------------|
| Grande (48 Å)     | -8.29    | 22.47 Å (superficie)       | -0.11 | -8.18         |
| Chica (22 Å)      | -3.32    | 9.69 Å (forzado al bolsillo)| -0.47 | -7.80         |

## Conclusión

El híbrido deca·adenina mejora la afinidad en 4 de 6 variantes de BRAF
(caso máximo: 6U2G, Δ = -4.09 kcal/mol). Sin embargo, el modo de unión
favorable es SUPERFICIAL (electrostático, alostérico): al forzarlo al
bolsillo ATP pierde ~5 kcal/mol. Los decavanadatos NO compiten con el
ATP; actúan por unión a parches cargados de la superficie.
