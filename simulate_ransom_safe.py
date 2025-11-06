#!/usr/bin/env python3
"""
simulate_ransom_safe.py
Simulação segura: NÃO altera o conteúdo dos arquivos. Apenas renomeia adicionando extensão do arquivo.
.ENCRYPTED_SIM e grava manifesto.json com mapeamento original->novo. Permite restauração.
USO:
    python3 simulate_ransom_safe.py /path/to/sandbox
    python3 simulate_ransom_safe.py --restore /path/to/sandbox
"""
import sys
import json
from pathlib import Path

MANIFEST_NAME = "manifesto_simulacao.json"
TAG = ".ENCRYPTED_SIM"

def simulate(sandbox: Path):
    manifest = {}
    for p in sandbox.iterdir():
        if p.is_file() and not p.name.endswith(MANIFEST_NAME) and not p.name.endswith(TAG):
            new_name = p.with_name(p.name + TAG)
            p.rename(new_name)
            manifest[new_name.name] = p.name  # store mapping new->original
    (sandbox / MANIFEST_NAME).write_text(json.dumps(manifest, indent=2))
    print(f"Simulação completa. salvo em {sandbox / MANIFEST_NAME}")

def restore(sandbox: Path):
    mf = sandbox / MANIFEST_NAME
    if not mf.exists():
        print("Manifesto não encontrado. Nada a restaurar.")
        return
    manifest = json.loads(mf.read_text())
    for new_name, orig_name in manifest.items():
        new_path = sandbox / new_name
        if new_path.exists():
            new_path.rename(sandbox / orig_name)
    mf.unlink()
    print("Restauração completa.")

if __name__ == "__main__":
    if len(sys.argv) not in (2,3):
        print("Uso: python3 simulate_ransom_safe.py [/--restore] /path/to/sandbox")
        sys.exit(1)
    if sys.argv[1] == "--restore":
        sandbox = Path(sys.argv[2]).resolve()
        restore(sandbox)
    else:
        sandbox = Path(sys.argv[1]).resolve()
        simulate(sandbox)
