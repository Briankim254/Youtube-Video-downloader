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
    # Open the file dialog
    path = filedialog.askdirectory()
    # Set the path to the entry
    pathEntry.insert(0, path)

# Create a label
linkLabel = tk.Label(window, text="Enter the link of the video", font=("Arial", 15))

# Create an entry
linkEntry = tk.Entry(window, width=50, font=("Arial", 15))

# Create a label
pathLabel = tk.Label(window, text="Select the path to save the video", font=("Arial", 15))

# Create an entry
pathEntry = tk.Entry(window, width=50, font=("Arial", 15))

# Create a button
selectPathButton = tk.Button(window, text="Select Path", font=("Arial", 15), command=selectPath)

# Create a button
downloadButton = tk.Button(window, text="Download", font=("Arial", 15), command=download)

# Place the widgets
linkLabel.grid(row=0, column=0, pady=10)
linkEntry.grid(row=1, column=0, pady=10)

    