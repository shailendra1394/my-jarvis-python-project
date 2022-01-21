import datetime
import os
import random
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio_string):
    engine.say(audio_string)
    engine.runAndWait()


def wish():
    hour = datetime.datetime.now().hour
    if 0 < hour < 12:
        speak("Hello good morning")
    elif 12 <= hour < 16:
        speak("Hello good afternoon")
    else:
        speak("hello good evening")
    speak('i am your assistant, how may i help you?')


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')

    except Exception as e:
        print(e)
        print('Say that again...')
        return "None"
    return query


if __name__ == '__main__':
    wish()
    while True:
        query = take_command().lower()
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        if "wikipedia" in query:
            print('Reading on wikipedia...')
            query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak('According tp wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open('youtube.com')

        elif 'open google' in query:
            webbrowser.get(chrome_path).open('google.com')

        elif 'play music' in query or 'play some music' in query:
            music_dir = 'F:\groove music\dansonn beats'
            songs = os.listdir(music_dir)
            print(songs)
            i = random.randint(0, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[i]))  # exact path of particular song.

        elif "what's the time" in query:
            str_time = datetime.datetime.now().strftime("%H Hours %M Minutes and %S Seconds")
            print(str_time)
            speak('right now it is' + str_time)
