import os
import sys

# Get the path to the GITHUB_ENV file
env_file_path = os.getenv("GITHUB_ENV")

# Check if the GITHUB_ENV file path is set
if env_file_path:
    # Open the GITHUB_ENV file in append mode
    with open(env_file_path, "a") as env_file:
        # Write the environment variable to the file
        env_file.write("NEW_ENV_VAR=1234\n")
else:
    print("GITHUB_ENV file path not found")
    sys.exit(1)
