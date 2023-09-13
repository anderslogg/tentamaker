# Copyright (C) 2023 Anders Logg
# Licensed under the MIT License

import os
import importlib.resources
import importlib.metadata


def main():
    print(f"This is TentaMaker, version {importlib.metadata.version('tentamaker')}\n")

    print("Making exam...")

    # Check if exam has been initialized
    if not os.path.exists("pool.tex"):
        print("Exam has not been initialized. Run 'init-exam' first.")
        return
