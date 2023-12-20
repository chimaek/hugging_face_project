'''
데코레이터 만들기
'''


def first():
    print("first 시작")
    print("first")
    print("first 종료")

def second():
    print("second 시작")
    print("second")
    print("second 종료")


def deco(func):
    def wrapper():
        print(func.__name__,"시작") #__name__으로 함수 이름 출력
        print(func)
        print(func.__name__,"종료")
    return wrapper

# deco(first()) # 파라미터로 함수를 넘겨줌
# deco(second())
def deco2(func):
    def wrapper():
        print(func.__name__,"시작") #__name__으로 함수 이름 출력
        func()
        print(func.__name__,"종료")
    return wrapper
@deco2
def deco_first():
    print("first")

@deco2
def deco_second():
    print("second")

deco_first()




