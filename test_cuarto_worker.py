#!/usr/bin/env python3
"""Tests del repro del cuarto worker fijo (miu-v14/worker.js).

Solo stdlib. Corre con:
    python3 -m unittest test_cuarto_worker.py -v
desde este directorio.
"""

import os
import re
import unittest

import cuarto_worker_repro as repro


class TestCuartoWorker(unittest.TestCase):
    def test_claves_seis(self):
        self.assertEqual(
            repro.claves_del_json(repro.WORKER_JS_REDACTADO),
            ["global_mind", "repo", "fix_404", "autorizacion", "phi", "drive"],
        )

    def test_phi_107M(self):
        self.assertEqual(repro.phi_del_json(repro.WORKER_JS_REDACTADO), "$107M")

    def test_texto_fuera_ruta(self):
        self.assertEqual(
            repro.texto_fuera_ruta(repro.WORKER_JS_REDACTADO),
            "global mind miu-v14 - MIU v29 fix 404 - 11->16 repos",
        )

    def test_fetch_solo_handler(self):
        src = repro.WORKER_JS_REDACTADO
        self.assertIn("async fetch(", src)
        self.assertEqual(src.count("fetch("), 1)

    def test_sin_env(self):
        self.assertNotIn("env.", repro.WORKER_JS_REDACTADO)

    def test_sin_kv_d1_supabase(self):
        src = repro.WORKER_JS_REDACTADO
        self.assertNotIn("KV", src)
        self.assertNotIn("D1", src)
        self.assertNotIn("Supabase", src)

    def test_lecturas_vivas_cero(self):
        self.assertEqual(
            repro.lecturas_vivas(repro.WORKER_JS_REDACTADO),
            {"fetch": 0, "env": 0, "KV": 0, "D1": 0, "Supabase": 0},
        )

    def test_drive_es_huella(self):
        src = repro.WORKER_JS_REDACTADO
        self.assertIn("drive:'<huella b3a56d7a>'", src)
        # El identificador original nunca va en este archivo: el campo
        # drive es exactamente el marcador de huella, nada más.
        m = re.search(r"drive:'([^']*)'", src)
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "<huella b3a56d7a>")

    def test_sha_original_registrado(self):
        # SHA de descarga del conector GitHub: hash de blob git, 40 hex.
        self.assertEqual(len(repro.SHA_ORIGINAL), 40)
        self.assertTrue(repro.SHA_ORIGINAL.startswith("9a1d8bcc"))
        self.assertEqual(repro.BYTES_ORIGINAL, 401)

    def test_stub_conservado(self):
        aqui = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(aqui, "README.md"), encoding="utf-8") as f:
            readme = f.read()
        self.assertIn("# miu-auto-tabletonephantom-i", readme)


if __name__ == "__main__":
    unittest.main()
