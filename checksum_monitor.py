#!/usr/bin/env python3
"""
checksum_monitor.py
Modo init: cria baseline.json com checksums SHA256 dos arquivos.
Modo check: compara e lista arquivos modificados/novos/removidos.
USO:
    python3 checksum_monitor.py init /path/to/sandbox
    python3 checksum_monitor.py check /path/to/sandbox
"""
import sys, hashlib, json
from pathlib import Path

BASELINE = "baseline_checksums.json"

def sha256_of_file(p: Path):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def init_baseline(sandbox: Path):
    data = {}
    for p in sandbox.iterdir():
        if p.is_file():
            data[p.name] = sha256_of_file(p)
    (sandbox / BASELINE).write_text(json.dumps(data, indent=2))
    print(f"Baseline criada em {sandbox / BASELINE}")

def check(sandbox: Path):
    mf = sandbox / BASELINE
    if not mf.exists():
        print("Baseline não encontrada. Rode 'init' primeiro.")
        return
    baseline = json.loads(mf.read_text())
    current = {}
    for p in sandbox.iterdir():
        if p.is_file():
            current[p.name] = sha256_of_file(p)
    modified = [f for f in baseline if f in current and baseline[f] != current[f]]
    removed = [f for f in baseline if f not in current]
    added = [f for f in current if f not in baseline]
    print("Modificados:", modified)
    print("Removidos:", removed)
    print("Adicionados:", added)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 checksum_monitor.py [init|check] /path/to/sandbox")
        sys.exit(1)
    action = sys.argv[1]
    sandbox = Path(sys.argv[2]).resolve()
    if action == "init":
        init_baseline(sandbox)
    elif action == "check":
        check(sandbox)
    else:
        print("Ação inválida. Use 'init' ou 'check'.")
