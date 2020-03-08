# import 방식
# 모듈 import
# 함수 import
import fibo


def main():
    n = 10
    fibo.fib(n)

    val = fibo.fib2(n)
    print("fib2 ==> ", val)

# import 모듈이름
# from 모듈이름 import 모듈함수


# 이 모듈이 단독으로 사용되면 main()를 호출하라.
if __name__ == "__main__":
    main()
