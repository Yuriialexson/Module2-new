a = 5
b = 10

def printer():
    global a, b
    a = "Str"
    b = "Str 2"
    c = 15
    d = 20
    print(c,d, "local")
    print(a,b, "global")


printer()
print(a,b)