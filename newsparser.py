# Latest News	https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml
# Asia	https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=6511
# Business	https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=6936
# Singapore	https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=10416
# Sport	https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=10296
# World	https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=6311
# Today	https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=679471

import threading
import time
import feedparser
from gpt4all import GPT4All
from transformers import AutoProcessor, BarkModel
import pygame  
import numpy as np
import nltk

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')
    nltk.download('punkt')

list_of_news = []

def fetch_rss_data(url):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        news = []
        news.append(entry.title +" "+ entry.summary)
        list_of_news.append(news)

rss_feed_urls = [
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml",
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=10416",
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=6311"
]

def generate_long_audio(text, processor, model, voice_preset):
    text = text.replace("\n", " ").strip()
    sentences = nltk.sent_tokenize(text)
    
    pieces = []
    print(f"--- Generating audio for {len(sentences)} sentences ---")
    
    for sentence in sentences:
        print(f"Generating: {sentence}")
        inputs = processor(sentence, voice_preset=voice_preset)
        
        audio_array = model.generate(**inputs)
        audio_array = audio_array.cpu().numpy().squeeze()
        
        silence = np.zeros(int(24000 * 0.25))
        
        pieces.append(audio_array)
        pieces.append(silence)
        
    return np.concatenate(pieces)

def initialization():
    for url in rss_feed_urls:
        fetch_rss_data(url)

    text_model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")

    pygame.mixer.init(frequency=24000, size=-16, channels=1)
    processor = AutoProcessor.from_pretrained("suno/bark")
    audio_model = BarkModel.from_pretrained("suno/bark")

    voice_preset = "v2/en_speaker_6"

    return text_model, processor, audio_model, voice_preset

    
def main(): 
    text_model, processor, audio_model, voice_preset = initialization()
    with text_model.chat_session():
            script = text_model.generate(f"Immediately talk like a dj news caster and report these news. {list_of_news[:1]}. Start with a welcome back greeting as you have already started airing. Your name is DJ Clanker and you're hosting on Clanker Radio", max_tokens=1024)        
            print(f"\nDJ Script:\n{script}\n")
            
            full_audio_array = generate_long_audio(script, processor, audio_model, voice_preset)

            audio_data = (full_audio_array * 32767).astype(np.int16)
            sound = pygame.sndarray.make_sound(audio_data)
            channel = sound.play()

            while channel.get_busy():
                pygame.time.wait(100) 


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n--- Program Stopped by User ---")