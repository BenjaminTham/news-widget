<h1 align="center" id="title">📰 News RSS Parser Widget</h1>

<p id="description">This is a simple lightweight Python project that puts a sleek modern news feed right on your desktop. It's designed to be unobtrusive helpful and a little bit cool. It floats on your screen is semi-transparent and gives you the latest headlines from Singapore's top news sources at a glance.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Sleek Modern UI: Built with CustomTkinter for a clean modern look.
*   Frameless & Draggable: Just click and drag the text to move the window anywhere you like.
*   Semi-Transparent: The window has a 90% opacity so it blends nicely with your desktop without being distracting.
*   Live News: Fetches the latest headlines from Channel News Asia (CNA) & The Straits Times (ST)
*   Easy to Read: Headlines publish dates and summaries are color-coded for clarity.
*   Lightweight: Uses minimal system resources.
*   Simple Controls: Just press the Escape key to close the app.

<h2>🛠️ Installation Steps:</h2>

<p>1. Make sure you have Python 3 installed on your system.</p>

<p>2. Clone the Repository</p>

```
git clone https://github.com/BenjaminTham/news-widget.git 
```

<p>3. cd to the repo</p>

```
cd news-widget
```

<p>4. This project relies on a couple of great libraries. You can install them using pip:</p>

```
pip install customtkinter feedparser
```

<p>5. That's it! Just run the Python script:</p>

```
python newsparser.py
```

<h3> Want to package this into a single standalone executable file for Windows? No problem! We can use pyinstaller for that.</h3>

<p>1. Install PyInstaller:</p>

```
pip install pyinstaller
```

<p>2. Run the Build Command: Open your terminal in the project directory and run this command:</p>

```
pyinstaller --onefile --windowed newsparser.py
```

--onefile: Bundles everything into a single .exe.</p>

--windowed: Prevents the black console window from opening when you run the app.</p>

<p>3. Find Your App: PyInstaller will create a dist folder. Inside you'll find your brand new newsparser.exe! You can share this file with friends (who use Windows) and they can run it without installing Python.</p>


<h2>🤖 What's Next? The AI Radio DJ!</h2>

The next big idea is to transform it from a silent news reader into a fully-fledged AI Radio DJ! Like the one made by Spotify. So all you gotta do is tune into the news feed

*   AI Chatbot: Integrate a chatbot to interact with you.
*   AI Voice Generator: Instead of you reading the news, an AI voice will tell you the news, just like a radio host.
*   Music Player: The "DJ" will also play your favorite music tracks between news segments.

<h2>🙏 Acknowledgements</h2>

This project stands on the shoulders of giants. A huge thank you to:

CustomTkinter: For making it so easy to create beautiful, modern GUIs in Python.

feedparser: For doing the heavy lifting of parsing all those RSS feeds.

Channel News Asia & The Straits Times: For providing the high-quality news feeds.
