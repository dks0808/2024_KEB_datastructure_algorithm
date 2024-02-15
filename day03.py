import tkinter as tk
def fibo_recursion(number: int) -> int:
    """
    fibonacci function by recursion.
    :param number: integer number
    :return: integer number
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibo_recursion(number - 1) + fibo_recursion(number - 2)


def fibo_repetition(number: int) -> int:
    """
    fibonacci function by repetition.
    :param number: integer number
    :return: integer number
    """
    a = 0
    b = 1
    for _ in range(number):
        a, b = b, a + b
    return a


memo = [0 if i == 0 else 1 if i == 1 else None for i in range(100)]
# memo = [0, 1] + [None] * (100-1)



# memo[0]=0
# memo[1] =1
def fibo_memoization(number: int) -> int:
    """
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    """
    global memo
    if memo[number] is not None:
        return memo[number]
    if number < 2:
        result = number
    else:
        result = fibo_memoization(number-1) + fibo_memoization(number-2)
        memo[number] = result
    return result
w = tk.Tk()
w.title("Fibonacci")
w.geometry("250x150")
lbl_display_fibonacci_result = tk.Lable(w, text = "Fibonacci by memoization")
en_input_number = tk.Entry(w)
btn_click = tk.button(w, text = "Click")

lbl_display_fibonacci_result.pack()
en_input_number.pack()
btn_click.pack(fill = "x")

w.mainloop()




# n = int(input("Input number : ")) #input box
#
# print(f"fibonacci{n} = {fibo_memoization(n)}") #lable
#
#

# for i in range(0, n):
#     print(i)
#     print(fibo_memoization(i))
# print("===========================")
# for i in range(0, n):
#     print(i)
#     print(fibo_recursion(i))
# print("===========================")
# for i in range(0, n):
#     print(i)
#     print(fibo_repetition(i))
