for i in range(10):
    print("GCI is great")
name = input("Enter your name - ")
print("Hello", name, ", pleased to meet you!")
revname = ""
for j in range(-1,-len(name)-1,-1):
    revname+=name[j]
print("Did you know that your name backwards is",revname)