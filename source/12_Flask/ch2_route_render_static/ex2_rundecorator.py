def check(func):
    def wrapper():
        print(func.__name__, '함수 전처리 작업 함')
        func()
        print(func.__name__, '함수 후처리 작업 함')
    return wrapper # function를 return

def hello():
    # print(hello.__name__,'함수 전처리 작업 함')
    print('Hello')
    # print(hello.__name__, '함수 후처리 작업 함')


def world():
    # print(world.__name__, '함수 전처리 작업 함')
    print('World')
    # print(hello.__name__, '함수 후처리 작업 함')


if __name__ == "__main__":
    trace_hello = check(hello)
    trace_hello()
    trace_world = check(world)
    trace_world()
    # world()
    # hello()
