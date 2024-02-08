import mymath
# recursion func is more slow than repeat
# because repeat is use register or cash memory recursion func is use main memory


if __name__ == "__main__": # 메인인 함수를 알려주기 위함. 전역 변수를 정해주는 것.여러개의
    n = int(input("Enter entire number : "))
    r = int(input("Input you want combinations : "))
    print(f"{n}C{r} = {mymath.Combination(n,r)}")

