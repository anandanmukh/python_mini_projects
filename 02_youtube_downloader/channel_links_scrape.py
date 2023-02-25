import requests
from bs4 import BeautifulSoup

channel_name = input("Enter the channel id: ")

# Replace "channel-name" with the actual name of the YouTube channel
url = f"https://www.youtube.com/{channel_name}/videos"

print(url)

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")
# Find all video elements on the page
videos = soup.find_all("a", {"class": "yt-uix-tile-link"})

# Print the links of all videos
for video in videos:
  print(video["href"])

'''scrape all the links off a youtube channel'''


