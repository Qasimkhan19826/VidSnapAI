# 🎬 VidSnapAI

VidSnapAI is an AI-powered reel generator built with Python and Flask. It allows users to upload multiple images or video files and provide text that can be converted into speech. The uploaded media and generated audio are then processed to create a short vertical reel.

## 📌 About The Project

VidSnapAI is designed to simplify the process of creating short-form video reels.

The user can:

- Upload multiple media files
- Enter text for the reel
- Convert the entered text into speech using ElevenLabs
- Store uploaded files using a unique ID
- Generate audio from the provided text
- Process images/videos and audio using FFmpeg
- Generate the final reel in MP4 format

The project mainly focuses on learning and implementing **Python, Flask, file handling, API integration, FFmpeg and backend processing** in a practical application.

## 🚀 Main Features

- 📁 Multiple file uploads
- 🔐 Unique folder creation for each reel
- 📝 Text input for voice generation
- 🗣️ Text-to-Speech using ElevenLabs API
- 🎵 Automatic audio generation
- 🎬 Reel generation using FFmpeg
- 📱 Vertical 1080 × 1920 reel format
- 💾 Local file storage
- ⚙️ Backend processing with Flask
- 🖥️ Simple web interface

## 🛠️ Technologies & Functions Used

### Python

Python is used as the main programming language for the backend and processing logic.

Python concepts used in the project include:

- Functions
- File handling
- `os` module
- `uuid`
- String formatting
- Loops
- Conditional statements
- Dictionaries
- Exception/error handling
- Working with external APIs
- Running system commands

### Flask

Flask is used to create the web application and handle backend requests.

The project uses Flask for:

- Creating routes
- Handling GET and POST requests
- Receiving uploaded files
- Receiving text input from forms
- Rendering HTML templates
- Connecting the frontend with backend logic

Main routes include:

```text
/
 /create
 /gallery
