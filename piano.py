import pyautogui
import time
import random
import json
from colorama import Fore, Style, init

init(autoreset=True)

# Enable pyautogui failsafe (move mouse to corner to stop)
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01  # Minimum pause between pyautogui calls

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW,
          Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]


def load_songs(filename="songs.json"):
    try:
        with open(filename, 'r') as file:
            songs = json.load(file)
        return songs
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return {}
    except json.JSONDecodeError:
        print("Error: failed to parse JSON file.")
        return {}


def colorize(note):
    return random.choice(colors) + note + Style.RESET_ALL


def play_chord(notes):
    colored_notes = "".join([colorize(note) for note in notes])
    print(f"playing chord: {colored_notes}")
    try:
        pyautogui.hotkey(*notes)
    except Exception as e:
        print(f"Error playing chord: {e}")


def type_sequence(sequence, song_name, delay=0.15):

    fast_songs = ["Rush E", "Flight of BumbleBee",
                  "Golden Hour", "Interstellar", "Moonlight 3rd Movement", "Vivaldi 3", "Thousands Miles", "Dancing in The Moonlight", "Polish Cow", "Sweater", "La Campanella", "Gravity Falls", "Super Mario Theme Song", "In the Hall of the Mountain", "The Office", "Runaway", "Set Fire to the Rain", "Halo", "Nocture C Choppin", "Riptide"]
    speed_factor = 0.04 if song_name in fast_songs else delay

    for part in sequence:
        if "[" in part and "]" in part:
            # Handle chord
            chord = part.strip("[]")
            play_chord(list(chord))
            time.sleep(speed_factor)
        elif '|' in part:
            # Handle rest
            print("Rest...")
            time.sleep(speed_factor * 2)
        else:
            # Handle individual notes
            for char in part:
                if char.strip():  # Skip whitespace
                    print(f"Typing: {colorize(char)}")
                    try:
                        pyautogui.press(char)
                    except Exception as e:
                        print(f"Error pressing key '{char}': {e}")
                    time.sleep(speed_factor)


def play_song(songs, song_name):
    if song_name not in songs:
        print(f"song '{song_name}' not found in the loaded songs.")
        return

    print(f"\nNow playing: {song_name}\n")
    try:
        for seq in songs[song_name]:
            print(f"processing sequence: {seq}")
            type_sequence(seq.split(), song_name, delay=0.15)
            time.sleep(0.2)  # Reduced from 0.3 for less lag between sequences
    except KeyboardInterrupt:
        print("\n\nPlayback stopped by user!")
        return


def song_selector(songs):
    print("select a song by entering a number:")
    song_names = list(songs.keys())
    for index, song in enumerate(song_names, start=1):
        print(f"{index}. {song}")

    while True:
        try:
            choice = int(input("enter your choice: ")) - 1
            if 0 <= choice < len(song_names):
                return song_names[choice]
            else:
                print("bad choice. please try again.")
        except ValueError:
            print("bad input. please enter a number.")


def select_screen(song_name):
    print(f"\nYou selected: {song_name}")
    print("what would you like to do next?")
    print("1. start Song")
    print("2. go Back to songs")
    print("3. quit")

    while True:
        try:
            option = int(input("enter your choice: "))
            if option == 1:
                return "start"
            elif option == 2:
                return "back"
            elif option == 3:
                return "quit"
            else:
                print("bad choice. please select a valid option.")
        except ValueError:
            print("bad input. please enter a number.")


if __name__ == "__main__":
    songs = load_songs("songs.json")
    if not songs:
        print("no songs loaded. exiting the program.")
        exit()

    while True:
        selected_song = song_selector(songs)
        action = select_screen(selected_song)

        if action == "start":
            print(
                "\nchoose a window, starting in 2 seconds")
            time.sleep(2)
            play_song(songs, selected_song)
        elif action == "back":
            continue
        elif action == "quit":
            print("byeeee")
            break
