A minimalist, borderless desktop GUI application built with Python that parses and displays the latest news headlines from various RSS feeds. It's designed to be a sleek, semi-transparent news ticker that sits on your desktop.

(Optional: Add a screenshot of the application in action here)
![App Screenshot](screenshot.png)

Features

Live News Feeds: Fetches and displays the latest news from multiple sources (currently configured for Channel News Asia and The Straits Times).

Minimalist GUI: Built with customtkinter for a modern look and feel.

Borderless & Transparent: Runs in a borderless, semi-transparent window for an unobtrusive desktop experience.

Draggable Window: Click and drag anywhere on the application to move it around your screen.

Easy Exit: Simply press the Esc key to close the application.

Styled Content: News titles, publication dates, and summaries are styled with different colors for easy readability.

Installation

Clone this repository:

git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name


Install the required Python libraries:

pip install customtkinter feedparser


Usage

To run the application from the source code, simply execute the Python script:

python newsparser.py


Building into an Executable (.exe)

You can package this application into a single, standalone executable file for Windows using pyinstaller.

Install pyinstaller:

pip install pyinstaller


Run the build command from your terminal in the project directory:

# --onefile: Bundles everything into a single .exe
# --windowed: Prevents a console window from opening when you run the .exe
pyinstaller --onefile --windowed newsparser.py


Your executable file will be located in the dist folder that pyinstaller creates.

🚀 Future Plans: The AI Radio DJ

The next major update aims to transform this news reader into a fully interactive "AI Radio DJ". The planned features include:

AI Chatbot Integration: An AI will provide commentary on the news stories, offering summaries or context.

AI Voice Generation: A text-to-speech (TTS) engine will read the news headlines and summaries aloud, just like a radio host.

Music Player: Functionality to play background music, creating a complete and immersive "radio" experience.

License

This project is licensed under the MIT License. (Recommended: You can add a LICENSE file with the MIT License text to your repository).
