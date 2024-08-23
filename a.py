from IPython.display import clear_output
lst = [" "," "," "]
lst2 = [" "," "," "]
lst3 = [" "," "," "]
def print_board():
    print(" | ".join(lst))
    print("-" * 9)
    print(" | ".join(lst2))
    print("-" * 9)
    print(" | ".join(lst3))
def check_win():
    if ' ' in lst or ' ' in lst2 or ' ' in lst3: 
        for i in lst[0]:
            if i == lst[1] and i == lst[2]:
                if ('X' in lst and 'O' not in lst) or ('O' in lst and 'X' not in lst):
                    print('a')
                    return True
            elif i == lst2[0] and i == lst3[0]:
                if ('X' in lst[0] and 'O' not in lst[0]) or ('O' in lst[0] and 'X' not in lst[0]):
                    print('a2')
                    return True
        for i in lst2[1]:
            if i == lst2[0] and i == lst2[2]:
                if ('X' in lst2 and 'O' not in lst2) or ('O' in lst2 and 'X' not in lst2):
                    print('a3')
                    return True
            elif i == lst[1] and i == lst3[1]:
                if ('X' in lst2[1] and 'O' not in lst2[1]) or ('O' in lst2[1] and 'X' not in lst2[1]):
                    print('a4')
                    return True
        for i in lst3[2]:
            if i == lst3[1] and i == lst3[0]:
                if ('X' in lst3 and 'O' not in lst3) or ('O' in lst3 and 'X' not in lst3):
                    print('a5')
                    return True
            elif i == lst[2] and i == lst2[2]:
                if ('X' in lst3[2] and 'O' not in lst3[2]) or ('O' in lst3[2] and 'X' not in lst3[2]):
                    print('a6')
                    return True
        if lst[0] == lst2[1] == lst3[2] or lst[2] == lst2[1] == lst3[0]:
            if ('X' in lst2[1] and 'O' not in lst2[1]) or ('O' in lst2[1] and 'X' not in lst2[1]):
                print('a7')
                return True
    else:
        return False
def user2_input():
    if check_win() == True:
        clear_output()
        print_board()
        print('PLAYER 2 YOU WON')
        return
    elif check_win() == False:
        clear_output()
        print_board()
        print('YOU DRAW')
        return
    acceptable_x_range = range(1,4)
    acceptable_y_range = range(1,4)
    print_board()
    user = input('Input your y position 1-3: ')
    while user.isdigit() == False or int(user) not in acceptable_y_range:
        clear_output()
        print_board()
        if user.isdigit() == False:
            print("can't u read ?")
        elif user.isdigit() == True:
            if int(user) not in acceptable_y_range:
                print('wtf is wrong with you ?')
        user = input('Input again y your position 1-3: ')
    clear_output()
    print_board()
    user2 = input('Input your x position 1-3: ')
    while user2.isdigit() == False or int(user2) not in acceptable_y_range:
        clear_output()
        print_board()
        if user2.isdigit() == False:
            print("can't u read ?")
        elif user2.isdigit() == True:
            if int(user2) not in acceptable_x_range:
                print('wtf is wrong with you ?')
        user2 = input('Input again x your position 1-3: ')
    clear_output()
    user = int(user)
    user2 = int(user2)
    if user == 1:
        if lst[user2-1] == " ":
            lst[user2-1] = 'O'
        else:
            print('The position is already taken')
            user2_input()
    elif user == 2:
        if lst2[user2-1] == " ":
            lst2[user2-1] = 'O'
        else:
            print('The position is already taken')
            user2_input()
    elif user == 3:
        if lst3[user2-1] == " ":
            lst3[user2-1] = 'O'
        else:
            print('The position is already taken')
            user2_input()
    user1_input()
def user1_input():
    if check_win() == True:
        clear_output()
        print_board()
        print('PLAYER 1 YOU WON')
        return
    elif check_win() == False:
        clear_output()
        print_board()
        print('YOU DRAW')
        return
    acceptable_x_range = range(1,4)
    acceptable_y_range = range(1,4)
    print_board()
    user = input('Input your y position 1-3: ')
    while user.isdigit() == False or int(user) not in acceptable_y_range:
        clear_output()
        print_board()
        if user.isdigit() == False:
            print("can't u read ?")
        elif user.isdigit() == True:
            if int(user) not in acceptable_y_range:
                print('wtf is wrong with you ?')
        user = input('Input again y your position 1-3: ')
    clear_output()
    print_board()
    user2 = input('Input your x position 1-3: ')
    while user2.isdigit() == False or int(user2) not in acceptable_y_range:
        clear_output()
        print_board()
        if user2.isdigit() == False:
            print("can't u read ?")
        elif user2.isdigit() == True:
            if int(user2) not in acceptable_x_range:
                print('wtf is wrong with you ?')
        user2 = input('Input again x your position 1-3: ')
    clear_output()
    user = int(user)
    user2 = int(user2)
    if user == 1:
        if lst[user2-1] == " ":
            lst[user2-1] = 'X'
        else:
            print('The position is already taken')
            user1_input()
    elif user == 2:
        if lst2[user2-1] == " ":
            lst2[user2-1] = 'X'
        else:
            print('The position is already taken')
            user1_input()
    elif user == 3:
        if lst3[user2-1] == " ":
            lst3[user2-1] = 'X'
        else:
            print('The position is already taken')
            user1_input()
    user2_input()