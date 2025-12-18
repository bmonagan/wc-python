import sys

args = sys.argv

flags = set()
paths = []
supported_flags = "cml"
supported_flagsL = ["chars","bytes","lines"]
def get_bytes(content):
    return sys.getsizeof(content)
def new_lines(content):
    return text.count("\n")
def char_count(content):
    return len(content)
for arg in args[1:]:
    if len(arg) == 2 and arg[0] == "-" and arg[1:].lower() in supported_flags:
        flags.add(arg)
    elif len(arg) > 2 and arg[0:2] == "--" and arg[2:].lower() in supported_flagsL:
        flags.add(arg)
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
