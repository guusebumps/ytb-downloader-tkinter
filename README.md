
# YouTube Video and Audio Downloader

This Python script allows users to download YouTube videos or audio (MP3) using a simple graphical user interface (GUI) built with Tkinter.

## Features
- Download YouTube videos in the highest available resolution.
- Convert YouTube videos to MP3 audio.
- Choose the destination folder for downloaded files.
- User-friendly interface using Tkinter.

## Requirements

- Python 3.x
- Libraries:
  - pytube
  - tkinter (usually pre-installed with Python)

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/guusebumps/youtube-downloader.git
   ```

2. Navigate to the project directory:

   ```
   cd youtube-downloader
   ```

3. Install the required Python packages:

   ```
   pip install pytube
   ```

## Usage

1. Run the script:

   ```
   python youtube_downloader.py
   ```

2. Enter the URL of the YouTube video you want to download.

3. Select whether you want to download the video or convert it to audio (MP3).

4. Choose the destination folder where the file will be saved.

5. Click "Download" to start the process.

## Notes

- For audio downloads, the script will automatically convert the downloaded file to `.mp3` format.
- Make sure you have a stable internet connection for downloading videos.
