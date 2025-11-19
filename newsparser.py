import feedparser
import os
import customtkinter as ctk
import pygame
from gpt4all import GPT4All
import sys

NEWS_NUMBER = 1
list_of_news = []

rss_feed_urls = [
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml",
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=6311",
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=10416"
]

def fetch_rss_data(url):
    global NEWS_NUMBER
    global list_of_news
    feed = feedparser.parse(url)
    for entry in feed.entries:
        list_of_news.append(f"News {NEWS_NUMBER}: {entry.title} Summary:{entry.summary}")
        NEWS_NUMBER+=1

def clear_console():
    """Clears the console screen."""
    _ = os.system('clear')

def updateLoop():
    global NEWS_NUMBER
    global list_of_news

    clear_console()
    NEWS_NUMBER = 1
    for url in rss_feed_urls:
        fetch_rss_data(url)
    # print(list_of_news)
    app.after(1000, updateLoop)

def play_sound():
    try:
        pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error playing sound: {e}")

model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf", device="cpu")
with model.chat_session():
    print(model.generate(f"Immediately talk like a dj news caster and report these news. {list_of_news[:5]}", max_tokens=1024))


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Hello CustomTkinter")
app.geometry("400x200")
pygame.mixer.init()

frame = ctk.CTkFrame(
    master=app,
    width=200,
    height=200,
    corner_radius=10,
    border_width=2
)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Frame Content")
label.pack(pady=10)

button = ctk.CTkButton(
    master=frame,
    text="Click Me",
    command=play_sound,
    width=120,
    height=32,
    border_width=0,
    corner_radius=8,
    hover=True
)
button.pack(pady=10)

# app.after(1000, updateLoop)
app.mainloop()