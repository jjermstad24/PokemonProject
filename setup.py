#!/usr/bin/env python3

import os
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
VENV_DIR = ROOT / ".venv"
REQ_FILE = ROOT / "requirements.txt"


def run(cmd):
    print(f"> {' '.join(map(str, cmd))}")
    subprocess.check_call(cmd)


def get_venv_python():
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def main():
    # Create venv if needed
    if not VENV_DIR.exists():
        print("Creating virtual environment...")
        run([sys.executable, "-m", "venv", str(VENV_DIR)])
    else:
        print("Virtual environment already exists.")

    venv_python = get_venv_python()

    # Upgrade pip
    print("Upgrading pip...")
    run([str(venv_python), "-m", "pip", "install", "--upgrade", "pip"])

    # Install requirements
    if REQ_FILE.exists():
        print("Installing requirements...")
        run([str(venv_python), "-m", "pip", "install", "-r", str(REQ_FILE)])
    else:
        print("requirements.txt not found.")

    print("\nSetup complete.")
    print("\nActivate with:")

    if os.name == "nt":
        print(r"    .venv\Scripts\activate")
    else:
        print("    source .venv/bin/activate")


if __name__ == "__main__":
    main()