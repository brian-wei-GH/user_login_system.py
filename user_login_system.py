def register():
    while True:
        line_list = []
        re_name = True
        user_name = input("Enter your name: ")
        with open("user_login_system.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if user_name.upper() == "Q":
                    return
                if user_name == parts[0]:
                    print("Username is already taken")
                    re_name = False
        if re_name == True:
            user_psw = input("Enter your password: ")
            user_data = "{},{}\n".format(user_name, user_psw)

            with open("user_login_system.txt", "a") as file:
                file.write(user_data)


def login():
    while True:
        user_n_log = input("Enter your name: ")
        if user_n_log.upper() == "Q":
            break
        with open("user_login_system.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if user_n_log == parts[0]:
                    print("please {} to enter your password".format(user_n_log))
                    while True:
                        user_n_psw = input("Enter your password: ")
                        if user_n_psw.upper() == "Q":
                            print("please re-enter your name")
                            break
                        if user_n_psw == parts[1]:  # will find all psw, not match the same one
                            print("welcome {} to login".format(user_n_log))
                            return
                        else:
                            print("wrong password")
            print("wrong name")


def show_users():
    line_list = []
    with open("user_login_system.txt", "r") as file:
        for line in file:
            parts = line.strip().split(',')
            line_list.append(parts)
            line_list.sort()
        for line_sort in line_list:
            line_str = "{},{}\n".format(line_sort[0], line_sort[1])
            line_str = line_str.strip()
            print(line_str)


def clear_file():
    with open("user_login_system.txt", "w") as file:
        file.write("user,password\n")

FUNC_LIST = {
        "1": register,
        "2": login,
        "3": show_users,
        "4": clear_file
    }
while True:
    SELECT_LIST = ["1", "2", "3", "4"]
    USER_SELECT = input("Enter your choice: 1.register 2.login 3.show users 4.clear file q.exist ")
    if USER_SELECT.upper() == "Q":
        break
    if USER_SELECT not in SELECT_LIST:
        print("wrong choice")
    else:
        FUNC_LIST[USER_SELECT]()
