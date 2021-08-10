import sys

#version and version_info
print(sys.version)
print(sys.version_info)

#stdin
print("Please enter a string: ")
message = sys.stdin.readline(8)
print(message)

#stdout
sys.stdout.write("I like Python")
print()

#platform
print(sys.platform)

#path
for dirpath in sys.path:
    print(dirpath)
