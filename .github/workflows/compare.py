import os
import sys
from pathlib import Path

CHANGED_FILES = ["1.txt", "2.txt", ".github/workflows/build.yaml"]

f = open(".dockerignore")
ignore_files = f.read().splitlines()
f.close()
all_changed_files = sys.argv[1:]

for changed_file in CHANGED_FILES:
    print("os.path.basename(changed_file)a", os.path.basename(changed_file))
    print("os.path.dirname(changed_file)a", os.path.dirname(changed_file))

for ignore_file in ignore_files:
    print("os.path.basename(ignore_file)", os.path.basename(ignore_file))
    print("os.path.dirname(ignore_file)a", os.path.dirname(ignore_file))
