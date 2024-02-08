import time
# def factorial(n) -> int:
#     result = 1
#     for i in range(1,n+1):
#         result = result * i
#         return result

def Combination(n,r) -> int:
    """
    this is combination func
    :param n:
    :param r:
    :return:
    """
    start = time.time()
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    end = time.time()
    print(f"during time : {end - start}")
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