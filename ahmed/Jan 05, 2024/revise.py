import pickle

todo_list = []

while True:
    current_task = input("введите задачу еще раз: ")
    if not current_task:
        break
    todo_list.append(current_task)

f = open("smth.data", "wb")
pickle.dump(todo_list, f)
f.close()
