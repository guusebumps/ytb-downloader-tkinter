
# YouTube Video and Audio Downloader

This Python script provides a simple graphical interface for downloading YouTube videos and converting them to MP3 files with various quality options. It uses the `yt-dlp` library for handling video downloads and `tkinter` for the graphical interface.

## Features
- Download YouTube videos in MP4 format (best available resolution).
- Convert YouTube videos to MP3 format with the following quality options: 64K, 128K, 192K, 256K, 320K.
- Graphical interface for easy interaction and input.

## Requirements

- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - You can install it using pip:
  ```bash
  pip install yt-dlp
  ```
- [FFmpeg](https://ffmpeg.org/download.html) - Required for MP3 conversion.
  - On Windows, download FFmpeg, extract it, and set the path in the system environment variables, or specify the path in the script.

## Installation

1. Clone the repository or download the script.
2. Make sure you have Python installed.
3. Install the required libraries by running:
   ```bash
   pip install yt-dlp
   ```
4. Download and install FFmpeg, if you're converting videos to MP3.

## Running the Script

1. Open a terminal or command prompt.
2. Run the script:
   ```bash
   python youtube_downloader.py
   ```
3. A graphical interface will open where you can paste the YouTube video URL, choose the format (Video or MP3), and select the download location.

## Notes

- If you encounter an error regarding FFmpeg not being found, make sure to install FFmpeg and either set the path in your system's environment variables or specify the path in the script.
- The script is compatible with Windows, macOS, and Linux.

