import json
import re
import requests


# Improvements that can be made:
# - Only make video requests in batches, after up-to-50 video ids are obtained 
#		(string with comma-separated-video-ids)
# - Account for playlists that have more than 50 videos (i.e. nextPageToken(s))
# - Figure out a more efficient way to add durations
# - Account for days/weeks/months in total duration printout
# - To make things more efficent, print out video titles and durations in same loop as original request
# - Change playlist id to be a user input


print("***** Fetching Data From A Youtube Playlist *****")


api_key = "YOUR_API_CODE"		# *** update with your own API key! ***
playlist_id = "PLAzDHex22XQz25EiHGjLPATj1C2ScT-hx"		# this will need to be changed to an argument
max_results = 3											# change this to be hardcoded into the params
														# 	Remember: 50 is max. Default is 5

playlist_parameters = {'key': api_key, 'playlistId': playlist_id, 'maxResults': str(max_results), 'part': 'snippet'}
playlist_response = requests.get('https://www.googleapis.com/youtube/v3/playlistItems', params=playlist_parameters)
playlist_data = playlist_response.json()		# Sidenote: same as 'json.loads(response.content)', via the json module


video_titles, video_ids, video_durations = []
total_time = {'hours': 0, 'minutes': 0, 'seconds': 0}


for item in playlist_data['items']:
	video_titles.append(item['snippet']['title'])
	video_ids.append(item['snippet']['resourceId']['videoId'])


videos_parameters = {'key': api_key, 'id': ','.join(video_ids), 'part': 'contentDetails'}
videos_response = requests.get('https://www.googleapis.com/youtube/v3/videos', params=videos_parameters)
videos_data = videos_response.json()

# **** For testing purposes: ****
with open('videos_data.json', 'w', encoding='utf-8') as f:
    json.dump(videos_data, f, ensure_ascii=False, indent=4)
# *******************************

for item in videos_data['items']:
	video_duration = item['contentDetails']['duration']
	video_durations.append(video_duration)

	video_duration_re = re.search(r'^PT(.*?H)?(.*?M)?(.*?S)?', video_duration)
	hours = video_duration_re.group(1)
	minutes = video_duration_re.group(2)
	seconds = video_duration_re.group(3)

	if hours: total_time['hours'] += int(hours[:-1])
	if minutes: total_time['minutes'] += int(minutes[:-1])
	if seconds: total_time['seconds'] += int(seconds[:-1])

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










