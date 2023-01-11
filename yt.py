import pytube as pt
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Create a window
window = tk.Tk()
window.title("Youtube Video Downloader")
window.geometry("500x300")
window.resizable(False, False)

# Create a function to download the video
def download():
    try:
        # Get the link of the video
        link = linkEntry.get()
        # Get the path to save the video
        savePath = pathEntry.get()
        # Create a youtube object
        yt = pt.YouTube(link)
        # Get the video stream
        stream = yt.streams.first()
        # Download the video
        stream.download(savePath)
        # Show a message
        messagebox.showinfo("Success", "Video has been downloaded successfully")
    except Exception as e:
        # Show a message
        messagebox.showerror("Error", e)

# Create a function to select the path
def selectPath():
    