information = {}


while True:
    def input_error(func):
        def inner():
            try:
                func()
            except KeyError:
                print("Enter the command and the user name and it's phone")
            except IndexError:
                print("Enter the command and the user name and it's phone")
            except ValueError:
                print("Enter the command and the user name and it's phone")
        return inner

    command = input()

    end_list = ["good bye", "close", "exit"]

    if command.lower() in end_list:
        print("Goodbye")
        break

    def say_hello():
        print("How can I help you?")

    def add():
        global information
        information[command.split(" ")[1]] = command.split(" ")[2]
        return information

    def show_all():
        print(information)

    def change():
        information[command.split(" ")[1]] = command.split(" ")[2]

    def phone():
        print(information[command.split(" ")[1]])

    commands = {"hello": say_hello, "add": add,
                "show": show_all, "change": change,
                "phone": phone}

    def get_handler(comm):
        return commands[comm]

    @input_error
    def main():
        get_handler(command.split(" ")[0].lower())()

    if __name__ == "__main__":
        main()
