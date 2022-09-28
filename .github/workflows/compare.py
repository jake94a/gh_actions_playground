import sys

f = open("ignore-files.txt")
ignore_files = f.readlines()
for line in ignore_files:
    print("line", line)

print("args: ", sys.argv)
