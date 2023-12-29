# color1, color2, color3, color4, color5, color6, color7

n = int(input("How many times do you want:  "))
a = input("What do yo want to print: ")


# for i in range(n):
#     print(f"{a}{i + 1}", end=", ")

counter = 0

while counter < n:
    print(f"{a}{counter + 1}", end=", ")
    counter += 1
