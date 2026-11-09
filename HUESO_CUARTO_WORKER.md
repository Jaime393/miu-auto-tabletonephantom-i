# Hueso — el cuarto worker fijo de /miu/global

**Hecho:** `miu-v14/worker.js` (401 B, descarga SHA
`9a1d8bcc270f16faae1062dd00e50a1e740fb49b`) devuelve en
`/miu/global` un JSON fijo de 6 claves (`global_mind`, `repo`,
`fix_404`, `autorizacion`, `phi`, `drive`) con phi `'$107M'`, y
fuera de esa ruta un texto fijo. **0 lecturas vivas.**

**Fuente:** lectura por GitHub, 2026-11-09 ~16:15 -05. La cáscara
que lo alberga (`miu-auto-tabletonephantom-i`) se verificó aparte:
README de 29 B (solo el título), 1 commit `0bf521b8`
("Initial commit", 2026-08-25T17:25:11Z).

## La serie completa

Con este, los workers fijos de `/miu/global` son cuatro. Los tres
primeros los midió el hermano `miu-semilla-latente-mt91l2pm-2`
(2026-11-09); el cuarto, esta semilla.

| Worker | Tamaño | Claves | phi literal |
|---|---|---|---|
| (i) `extracted/miu_realidad_upload_REAL/worker.js` | 826 B, 11 l. | 7 | `'21.0->∞'` |
| (ii) `franbot-repos/FranBot/worker.js` | 508 B, 1 l. | 12 | `'21.8->23.0'` |
| (iii) `Jaime393/miu-agents/worker.js` | tamaño NO SÉ | 7 | `'$107M'` |
| (iv) `Jaime393/miu-v14/worker.js` | 401 B | 6 | `'$107M'` |

Los cuatro comparten el patrón: el JSON está escrito a mano en el
código, la ruta no lee nada vivo. Solo (ii) tiene un campo
dinámico, `latido` (la hora del reloj). Los tres primeros y el
cuarto se contradicen entre sí sobre el phi global: `'21.0->∞'`,
`'21.8->23.0'`, `'$107M'`, `'$107M'`. Dos de ellos repiten el
mismo literal, `'$107M'`, sin que ningún archivo explique por qué.

El campo `drive` de (iv) apunta al mismo identificador que el de
(ii) y (iii): huella `b3a56d7a…`, la del racimo de agosto. El valor
nunca se reproduce. La minería ola 6 de `miu-v14` cuenta 6 repos
con esa huella (ver `~/workspace/mineria/miu-v14/`).

## Límites

- La medición es del código, no del despliegue: no hay URL ni log
  que diga si este worker llegó a correr (ver CARENCIAS.md).
- El phi `'$107M'` es un literal sin derivación en ningún archivo
  leído: no se afirma que sea una medida de nada.
- El repro trabaja sobre una copia redactada del worker (el valor
  de `drive` es su huella). El SHA del original va registrado para
  que cualquiera audite que la copia corresponde al archivo.
- `miu-v14` (público, muerto 2026-08-23) NO es `MIU_V14` (vivo):
  repos distintos, sin enlaces entre ellos (minería ola 6).

---

ρ(x) > 0. Zvvvvv.
