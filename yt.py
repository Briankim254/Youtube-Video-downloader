import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

class VideoDownloader:
    def __init__(self, master):
        self.master = master
        master.title("Video Downloader")

        self.url_label = tk.Label(master, text="Enter video URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.pack()

        self.save_label = tk.Label(master, text="Select save location:")
        self.save_label.pack()

        self.save_button = tk.Button(master, text="Browse", command=self.browse_directory)
        self.save_button.pack()

        self.download_button = tk.Button(master, text="Download", command=self.download_video)
        self.download_button.pack()

    def browse_directory(self):
        save_dir = filedialog.askdirectory()
        if save_dir:
            self.save_label.config(text=f"Save location: {save_dir}")
            self.save_location = save_dir

    def download_video(self):
        url = self.url_entry.get()
        if url:
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').first()
            video.download(self.save_location)
            tk.messagebox.showinfo("Success", "Video downloaded successfully!")
        else:
            tk.messagebox.showerror("Error", "Please enter a valid video URL")

root = tk.Tk()
app = VideoDownloader(root)
root.mainloop()
