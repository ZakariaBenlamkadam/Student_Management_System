import tkinter as tk
import os
import shutil
from tkinter import filedialog

# List of tuples containing book name and PDF file path
books = [("Deep work rules :", "Book.pdf"),
         ("Java for begginers", "book2.pdf"),
         ("Visualization Analysis and Design ", "book3.pdf")]

# Function to handle download button press
def download_book(file_path):
    # Get the user's selected directory
    directory = filedialog.askdirectory()
    if directory:
        # Set the path for the downloaded file
        dest_path = os.path.join(directory, os.path.basename(file_path))
        # Copy the PDF file to the selected directory
        shutil.copyfile(file_path, dest_path)

# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.title("Book Downloader")

# Add a label to the window
label = tk.Label(root, text="Click a button below to download a book.")
label.pack(pady=10)

# Create labels and buttons for each book
for book in books:
    # Add a label with the book name
    label = tk.Label(root, text=book[0])
    label.pack(pady=5)
    # Add a download button for the book
    button = tk.Button(root, text="Download", command=lambda file_path=book[1]: download_book(file_path))
    button.pack()

# Start the GUI loop
root.mainloop()
