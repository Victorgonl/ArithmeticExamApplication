# Victorgonl - Arithmetic Exam Application - 20211227
# ArithmeticExamApplication.py

from random import seed, randint
seed()

SPLITER = ' '
MIN = 2
MAX = 9
MIN_SQUARE = 11
MAX_SQUARE = 29
N_TASKS = 5
FILE_NAME = "results.txt"


class Operation:
    x = 0
    y = 0
    operator = '+'
    
    def __init__(self, expression: str) -> None:
        expression = expression.split()
        x = expression[0]
        y = expression[2]
        operator = expression[1]
        if not is_int(x) or not is_int(y):
            raise Exception("Error: Invalid Integer Number!")
        if operator != '+' and operator != '-' and operator != '*' and operator != '^':
            raise Exception("Error: Invalid Operator!")
        self.x = int(x)
        self.y = int(y)
        self.operator = operator
        
    def result(self):
        if self.operator == '+':
            return self.x + self.y
        elif self.operator == '-':
            return self.x - self.y
        elif self.operator == '*':
            return self.x * self.y
        elif self.operator == '^':
            return self.x ** self.y


def is_int(string: str) -> bool:
    if string == '':
        return False
    if string[0] in ('-', '+'):
        return string[1:].isdigit()
    return string.isdigit()


def random_operator() -> str:
    choice = randint(0, 2)
    if choice == 0:
        return '+'
    elif choice == 1:
        return '-'
    elif choice == 2:
        return '*'


def random_operation() -> Operation:
    x = randint(MIN, MAX)
    y = randint(MIN, MAX)
    operator = random_operator()
    expression = str(x) + SPLITER + operator + SPLITER + str(y)
    op = Operation(expression)
    return op


def print_operation(op: Operation) -> None:
    print(op.x, op.operator, op.y)


def check_result(guess: int, op: Operation) -> bool:
    return guess == op.result()


def input_guess() -> int:
    guess = input()
    if not is_int(guess):
        raise Exception("Wrong format! Try again.")
    else:
        return int(guess)


def input_level() -> str:
    level = input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n")
    if level != '1' and level != '2':
        raise Exception("Incorrect format.")
    return level


def to_save() -> bool:
    save = input("Would you like to save the result? Enter yes or no.\n")
    if save == "yes" or save == 'y' or save == "YES" or save == "Yes":
        return True
    else:
        return False


def save_results(name: str, result: int, level: str) -> None:
    with open(FILE_NAME, "a+") as file:
        content = name + ": " + str(result) + '/' + str(N_TASKS) + " in level "
        if level == '1':
            content += level + " (simple operations with numbers " + str(MIN) + '-' + str(MAX) + ")."
        elif level == '2':
            content += level + " (integral squares of " + str(MIN_SQUARE) + '-' + str(MAX_SQUARE) + ")."
        content += '\n'
        file.write(content)


def main() -> None:
    result = 0
    while True:
        try:
            level = input_level()
            break
        except Exception as error:
            print(error)
    for _ in range(N_TASKS):
        if level == '1':
            op = random_operation()
            print_operation(op)
        elif level == '2':
            x = randint(MIN_SQUARE, MAX_SQUARE)
            print(x)
            expression = str(x) + " ^ 2"
            op = Operation(expression)
        else:
            return
        while True:
            try:
                if check_result(input_guess(), op):
                    print("Right!")
                    result += 1
                else:
                    print("Wrong!")
                break
            except Exception as error:
                print(error)
    print("Your mark is ", result, '/', N_TASKS, ". ", sep='', end='')
    if to_save():
        name = input("What is your name?\n")
        save_results(name, result, level)
        print("The results are saved in \"", FILE_NAME, "\".", sep='')


main()