import time
# def factorial(n) -> int:
#     result = 1
#     for i in range(1,n+1):
#         result = result * i
#         return result
def timer(func) :
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"during time : {end - start}")
        return result
    return wrapper




@timer
def Combination(n,r) -> int: # SRP, OCP violation
    """
    this is combination func
    :param n:
    :param r:
    :return:
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)

    return int(numerator / denominator)


def factorial(num) -> int:
    """
    recusion
    :param num:
    :return:
    """

    if num == 1:
        return 1
    else:
        return num * factorial(num-1)