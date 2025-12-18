import sys

args = sys.argv

flags = set()
paths = []
supported_flags = "cml"
supported_flagsL = ["chars","bytes","lines"]
def get_bytes(content):
    return str(sys.getsizeof(content))
def new_lines(content):
    return str(content.count("\n"))
def char_count(content):
    return str(len(content))
for arg in args[1:]:
    if len(arg) == 2 and arg[0] == "-" and arg[1:].lower() in supported_flags:
        flags.add(arg.lower())
    elif len(arg) > 2 and arg[0:2] == "--" and arg[2:].lower() in supported_flagsL:
        if arg == "--chars":
            flags.add("-m")
        elif arg == "--bytes":
            flags.add("-c")
        elif arg == "--lines":
            flags.add("-l")
    else:
        paths.append(arg)
if not flags and not paths:
    print("error")
    sys.exit(5)
if not flags:
    flags = set("-c","-m","-l")

for path in paths:
    try: 
        with open(path, 'r') as p:
            content = p.read()
            output = []
            if "-l" in flags:
                output.append("lines " + new_lines(content))
            if "-m" in flags:
                output.append("chars " + char_count(content))
            if "-c" in flags:
                output.append("bytes " + get_bytes(content))
            output.append(path)
            filled = " ".join(output)
            print(filled)
    except FileNotFoundError:
        print(f"ERROR: File not found at path: {path}")

