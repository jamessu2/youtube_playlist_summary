import json
import re
import requests
import sys

api_key = "YOUR_API_KEY"		# Insert your API key here!

total_time = {'hours': 0, 'minutes': 0, 'seconds': 0}


def update_total_time(dur):	# dur = string of a video duration, that matches Youtube's ISO 8601 format
	global total_time
	dur_re = re.search(r'^P(.*?W)?(.*?D)?T(.*?H)?(.*?M)?(.*?S)?', dur)
	weeks, days, hours, minutes, seconds = dur_re.groups()
	if weeks: total_time['hours'] += int(hours[:-1]) * 24 * 7
	if days: total_time['hours'] += int(hours[:-1]) * 24
	if hours: total_time['hours'] += int(hours[:-1])
	if minutes: total_time['minutes'] += int(minutes[:-1])
	if seconds: total_time['seconds'] += int(seconds[:-1])


if __name__ == "__main__":
	print("***** Fetching Data From A Youtube Playlist *****")

	page_token = ""
	index = 1
	playlist_id = "PLmJq_tQT-51EZ_e6eL9oIFrwDcuIKNh9k"
	# playlist_link = " ".join(sys.argv[1])
	# if search_term == "": 
			# print("Error: No Youtube playlist link provided.")
			# sys.exit()
	# 
	# pattern = re.compile(r'youtube.com/playlist\?list=(.*)')
	# playlist_id_search = pattern.search(playlist_link)
	# print(playlist_id_search.group(1) if playlist_id_search else False)

	while True:
		# Fetch playlist API data
		#	Note: for maxResults, Youtube's default is 5, and 50 is the max allowed. 
		playlist_parameters = {'key': api_key, 'playlistId': playlist_id, 'maxResults': '50', 'part': 'snippet', 'pageToken': page_token}
		playlist_response = requests.get('https://www.googleapis.com/youtube/v3/playlistItems', params=playlist_parameters)
		if not playlist_response.ok:
			print("Error: Youtube playlist link provided is either invalid or not public.")
			sys.exit()
		

		playlist_data = playlist_response.json()		# Fyi, same as 'json.loads(playlist_response.content)', via the json module

		video_ids = [ item['snippet']['resourceId']['videoId'] for item in playlist_data['items'] ]

		# Fetch video API data for the bundle of video_ids (50 at a time allowed, max)
		videos_parameters = {'key': api_key, 'id': ','.join(video_ids), 'part': 'snippet,contentDetails'}
		videos_response = requests.get('https://www.googleapis.com/youtube/v3/videos', params=videos_parameters)
		videos_data = videos_response.json()

		for item in videos_data['items']:
			video_title = item['snippet']['title']
			video_duration = item['contentDetails']['duration']
			print(f"Video #{index}:\n\t Title: {video_title}\n\t Duration: {video_duration}\n")
			index += 1

			update_total_time(video_duration)


		# *******************************
		# **** NEED TO IMPLEMENT: check for nextPageToken! ****
		# 	this should be a while-True loop that will 'break' once there is no nextPageToken
		if 'nextPageToken' in playlist_data.keys(): 
			page_token = playlist_data['nextPageToken']
			print("nextPageToken:", page_token)
		else: 
			print("No nextPageToken")
			break
		# *******************************



	# Simplify total_time
	total_time['minutes'] += total_time['seconds'] // 60
	total_time['seconds'] = total_time['seconds'] % 60
	total_time['hours'] += total_time['minutes'] // 60
	total_time['minutes'] = total_time['minutes'] % 60
	print(f"Duration of entire playlist = {total_time}\n")


	# # *******************************
	# # **** For testing purposes: ****
	# with open('playlist_data.json', 'w', encoding='utf-8') as f:
	#    json.dump(playlist_data, f, ensure_ascii=False, indent=4)
	# # *******************************




















