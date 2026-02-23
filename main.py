from search import search_open
from weather import weather
from time_module import get_date
from time_module import get_time

def command_handler(command):
    command = command.lower()

    if "open" in command:
        query = command.replace("open","").strip()
        search_open(query)

    elif "weather" in command:
        weather()

    elif "time" or "date" in command:
        print(get_time())
        print(get_date())

    else:
        print("Command not recognised!!")


if __name__ == "__main__":
    user_input = input("Enter command: ")
    command_handler(user_input)