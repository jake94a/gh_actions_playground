import sys

f = open("ignore-files.txt")
ignore_files = f.read().splitlines()
f.close()
all_changed_files = sys.argv[1:]

# file_diff = [
#     x
#     for x in ignore_files + all_changed_files
#     if x not in ignore_files or x not in all_changed_files
# ]

# print("file_diff", file_diff)

compared = []
for changed_file_name in all_changed_files:
    if changed_file_name not in ignore_files:
        compared.append(changed_file_name)
        break

print("compared", compared)
