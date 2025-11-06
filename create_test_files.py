## 1) create_test_files.py — cria arquivos de teste
```python
#!/usr/bin/env python3
"""
create_test_files.py
Cria arquivos de teste em um diretório sandbox.
USO: python3 create_test_files.py /caminho/para/sandbox
"""
import sys
from pathlib import Path

def create_files(folder: Path, n_txt=5, n_bin=3):
    folder.mkdir(parents=True, exist_ok=True)
    for i in range(1, n_txt+1):
        p = folder / f"document_{i}.txt"
        p.write_text(f"This is test document {i}.\nUse this file for safe experiments.\n")
    for i in range(1, n_bin+1):
        p = folder / f"image_{i}.jpg"
        p.write_bytes(b"\xff\xd8\xff" + bytes(100))  # placeholder JPG header + padding
    print(f"Created {n_txt} text and {n_bin} binary placeholder files in {folder}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 create_test_files.py /path/to/sandbox")
        sys.exit(1)
    sandbox = Path(sys.argv[1]).resolve()
    create_files(sandbox)
