import sys

args = sys.argv

flags = []
paths = []
supported_flags = "cml"
supported_flagsL = ["chars","bytes","lines"]

for arg in args[1:]:
    if len(arg) == 2 and arg[0] == "-" and arg[1:].lower() in supported_flags:
        flags.append(arg)
    elif len(arg) > 2 and arg[0:2] == "--" and arg[2:].lower() in supported_flagsL:
        flags.append(arg)
    else:
        paths.append(arg)
if not flags and not paths:
    print("error")
    sys.exit(5)
print(flags)
res = []

for path in paths:
    try: 
        with open(path, 'r') as p:
            content = p.read()
            print("file found")
    except FileNotFoundError:
        print(f"ERROR: File not found at path: {path}")
