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


api_key = "YOUR_API_KEY"		# *** update with your own API key! ***
playlist_id = "PLAzDHex22XQz25EiHGjLPATj1C2ScT-hx"		# this will need to be changed to an argument
max_results = 50											# change this to be hardcoded into the params
														# 	Remember: 50 is max. Default is 5

playlist_parameters = {'key': api_key, 'playlistId': playlist_id, 'maxResults': str(max_results), 'part': 'snippet'}
playlist_response = requests.get('https://www.googleapis.com/youtube/v3/playlistItems', params=playlist_parameters)
playlist_data = playlist_response.json()		# Sidenote: same as 'json.loads(response.content)', via the json module

# For testing purposes:
with open('playlist_data.json', 'w', encoding='utf-8') as f:
    json.dump(playlist_data, f, ensure_ascii=False, indent=4)


playlist_video_titles = []
playlist_video_ids = []
playlist_video_durations = []
total_playlist_time = {
	'hours': 0,
	'minutes': 0,
	'seconds': 0
}


for item in playlist_data['items']:
	video_title = item['snippet']['title']
	video_id = item['snippet']['resourceId']['videoId']

	video_parameters = {'key': api_key, 'id': video_id, 'part': 'contentDetails'}
	video_response = requests.get('https://www.googleapis.com/youtube/v3/videos', params=video_parameters)
	video_data = video_response.json()
	video_duration = video_data['items'][0]['contentDetails']['duration']

	playlist_video_titles.append(video_title)
	playlist_video_ids.append(video_id)
	playlist_video_durations.append(video_duration)


	# ******** Need to edit this section to account for times 1 day or longer ************
	# ******** Or, just set a try-except, and flag a video when it's over 24 hours long ************

	video_duration_re = re.search(r'^PT(.*?H)?(.*?M)?(.*?S)?', video_duration)
	hours = video_duration_re.group(1)
	minutes = video_duration_re.group(2)
	seconds = video_duration_re.group(3)

	if hours: total_playlist_time['hours'] += int(hours[:-1])
	if minutes: total_playlist_time['minutes'] += int(minutes[:-1])
	if seconds: total_playlist_time['seconds'] += int(seconds[:-1])

# Simplify the times
if total_playlist_time['seconds'] >= 60:
	total_playlist_time['minutes'] += total_playlist_time['seconds'] // 60
	total_playlist_time['seconds'] = total_playlist_time['seconds'] % 60
if total_playlist_time['minutes'] >= 60:
	total_playlist_time['hours'] += total_playlist_time['minutes'] // 60
	total_playlist_time['minutes'] = total_playlist_time['minutes'] % 60

for index, (video_title, video_duration) in enumerate(zip(playlist_video_titles, playlist_video_durations), start=1):
	print(f"Video #{index}:")
	print(f"\t Title: {video_title}")
	print(f"\t Duration: {video_duration}\n")

print(f"Duration of entire playlist = {total_playlist_time}\n")





