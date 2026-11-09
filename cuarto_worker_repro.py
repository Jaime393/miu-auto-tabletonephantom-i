#!/usr/bin/env python3
"""Repro: el cuarto worker fijo de /miu/global (miu-v14/worker.js).

Mide lo que el archivo hace sin desplegarlo: en /miu/global devuelve
un JSON fijo de 6 claves; fuera de esa ruta, un texto fijo. 0 lecturas
vivas: nada se lee de la red, de KV, de D1 ni del entorno.

El código fuente va REDACTADO: el campo `drive` del original lleva un
identificador cuyo valor nunca se reproduce (regla del rincón); aquí va
su huella, `b3a56d7a…`, la del racimo de agosto. El archivo original
mide 401 B, descarga SHA
9a1d8bcc270f16faae1062dd00e50a1e740fb49b (GitHub, 2026-11-09 ~16:15 -05).

Solo stdlib. Salida 0 si todo coincide.
"""

import re
import sys

# Copia redactada de miu-v14/worker.js. El valor de `drive` es la huella,
# no el identificador; ver la nota del módulo.
WORKER_JS_REDACTADO = (
    "export default { async fetch(req){ const u=new URL(req.url); "
    "if(u.pathname=='/miu/global') return new Response(JSON.stringify("
    "{global_mind:true, repo:'miu-v14', fix_404:true, "
    "autorizacion:'TOTAL x10000 v29 fix 404', phi:'$107M', "
    "drive:'<huella b3a56d7a>'}),{headers:{'Content-Type':'application/json'}}); "
    "return new Response('global mind miu-v14 - MIU v29 fix 404 - 11->16 repos'); } }"
)

SHA_ORIGINAL = "9a1d8bcc270f16faae1062dd00e50a1e740fb49b"
BYTES_ORIGINAL = 401

CLAVES_ESPERADAS = ["global_mind", "repo", "fix_404", "autorizacion", "phi", "drive"]
PHI_ESPERADO = "$107M"
TEXTO_FUERA_RUTA = "global mind miu-v14 - MIU v29 fix 404 - 11->16 repos"


def claves_del_json(src):
    """Las claves del objeto que /miu/global devuelve, en orden."""
    m = re.search(r"JSON\.stringify\(\{(.*?)\}\)", src)
    if not m:
        return []
    return re.findall(r"(\w+):", m.group(1))


def phi_del_json(src):
    """El literal phi del JSON de /miu/global."""
    m = re.search(r"phi:'([^']*)'", src)
    return m.group(1) if m else None


def texto_fuera_ruta(src):
    """El texto fijo que devuelve cualquier ruta que no sea /miu/global."""
    m = re.search(r"return new Response\('([^']*)'\); \} \}", src)
    return m.group(1) if m else None


def lecturas_vivas(src):
    """Conteo de lecturas vivas: llamadas fetch, entorno, KV, D1, Supabase."""
    fetch_llamadas = src.count("fetch(") - (1 if "async fetch(" in src else 0)
    return {
        "fetch": fetch_llamadas,
        "env": src.count("env."),
        "KV": src.count("KV"),
        "D1": src.count("D1"),
        "Supabase": src.count("Supabase"),
    }


def main():
    src = WORKER_JS_REDACTADO
    ok = True

    claves = claves_del_json(src)
    print("1. claves del JSON de /miu/global:", claves)
    if claves != CLAVES_ESPERADAS:
        print("   NO COINCIDE: se esperaban", CLAVES_ESPERADAS)
        ok = False

    phi = phi_del_json(src)
    print("2. phi literal:", repr(phi))
    if phi != PHI_ESPERADO:
        print("   NO COINCIDE: se esperaba", repr(PHI_ESPERADO))
        ok = False

    texto = texto_fuera_ruta(src)
    print("3. texto fuera de ruta:", repr(texto))
    if texto != TEXTO_FUERA_RUTA:
        print("   NO COINCIDE: se esperaba", repr(TEXTO_FUERA_RUTA))
        ok = False

    vivas = lecturas_vivas(src)
    print("4. lecturas vivas:", vivas)
    if any(vivas.values()):
        print("   NO COINCIDE: se esperaban todas en 0")
        ok = False

    print("5. archivo original: %d B, descarga SHA %s…" % (BYTES_ORIGINAL, SHA_ORIGINAL[:8]))
    print("   campo drive: huella b3a56d7a (valor nunca reproducido)")

    if ok:
        print("TODO COINCIDE")
        return 0
    print("NO COINCIDE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
