from subprocess import Popen, PIPE
f = open("output.txt", "w")
num = int(input())
i = f"tests/input{num}.txt"
inputs = open(i, "r")
child = Popen(["python", "Main.py"], stdin=PIPE, stdout=f)
child.communicate(inputs.read().encode("ascii"))
output = open("output.txt", "r")
real = open(f"tests/output{num}.txt")
if real.read() == output.read():
    print(True)
else:
    print(False)
