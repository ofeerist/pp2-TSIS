import os

# 1
def ls(path):
    print("Directories:", list(filter(os.path.isdir, os.listdir(path))))
    print("Files:", list(filter(os.path.isfile, os.listdir(path))))
    print("Files and Directories:", os.listdir(path))

# 2
def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

# 3
def path_exists(path):
    if os.path.exists(path):
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("File does not exists")

# 4
def count_lines(path):
    with open(path, 'r') as f:
        print("Count:", len(f.readlines()))

# 5
def write_list(file_path, data):
    with open(file_path, 'w') as f:
        f.write(str(data))

def generate(path):
    for c in range(65, 91):
        f = open(f"{path}{chr(c)}.txt", 'w')

def cp(f, t):
    f1 = open(f, 'r').read()
    f2 = open(t, 'w')
    f2.write(f1)

def delete(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
    else:
        print("File does not exist or no permission to delete")

ls("./")
check_access("demofile2.txt")
path_exists("pp2-TSIS/TSIS1/w3school-examples/1_home.py")
count_lines("pp2-TSIS/TSIS1/w3school-examples/7_casting.py")
write_list("demofile.txt", ["str", "list", "1", "2"])
generate("./generated/")
cp("demofile2.txt", "generated/copy.txt")
delete("generated/copy.txt")