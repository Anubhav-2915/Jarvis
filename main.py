from search import search_open
from weather import weather
from time_module import get_date
from time_module import get_time
from playmusic import run_music

def command_handler(command):
    command = command.lower()

    if "open" in command:
        query = command.replace("open","").strip()
        search_open(query)

    elif "weather" in command:
        weather()

    elif "time" in command or "date" in command:
        print("Today is: ", get_date())
        print("it's ",get_time(),"right now!!")

    elif "play" in command or "song" in command or "music" in command:
        run_music();

    else:
        print("Command not recognised!!")


if __name__ == "__main__":
    user_input = input("Hello Boss! What shall I do for you today: ")
    print("Ok Boss!!")
    command_handler(user_input)