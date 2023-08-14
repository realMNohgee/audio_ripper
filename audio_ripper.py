import requests
from bs4 import BeautifulSoup
import os
import tkinter as tk

def main():
  # Create the window
  window = tk.Tk()

  # Add a label for the URL input
  url_label = tk.Label(text="URL:")
  url_label.grid(row=0, column=0)

  # Add an entry for the URL input
  url_entry = tk.Entry()
  url_entry.grid(row=0, column=1)

  # Add a label for the artist names and song names input
  artist_and_song_names_label = tk.Label(text="Artist Names and Song Names (Separated by commas):")
  artist_and_song_names_label.grid(row=1, column=0)

  # Add an entry for the artist names and song names input
  artist_and_song_names_entry = tk.Entry()
  artist_and_song_names_entry.grid(row=1, column=1)

  # Add a button to start the download
  download_button = tk.Button(text="Download", command=rip_audio_file)
  download_button.grid(row=2, column=0)

  # Start the GUI
  window.mainloop()

def rip_audio_file():
  # Get the URL from the input
  url = url_entry.get()

  # Get the artist names and song names from the input
  artist_and_song_names = artist_and_song_names_entry.get()

  # Split the artist names and song names into a list
  artist_and_song_names_list = artist_and_song_names.split(",")

  # Download each audio file in the list
  for artist_and_song_name in artist_and_song_names_list:
    artist_name, song_name = artist_and_song_name.split(" - ")

    # Make a request to the website and get the HTML response
    response = requests.get(url)

    # Parse the HTML response with Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the audio file link in the HTML
    audio_link = soup.find("a", href=re.compile(r"\.mp3$"))

    # Get the audio file URL
    audio_url = audio_link["href"]

    # Download the audio file
    response = requests.get(audio_url)

    # Save the audio file to disk
    with open(f"{artist_name} - {song_name}.mp3", "wb") as f:
      f.write(response.content)

if __name__ == "__main__":
  main()
