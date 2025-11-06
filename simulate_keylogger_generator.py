#!/usr/bin/env python3
"""
simulate_keylogger_generator.py
Gera um arquivo de log de teclas com frases de exemplo.
USO: python3 simulate_keylogger_generator.py /path/to/sandbox
"""
import sys
from pathlib import Path
import random

SAMPLE_PHRASES = [
    "login: user@example.com",
    "password: P@ssw0rd!",
    "Hello world, this is a typed sentence.",
    "The quick brown fox jumps over the lazy dog.",
    "Sample input for testing keylogger detection."
]

def generate(sandbox: Path, entries=50):
    sandbox.mkdir(parents=True, exist_ok=True)
    out = sandbox / "fake_keystrokes.log"
    with out.open("w", encoding="utf-8") as f:
        for _ in range(entries):
            phrase = random.choice(SAMPLE_PHRASES)
            timestamp = __import__("time").ctime()
            f.write(f"[{timestamp}] {phrase}\n")
    print(f"Generated synthetic keystroke log at {out}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 simulate_keylogger_generator.py /path/to/sandbox")
        sys.exit(1)
    sandbox = Path(sys.argv[1]).resolve()
    generate(sandbox)
