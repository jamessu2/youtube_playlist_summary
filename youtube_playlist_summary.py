import re
import requests

print("***** Fetching Data From A Youtube Playlist *****")

api_key = "YOUR_API_KEY"		# Insert your API key here!
playlist_id = "PLAzDHex22XQz25EiHGjLPATj1C2ScT-hx"		# this will need to be changed to an argument
video_titles, video_ids, video_durations = [], [], []
total_time = {'hours': 0, 'minutes': 0, 'seconds': 0}

# Fetch playlist API data (assuming playlist has less videos than maxResults)
playlist_parameters = {'key': api_key, 'playlistId': playlist_id, 'maxResults': '3', 'part': 'snippet'}
#	Note: for maxResults, Youtube's default is 5, and 50 is the max allowed. 
playlist_response = requests.get('https://www.googleapis.com/youtube/v3/playlistItems', params=playlist_parameters)
playlist_data = playlist_response.json()		# Fyi, same as 'json.loads(playlist_response.content)', via the json module

for item in playlist_data['items']:
	video_titles.append(item['snippet']['title'])
	video_ids.append(item['snippet']['resourceId']['videoId'])

# Fetch video API data for all videos in playlist
videos_parameters = {'key': api_key, 'id': ','.join(video_ids), 'part': 'contentDetails'}
videos_response = requests.get('https://www.googleapis.com/youtube/v3/videos', params=videos_parameters)
videos_data = videos_response.json()

for item in videos_data['items']:
	# Get each video duration
	video_duration = item['contentDetails']['duration']
	video_durations.append(video_duration)

	# Calulate total video time
	video_duration_re = re.search(r'^PT(.*?H)?(.*?M)?(.*?S)?', video_duration)
	hours, minutes, seconds = video_duration_re.groups()
	if hours: total_time['hours'] += int(hours[:-1])
	if minutes: total_time['minutes'] += int(minutes[:-1])
	if seconds: total_time['seconds'] += int(seconds[:-1])

# Print the desired output
for index, (video_title, video_duration) in enumerate(zip(video_titles, video_durations), start=1):
	print(f"Video #{index}:")
	print(f"\t Title: {video_title}")
	print(f"\t Duration: {video_duration}\n")

# Simplify the times
total_time['hours'] += total_time['minutes'] // 60
total_time['minutes'] += total_time['seconds'] // 60
total_time['minutes'] = total_time['minutes'] % 60
total_time['seconds'] = total_time['seconds'] % 60
print(f"Duration of entire playlist = {total_time}\n")


# **** For testing purposes: ****
# with open('videos_data.json', 'w', encoding='utf-8') as f:
#    json.dump(videos_data, f, ensure_ascii=False, indent=4)
# *******************************








