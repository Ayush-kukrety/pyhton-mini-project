import os
from moviepy.editor import VideoFileClip

import speech_recognition as sr
from googletrans import Translator

def transcribe_audio(path):
    """
    Transcribe audio file to text using Google Speech Recognition.
    """
    r = sr.Recognizer()

    with sr.AudioFile(path) as source:
        audio = r.record(source)

    try:
        return r.recognize_google(audio)
    except Exception as e:
        print(f"Error during recognition: {e}")
        return None

def video_to_text(video_path, output_language="en"):
    """
    Convert video to text using Google Speech Recognition and Google Translate.
    """
    translator = Translator()
    translations = []

    # Extract audio from video
    video_clip = VideoFileClip(video_path)
    audio = video_clip.audio

    # Write audio to temporary file
    audio.write_audiofile("temp_audio.wav")

    # Transcribe audio
    text = transcribe_audio("temp_audio.wav")

    if text:
        # Translate text to specified language
        translated_text = translator.translate(text, dest=output_language)
        translations.append(translated_text.text)

        # Add additional languages if needed
        translations.append(translator.translate(text, dest="fr").text)
        translations.append(translator.translate(text, dest="de").text)

        # Print all translations
        for translated in translations:
            print(translated)

        return translations
    else:
        return None

if __name__ == "__main__":
    video_path = r"C:\\Users\acrer\Desktop\New folder\Drake - One Dance (Lyrics) ft. Wizkid & Kyla.mp4"
    output_text = video_to_text(video_path)