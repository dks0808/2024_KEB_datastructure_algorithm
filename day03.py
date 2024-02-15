import tkinter as tk

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

def process_fibonacci(number):
    number = int(en_input_number.get())
    lbl_display_fibonacci_result.config(text = f"fibonacci({number}) = {fibo_memoization(number)}")

if (__name__ == "__main__"):
    # UI not a functional part
    w = tk.Tk()
    w.title("Fibonacci")
    w.geometry("250x150")
    lbl_display_fibonacci_result = tk.Label(w, text = "Fibonacci by memoization")
    en_input_number = tk.Entry(w)
    btn_click = tk.Button(w, text = "Click", command=process_fibonacci) #bind function

    lbl_display_fibonacci_result.pack()
    en_input_number.pack()
    btn_click.pack(fill = "x")
    en_input_number.focus()
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
