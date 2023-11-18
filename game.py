import random


class zeroPencil(Exception):
    pass


class nonnumericPencil(Exception):
    pass


def lesser_bot(p_count):
    if p_count % 4 == 1 and p_count != 1:
        input_2 = random.randint(1, 3)
    if p_count == 1:
        input_2 = 1
    if p_count % 4 == 0:
        input_2 = 3
    if p_count % 2 == 1 and p_count != 1:
        input_2 = 2
    if p_count == 2:
        input_2 = 1
    if p_count % 4 == 2:
        input_2 = 1
    return input_2


while True:
    try:
        p_count = input('How many pencils would you like to use:')
        if int(p_count) == 0:
            raise zeroPencil
        elif int(p_count) < 0:
            raise zeroPencil
        elif not int(p_count.isdigit()):
            raise ValueError
        else:
            break

    except ValueError:
        print('The number of pencils should be numeric')
        continue
    except zeroPencil:
        print('The number of pencils should be positive')
        continue

while True:
    try:
        p_count = int(p_count)
        John = 'John'
        Jack = 'Jack'
        nameCheck = True

        while nameCheck:
            userInput = input(f'Who will be the first ({John}, {Jack}):')
            if userInput != John and userInput != Jack:
                print('Choose between *Name1* and *Name2*')
            else:
                nameCheck = False

        print(p_count * '|')
        break
    except ValueError:
        print('Choose between *Name1* and *Name2*')

if userInput == John:
    while True:
        try:  # Allowed list of inputs
            falsePick1 = True
            falsePick_list = [1, 2, 3]

            while falsePick1:
                input_1 = input("John's turn!")
                if not input_1.isdigit():
                    print("Possible values: '1', '2' or '3'")
                else:
                    input_1 = int(input_1)
                    if input_1 not in falsePick_list:
                        print("Possible values: '1', '2' or '3'")
                        continue
                    elif p_count < 4:
                        if input_1 > p_count:
                            print("Too many pencils were taken")
                            continue
                        else:
                            break
                    else:
                        falsePick1 = False

            print((p_count - input_1) * '|')
            p_count = p_count - input_1

            if p_count == 0:        # Winning sequence
                print('Jack won!')
                break

            print("Jack's turn:")              # Bots turn
            input_2 = lesser_bot(p_count)
            print(input_2)
            print((p_count - int(input_2)) * '|')
            p_count = p_count - int(input_2)

            # Winning sequence
            if p_count == 0:
                print('John won!')
                break
            else:
                continue

        except ValueError:
            print('The number of pencils should be numeric')
        except zeroPencil:
            print('The number of pencils should be positive')

if userInput == Jack:
    while True:
        try:
            print("Jack's turn:")  # Bots turn first
            input_2 = lesser_bot(p_count)
            print(input_2)
            print((p_count - int(input_2)) * '|')
            p_count = p_count - int(input_2)

            if p_count == 0:        # Winning sequence
                print(f'{userInput} won!')
                break

            falsePick1 = True
            falsePick_list = [1, 2, 3]

            while True:
                input_1 = input("John's turn!")
                if not input_1.isdigit():
                    print("Possible values: '1', '2' or '3'")
                else:
                    input_1 = int(input_1)

                    if input_1 not in falsePick_list:
                        print("Possible values: '1', '2' or '3'")
                        continue
                    if input_1 > p_count:
                        print("Too many pencils were taken")
                        continue
                    else:
                        break
            p_count = p_count - int(input_1)
            print(p_count * '|')
            if p_count == 0:
                print(f'{userInput} won!')
                break

        except ValueError:
            print('The number of pencils should be numeric')
        except zeroPencil:
            print('The number of pencils should be positive')
