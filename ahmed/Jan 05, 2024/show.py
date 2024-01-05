from pickle import load

f = open("smth.data", "rb")
todo_list = load(f)
f.close()

# Вам нужно сделать следующие задачи:
# 1. аывфавфыавы
# 2. афваыавфы
# 3. выафаыфвафв

counter = 0

print("Вам нужно сделать следующие задачи:")
for i in todo_list:
    counter += 1
    print(f"{counter}. {i}")
