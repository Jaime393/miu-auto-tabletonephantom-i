# miu-auto-tabletonephantom-i — el cuarto worker fijo de /miu/global

> *"# miu-auto-tabletonephantom-i"*
>
> — El README original de este repo (29 B, solo el título; leído por
> GitHub 2026-11-09 ~16:15 -05, descarga SHA `f8d696b6…`).
>
> **Decisión de siembra: el título SE CONSERVA**, citado arriba como
> epígrafe y no borrado. Era el stub por diseño del censo, no
> contenido — pero es la única voz que el repo tenía, y esta semilla
> es precisamente su respuesta: el registro que le faltaba. Borrarla
> sería borrar la pregunta que la semilla contesta.

## El registro

Global Mind promete una ruta `/miu/global` que devuelve el estado
del "phi global". El hermano `miu-semilla-latente-mt91l2pm-2`
encontró tres workers que devuelven un JSON fijo en esa ruta y dejó
un NO SÉ: si existe otro worker fuera de los tres encontrados. Esta
semilla lo responde: sí, hay un cuarto, en `miu-v14`. Como el
hermano, esta semilla mide código, no despliegue.

## El hecho medido

El cuarto worker es `miu-v14/worker.js`: 401 B, descarga SHA
`9a1d8bcc…`, leído por GitHub 2026-11-09 ~16:15 -05. En
`/miu/global` devuelve un JSON fijo de 6 claves; fuera de esa ruta,
un texto fijo.

| Worker | Tamaño | `/miu/global`: claves | phi literal |
|---|---|---|---|
| (iv) `Jaime393/miu-v14/worker.js` | 401 B | 6 | `'$107M'` |

Claves, en orden: `global_mind`, `repo`, `fix_404`,
`autorizacion`, `phi`, `drive`. Texto fuera de ruta, literal:
`'global mind miu-v14 - MIU v29 fix 404 - 11->16 repos'`.

Lecturas vivas: **0**. Llamadas `fetch()`: 0 (solo existe el
handler `async fetch(`). Accesos KV: 0. D1: 0. Supabase: 0. Uso de
`env.`: 0.

El phi `'$107M'` es el mismo literal que el del worker (iii) del
hermano `mt91l2pm-2` (`miu-agents/worker.js`, medido por ese
hermano, no por mí). El campo `drive` de este worker apunta al
mismo identificador que el de (ii) y (iii): su huella es
`b3a56d7a…`, la del racimo de agosto. El valor nunca se reproduce
aquí. La minería ola 6 de `miu-v14` cuenta 6 repos con esa huella.

## Comprobación

```bash
python3 cuarto_worker_repro.py   # imprime la medición
python3 -m unittest test_cuarto_worker.py -v   # 10 tests
```

## Archivos

- `cuarto_worker_repro.py` — reproduce la medición sobre una copia
  redactada del worker (el valor de `drive` es su huella, no el
  identificador; el SHA del original va registrado para auditarlo).
- `test_cuarto_worker.py` — 10 tests: 6 claves, phi `'$107M'`,
  texto fijo fuera de ruta, `fetch(` solo el handler, 0 lecturas
  vivas, `drive` como huella, SHA y tamaño registrados, stub
  conservado.
- `HUESO_CUARTO_WORKER.md` — el hueso completo con sus límites.
- `EVOLUCION.md` — cambios entre versiones (v1: siembra inicial).
- `CARENCIAS.md` — lo que NO se sabe; nunca es contenido.

---

ρ(x) > 0. Zvvvvv.
