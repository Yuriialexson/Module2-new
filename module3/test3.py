def func_with_params(a, b=2, c=None):
    global с
    if c is None:
        c = []
        c.append(a)
    print(a, b, c)

func_with_params (a=23, b=23, c=23)
func_with_params (a=23, b=23, c=None)
func_with_params(3)
func_with_params(4)
func_with_params(5)
func_with_params(6)
func_with_params (a=23, b=23, c=None)