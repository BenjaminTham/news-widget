import feedparser
from customtkinter import *

def on_drag_start(event):
    widget = event.widget.winfo_toplevel()
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget.winfo_toplevel()
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.geometry(f"+{x}+{y}")

def close_app(event=None):
    root.destroy()

rss_feed_urls = [
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml",
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=6511",
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=6936",
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=10416",
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=10296",
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=6311",
    "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=679471",
    "https://www.straitstimes.com/news/singapore/rss.xml",
    "https://www.straitstimes.com/news/asia/rss.xml",
    "https://www.straitstimes.com/news/world/rss.xml",
    "https://www.straitstimes.com/news/opinion/rss.xml",
    "https://www.straitstimes.com/news/life/rss.xml",
    "https://www.straitstimes.com/news/business/rss.xml",
    "https://www.straitstimes.com/news/sport/rss.xml",
    "https://www.straitstimes.com/news/multimedia/rss.xml",
    "https://www.straitstimes.com/news/newsletter/rss.xml"

]
root = CTk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"800x{screen_height}")
root.attributes("-alpha", 0.9)

root.overrideredirect(True)

text_widget = CTkTextbox(root, 
                         wrap="word", 
                         font=("Arial", 14), 
                         fg_color="transparent") 

text_widget.pack(fill="both", expand=True, padx=10, pady=10)

text_widget.bind("<Button-1>", on_drag_start)
text_widget.bind("<B1-Motion>", on_drag_motion)
root.bind("<Escape>", close_app)

text_widget.tag_config("title_style", 
                       foreground="#00AEEF") 

text_widget.tag_config("published_style", 
                       foreground="gray")

text_widget.tag_config("summary_style", 
                       foreground="white") 

text_widget.tag_config("separator_style", 
                       foreground="#444444")

for url in rss_feed_urls:
    feed = feedparser.parse(url)

    for entry in feed.entries:
        text_widget.insert(END, f"TITLE: {entry.title}\n", "title_style")
        text_widget.insert(END, f"Published: {entry.published}\n", "published_style")
        text_widget.insert(END, f"Summary: {entry.summary}\n", "summary_style")
        text_widget.insert(END, "-" * 80 + "\n\n", "separator_style")

text_widget.configure(state=DISABLED)

root.mainloop()