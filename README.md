# Automatically playing Virtual Piano

This project allows you to automate playing songs on a virtual piano using Python and `pyautogui`. You can load a song from a JSON file, select it, and watch the script type it out on the virtual piano for you. The script also provides colorized output of the notes, making it visually engaging.

---

## Table of Contents
- [Automatically playing Virtual Piano](#automatically-playing-virtual-piano)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation \& Download](#installation--download)
  - [Finding Sheets](#finding-sheets)
  - [Run the script:](#run-the-script)
  - [Adding a song:](#adding-a-song)
  - [Supported Songs:](#supported-songs)

---

## Features
- **Load Songs from JSON**: Load songs from a pre-defined `songs.json` file.
- **Song Selection Menu**: Choose from a list of available songs.
- **Adjustable Typing Speed**: Automatically adjusts typing speed for faster songs.
- **Real-Time Colorized Output**: Displays colorized notes for visual feedback.
- **Supports Chords and Rests**: Can handle chord sequences and rests within a song.
- **Easily Configurable**: Modify the JSON file to add new songs.

## Requirements
- **Python 3.x**
- **pyautogui library**
- **colorama library**

## Installation & Download
Clone or Download Repo
```bash
git clone https://github.com/ivoinestrachan/Play-Virtual-Piano
```
```bash
cd Play-Virtual-Piano
```

## Finding Sheets
[Virtual piano Sheet](https://virtualpiano.net/music-sheets/)

You can install the required libraries using:
```bash
pip install pyautogui colorama
```

## Run the script:
```bash
pip piano.py
```

## Adding a song:
```JSON
{
    "Song Name 1": [
        "C D E F G",
        "[C E G] [D F A] [E G B]",
        "|",
        "C D E"
    ],
    "Song Name 2": [
        "A B C D",
        "|",
        "[A C E]"
    ]
}
```

## Supported Songs:
- Myler's
- Naruto
- Runaway
- I'm Not the Only One
- Minecraft Wet Hands
- Super Mario Theme Song
- Golden Hour
- Little Do You Know
- Vilvadi Winter
- Nocturne
- Moonlight
- Flight of the BumbleBee
- Undertale
- Nocturne C Sharp
- Interstellar
- Waltz
- Mozart Lacrimosa
- Moonlight 3rd Movement
- Waltz in A Minor
- Rick
- See You Again
- Dr Dre
- Vivaldi 2
- Marry You
- Rush E
- Anthem
- Stay With Me
- Tones and I
- Happier



