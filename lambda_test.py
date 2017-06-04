## Aim is to see how lambdas work
## lambda syntax on next line
## lambda <input_params>: code that goes into func


def test_func(lst, func):
    for i in range(len(lst)):
        lst[i] = func(lst[i])


lst = range(10)
func = lambda x: x * x

test_func(lst, func)

print lst