import random


if __name__ == '__main__':
    while 1:
        try:
            command = input()
            match command:
                case 'Hi':
                    print('Hi')
                case 'GetRandom':
                    print(f'{random.randint(-2**31, 2 ** 31-1)}')
                case 'Shutdown':
                    exit(0)
                case _:
                    break
        except EOFError:
            break