information = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            if func == phone:
                return "Please enter the name whose number ypu want to see"
            return "Please enter name and phone number"
        except ValueError:
            return "Wrong input"
        except TypeError:
            return "Wrong input"
        except KeyError:
            return "Wrong input"

    return inner


def say_hello():
    return "How can I help you?"


@input_error
def add(data):
    name = data.strip().split(" ")[1]
    phone = data.strip().split(" ")[2]

    if name in information:
        return f"{name} already has a number, call change function"

    elif not phone.isnumeric():
        return f"{phone} isn't a right input,enter a numeric one"

    else:
        information[name] = phone
        return f"User {name} with {phone} was added."


def show_all():
    return information


@input_error
def phone(data):
    name = data.strip().split(" ")[1]

    if name not in information:
        return f"{name} doesn't have a number, call 'add' command to add this user"
    else:
        return information[name]


@input_error
def change(data):
    name = data.strip().split(" ")[1]
    phone = data.strip().split(" ")[2]

    if name not in information:
        return f"{name} doesn't have a number, call 'add' command to add this user"
    elif not phone.isnumeric():
        return f"{phone} isn't a right input,enter a numeric one"
    else:
        information[name] = phone
        return f"{name}'s phone number was changed to {phone}"


COMMANDS = {"hello": say_hello,
            "add": add,
            "phone": phone,
            "change": change,
            "show all": show_all}


def handler(comm):
    return COMMANDS[comm]


def main():
    while True:
        user_command = input("Enter a command: ")

        if user_command.lower() == "hello" or user_command.lower() == "show all":
            print(handler(user_command.lower())())

        elif user_command.split(" ")[0].lower() not in ["change", "phone", "add", "exit", "close", "goodbye"]:
            print("No such a command")

        elif user_command.lower() in ["exit", "close", "goodbye"]:
            print("Goodbye")
            break
        else:
            print(handler(user_command.split(" ")[0].lower())(user_command))


if __name__ == "__main__":
    main()
