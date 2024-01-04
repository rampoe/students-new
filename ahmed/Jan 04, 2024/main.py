sample_string = "Hello, World!"

f = open("output.txt", "wt")
f.write(sample_string)
f.close()

f = open("output.txt", "rt")

while True:
    current_line = f.readline()
    if len(current_line) == 0:
        break
    print(current_line, end="")

f.close()
