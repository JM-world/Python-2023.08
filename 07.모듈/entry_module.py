PI = 3.14159

def a():
    return float(input('숫자 입력> '))

def get_circumference(radius):
    return 2 * PI * radius

def get_area(radius):
    return PI * radius * radius

def print_name():
    print(__name__)

# cmd창으로 python entry_module.py와 같이 실행될 경우에는 
# __name__값이 __main__이 되며, 아래 코드가 실행됨
if __name__ == '__main__':
    print('원의 반지름: 10')
    print(f'둘레: {get_circumference(10):.4f}, 넓이: {get_area(10):.4f}')