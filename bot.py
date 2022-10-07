information = {}
while True:
    def input_error(func):
        def inner():
            try:
                func()
            except KeyError:
                print("Enter the name of the user whose number you want to change")
            except IndexError:
                print("Enter the name and the phone with space between them")
        return inner

    command = input()

    end_list = ["good bye", "close", "exit"]

    if command.lower() in end_list:
        print("Goodbye")
        break

    def say_hello():
        print("How can I help you?")

    @input_error
    def add():
        global information
        dict_1 = {command.split(" ")[1]: command.split(" ")[2]}
        return information.update(dict_1)

    def show_all():
        print(information)

    @input_error
    def change():
        information[command.split(" ")[1]] = command.split(" ")[2]

    @input_error
    def phone():
        print(information[command.split(" ")[1]])

    commands = {"hello": say_hello, "add": add,
                "show": show_all, "change": change,
                "phone": phone}

    def get_handler(comm):
        return commands[comm]

    try:
        get_handler(command.split(" ")[0].lower())()
    except KeyError:
        print("Please enter command")
