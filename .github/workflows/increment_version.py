import re
import os
import sys

ENV_FILE_PATH = os.getenv("GITHUB_ENV")
NEW_VER = ""


def increment_version(old_version):
    # future accommodations for labels here
    # if label=new_patch then increment patch ver
    # if label=new_minor then increment minor ver
    # if label=new_major then increment major ver
    major, minor, patch = map(int, old_version)
    new_version = f"{major}.{minor}.{patch+1}"
    return new_version


with open("pyproject.toml", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    # search for a line that matches:
    # "version(possible whitespace)=(possible whitespace)digits.digits.digits"
    if re.search(r'version\s*=\s*"\d+\.\d+\.\d+"', line):
        version_match = re.search(r"\d+\.\d+\.\d+", line)
        if version_match:
            old_version = version_match.group()
            new_version = increment_version(old_version.split("."))
            NEW_VER = new_version
            lines[i] = re.sub(old_version, new_version, line)
            break

with open("pyproject.toml", "w") as f:
    f.writelines(lines)


# Check if the GITHUB_ENV file path is set
if ENV_FILE_PATH:
    # Open the GITHUB_ENV file in append mode
    with open(ENV_FILE_PATH, "a") as env_file:
        # Write the environment variable to the file
        env_file.write(f"NEW_VER={NEW_VER}")
else:
    print("GITHUB_ENV file path not found")
    sys.exit(1)
