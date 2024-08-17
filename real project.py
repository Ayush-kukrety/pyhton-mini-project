import os
import moviepy.editor as mp 
import speech_recognition as sr 
from googletrans import Translator


# Load the video 
video = mp.VideoFileClip(r"C:\Users\acrer\Desktop\New folder\Drake - One Dance (Lyrics) ft. Wizkid & Kyla.mp4")

# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile("Drake - One Dance (Lyrics) ft. Wizkid & Kyla.wav")

# Initialize recognizer 
r = sr.Recognizer()

# Load the audio file 
with sr.AudioFile("Drake - One Dance (Lyrics) ft. Wizkid & Kyla.wav") as source: 
    data = r.record(source) 

# Convert speech to text 
text = r.recognize_google(data)

# Print the text 
print("\nThe resultant text from video is: \n") 
print(text)

# Initialize Googletrans translator 
translator = Translator()

# Translate the text to Spanish (es)
translated_text = translator.translate(text, dest="es")

# Print the Spanish translation
print("\nThe text translated to Spanish is: \n") 
print(translated_text.text)
