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

  # Add a label for the artist name input
  artist_name_label = tk.Label(text="Artist Name(s):")
  artist_name_label.grid(row=1, column=0)

  # Add an entry for the artist name input
  artist_name_entry = tk.Entry()
  artist_name_entry.grid(row=1, column=1)

  # Add a label for the song name input
  song_name_label = tk.Label(text="Song Name(s):")
  song_name_label.grid(row=2, column=0)

  # Add an entry for the song name input
  song_name_entry = tk.Entry()
  song_name_entry.grid(row=2, column=1)

  # Add a button to start the download
  download_button = tk.Button(text="Download", command=rip_audio_files)
  download_button.grid(row=3, column=0)

  # Start the GUI
  window.mainloop()

def rip_audio_files():
  # Get the URL from the input
  url = url_entry.get()

  # Get the artist names from the input
  artist_names = artist_name_entry.get().split(",")

  # Get the song names from the input
  song_names = song_name_entry.get().split(",")

  # Make a request to the website and get the HTML response
  response = requests.get(url)

  # Parse the HTML response with Beautiful Soup
  soup = BeautifulSoup(response.content, "html.parser")

  # Find the audio file links in the HTML
  audio_links = soup.find_all("a", href=re.compile(r"\.mp3$"))

  # Download the audio files
  for audio_link in audio_links:
    audio_url = audio_link["href"]
    for artist_name, song_name in zip(artist_names, song_names):
      with open(f"{artist_name} - {song_name}.mp3", "wb") as f:
        f.write(requests.get(audio_url).content)

if __name__ == "__main__":
  main()
