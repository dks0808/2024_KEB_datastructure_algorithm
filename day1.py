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

if __name__ == "__main__": # 메인인 함수를 알려주기 위함. 전역 변수를 정해주는 것.여러개의
    n = int(input("Enter entire number : "))
    r = int(input("Input you want combinations : "))
    print(f"{n}C{r} = {Combination(n,r)}")

