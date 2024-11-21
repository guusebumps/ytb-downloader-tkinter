import os
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def download_media():
    url = url_entry.get()
    save_path = filedialog.askdirectory()
    
    if not url or not save_path:
        messagebox.showwarning("Input Error", "Please provide a valid URL and select a save location.")
        return

    ydl_opts = {}

    if download_type.get() == "Video":
        ydl_opts = {
            'format': 'bestvideo+bestaudio',
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        }
    elif download_type.get() == "MP3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(save_path, '%(title)s.mp3'),
            'ffmpeg_location': r'C:\ffmpeg\bin',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality.get()
            }]
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Download Complete", "The file has been downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Download Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("YouTube Downloader")

tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

download_type = tk.StringVar(value="Video")
tk.Radiobutton(root, text="Download Video", variable=download_type, value="Video").grid(row=1, column=0, padx=10, pady=5)
tk.Radiobutton(root, text="Download MP3", variable=download_type, value="MP3").grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="MP3 Quality (kbps):").grid(row=2, column=0, padx=10, pady=5)
quality = tk.StringVar(value="256")
# quality = tk.StringVar(value="320")
quality_options = tk.OptionMenu(root, quality, "64", "128", "192", "256", "320")
quality_options.grid(row=2, column=1, padx=10, pady=5)

download_button = tk.Button(root, text="Download", command=download_media)
download_button.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
