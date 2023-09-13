# Copyright (C) 2023 Anders Logg
# Licensed under the MIT License

import os, shutil
import importlib.resources
import importlib.metadata


def main():
    print(f"This is TentaMaker, version {importlib.metadata.version('tentamaker')}\n")

    print("Initializing exam...")

    # Create directories (if they don't exist)
    directories = ["tex", "pdf", "png", "tmp"]
    for directory in directories:
        if not os.path.exists(directory):
            print("Creating directory '%s'" % directory)
            os.mkdir(directory)
        else:
            print("Directory '%s' already exists" % directory)

    # Add question pool (if it doesn't exist)
    if not os.path.exists("pool.tex"):
        print("Copying question pool to 'pool.tex'")
        path = importlib.resources.files("tentamaker") / "resources" / "pool.tex"
        shutil.copy(path, "pool.tex")
    else:
        print("File 'pool.tex' already exists")
