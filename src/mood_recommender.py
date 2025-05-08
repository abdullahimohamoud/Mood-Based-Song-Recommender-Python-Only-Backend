import json
import random
import os
import re
import webbrowser

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

def load_songs(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def recommend_songs(songs, mood, num=5):
    mood = mood.lower().strip()
    if mood not in songs:
        return None
    song_list = songs[mood]
    random.shuffle(song_list)
    return song_list[:min(num, len(song_list))]

def extract_mood(user_input, available_moods):
    user_input = user_input.lower()
    for mood in available_moods:
        if re.search(rf'\b{re.escape(mood)}\b', user_input):
            return mood
    return None

def speak_songs(song_list):
    if not TTS_AVAILABLE:
        print("pyttsx3 not installed. Skipping voice output.")
        return
    engine = pyttsx3.init()
    for song in song_list:
        engine.say(song['title'])
    engine.runAndWait()

def main():
    songs_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'songs.json')
    songs = load_songs(songs_file)
    print("\nWelcome to the Mood-Based Song Recommender!\n")
    print(f"Available moods: {', '.join(songs.keys())}")
    user_input = input("Enter your current mood: ").strip().lower()
    mood = extract_mood(user_input, songs.keys())
    if not mood:
        print(f"Sorry, could not detect a valid mood in your input. Try using one of: {', '.join(songs.keys())}")
        return
    recommendations = recommend_songs(songs, mood, num=random.randint(3,5))
    if not recommendations:
        print(f"Sorry, no songs found for mood '{mood}'. Try another mood.")
        return
    print(f"\n🎵 Songs for '{mood}' mood:")
    for idx, song in enumerate(recommendations, 1):
        print(f"  {idx}. {song['title']}\n      Link: {song['url']}")
    open_links = input("\nWould you like to open any of these songs in your browser? (y/n): ").strip().lower()
    if open_links == 'y':
        print("Enter the numbers of the songs to open, separated by commas (e.g., 1,3): ")
        choices = input().strip()
        try:
            indices = [int(x)-1 for x in choices.split(',') if x.strip().isdigit()]
            for i in indices:
                if 0 <= i < len(recommendations):
                    webbrowser.open(recommendations[i]['url'])
        except Exception as e:
            print("Invalid input. No links opened.")
    if TTS_AVAILABLE:
        speak = input("\nWould you like the songs read aloud? (y/n): ").strip().lower()
        if speak == 'y':
            speak_songs(recommendations)
    else:
        print("\n(Install pyttsx3 for voice output: pip install pyttsx3)")

if __name__ == "__main__":
    main()
