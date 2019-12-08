import json
import re
import requests
# import dateutil.parser


print("***** Fetching Data From A Youtube Playlist *****")


api_key = "YOUR_API_KEY"		# *** update with your own API key! ***
playlist_id = "PLAzDHex22XQz25EiHGjLPATj1C2ScT-hx"		# this will need to be changed to an argument
max_results = 3											# change this to be hardcoded into the params
														# 	Remember: 50 is max

playlist_parameters = {'key': api_key, 'playlistId': playlist_id, 'maxResults': str(max_results), 'part': 'snippet'}
playlist_response = requests.get('https://www.googleapis.com/youtube/v3/playlistItems', params=playlist_parameters)

playlist_data = playlist_response.json()		# Sidenote: same as 'json.loads(response.content)', via the json module



playlist_video_titles = []
playlist_video_ids = []
playlist_video_durations = []
total_playlist_time = {
	'hours': 0,
	'minutes': 0,
	'seconds': 0
}

# ******** CREATE FOR LOOP HERE ************

# for item in playlist_data['items']:
# 	playlist_video_titles.append(item['snippet']['title'])
# 	playlist_video_ids.append(item['snippet']['resourceId']['videoId'])



# *******************************************



first_video_title = playlist_data['items'][0]['snippet']['title']
first_video_id = playlist_data['items'][0]['snippet']['resourceId']['videoId']
print("First video title:", first_video_title)
print("First video id:", first_video_id)

video_parameters = {'key': api_key, 'id': first_video_id, 'part': 'contentDetails'}
video_response = requests.get('https://www.googleapis.com/youtube/v3/videos', params=video_parameters)

video_data = video_response.json()

video_duration = video_data['items'][0]['contentDetails']['duration']
print(video_duration)
print(type(video_duration))

video_duration_re = re.search(r'^PT(.*?H)?(.*?M)?(.*?S)?', video_duration)
hours = video_duration_re.group(1)
minutes = video_duration_re.group(2)
seconds = video_duration_re.group(3)

if hours: print(hours)
if minutes: print(minutes)
if seconds: print(seconds)






second_video_title = playlist_data['items'][1]['snippet']['title']
second_video_id = playlist_data['items'][1]['snippet']['resourceId']['videoId']
print("Second  video title:", second_video_title)
print("Second video id:", second_video_id)

# Get the video lengths

video_parameters = {'key': api_key, 'id': second_video_id, 'part': 'contentDetails'}
video_response = requests.get('https://www.googleapis.com/youtube/v3/videos', params=video_parameters)

video_data = video_response.json()

video_duration = video_data['items'][0]['contentDetails']['duration']
print(video_duration)
print(type(video_duration))


# ******** BEGIN EDIT ************
# ******** Need to edit this section to account for times 1 day or longer ************
# ******** Or, just set a try-except, and flag a video when it's over 24 hours long ************

video_duration_re = re.search(r'^PT(.*?H)?(.*?M)?(.*?S)?', video_duration)
hours = video_duration_re.group(1)
minutes = video_duration_re.group(2)
seconds = video_duration_re.group(3)

if hours: print(hours)
if minutes: print(minutes)
if seconds: print(seconds)

# ******** END EDIT ************







# ********* You can put up to 50 video IDs in a VIDEOS request!!!! **********
# ********* Just separate the video IDs by commas!!!! **********



# # video_id = "pSudEWBAYRE"	# EXO's Love Shot MV

# # url_snippet = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"


# url_content_details = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={video_id}&key={api_key}"

# json_url_content_details = urllib.request.urlopen(url_contentDetails)
# data_content_details = json.loads(json_url_content_details.read())

# print(data_content_details['items'][0]['contentDetails']['duration'])



# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)






