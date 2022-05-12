def compute_divide(a, b):

    try:
        print(f"{a} / {b} = {a/b}")
        return a / b
    except ZeroDivisionError:
        print("Divide by zero not permitted")


compute_divide(5, 1)


