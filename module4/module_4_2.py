print()
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function() # выполняется

print()

inner_function() # не выполняется, т.к. объемлющая область видимости




