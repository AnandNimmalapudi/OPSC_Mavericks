import csv
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials

# Set up API credentials
api_key = 'AIzaSyDtz1Jxn2KwMRBA282sLPingrY2uOXqnC0'
api_service_name = 'youtube'
api_version = 'v3'

# Create a YouTube API client
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

# Specify the video ID for the comments you want to extract
video_id = 'UP1tWImU_b8'

# Request comments for the specified video
request = youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    textFormat='plainText'
)
response = request.execute()

# Extract comments
comments_data = []

for comment in response['items']:
    snippet = comment['snippet']['topLevelComment']['snippet']
    author = snippet['authorDisplayName']
    text = snippet['textDisplay']
    comments_data.append([author, text])

# Save comments to CSV file
csv_file_path = 'youtube_comments.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Author', 'Comment'])

    for comment_data in comments_data:
        csv_writer.writerow(comment_data)

print(f'Comments have been saved to {csv_file_path}')
