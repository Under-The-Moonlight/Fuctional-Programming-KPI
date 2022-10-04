def Singleton(arg):
    return [arg]


def null(arg):
    return not arg


def snoc(arr, arg):
    if (type(arr) == list):
        arr.append(arg)
        return arr
    else:
        return "Not list"


def length(arr):
    return len(arr)


# test 1
arg = "Hello again"
var = Singleton(arg)
print(f"{var}")

# test 2
arg = ["Hello", "Again"]
var = null(arg)
print(var)
arg = []
var = null(arg)
print(var)

# test 3
arr = ["Hello", "Again"]
arg = 6
var = snoc(arr, arg)
print(var)

# test 4
arr = ["Hello", "Again", "Hello", "Again", "Hello", "Again", "Hello", "Again", "Hello", "Again", "Hello", "Again",
       "Hello", "Again", "Hello", "Again", "Hello", "Again", "Hello", "Again", "Hello", "Again", "Hello", "Again",
       "Hello", "Again"]
var = length(arr)
print(var)
