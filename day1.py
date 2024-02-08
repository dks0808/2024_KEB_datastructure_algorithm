def factorial(n) -> int:
    for i in range(0,n):
        i

    pass

def Combination(n,r) -> int:
    """
    this is combination func
    :param n:
    :param r:
    :return:
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return numerator/ denominator

if __name__ = "__main__": # 메인인 함수를 알려주기 위함. 전역 변수를 정해주는 것.여러개의
    n = int(input("Enter entire number n : "))
    r = int(input("Input you want combi : "))
    print(f"{n}C{r} = {nCr(n,r)}")

