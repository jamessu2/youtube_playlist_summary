import re
import requests
import sys
# import json

api_key = "YOUR_API_KEY"		# Insert your API key here!

if __name__ == "__main__":
	# Make sure the user provides 1 (and only 1) argument
	if len(sys.argv) == 1: 
		print("Error: No Youtube playlist link provided.")
		sys.exit()
	elif len(sys.argv) > 2:
		print("Error: Please provide a single argument, of a link to a Youtube playlist.")
		sys.exit()

	# Parse the user argument input for the Youtube playlist_id
	pattern = re.compile(r'youtube.com/playlist\?list=(.*)')	# regex of the Youtube playlist URL
	playlist_id_search = pattern.search(sys.argv[1])
	playlist_id = playlist_id_search.group(1) if playlist_id_search else ""

	# Initalize variables
	page_token = ""
	video_index = 0
	total_time = {'hours': 0, 'minutes': 0, 'seconds': 0}

	while True:
		playlist_parameters = {
			'key': api_key, 
			'playlistId': playlist_id, 
			'pageToken': page_token,	# loop will continue if a nextPageToken exists; checked at end of loop
			'part': 'snippet', 
			'maxResults': '50'			# Youtube's default is 5. Max allowed is 50. 
		}
		# Fetch playlist API data
		playlist_response = requests.get('https://www.googleapis.com/youtube/v3/playlistItems', params=playlist_parameters)
		if not playlist_response.ok:
			print("Error: Youtube playlist link provided is either invalid or not public.")
			sys.exit()
		playlist_data = playlist_response.json()	# Fyi, same as 'json.loads(playlist_response.content)', via the json module

		# Get video_ids of all videos in the current playlist page
		video_ids = [ video['snippet']['resourceId']['videoId'] for video in playlist_data['items'] ]

		# Fetch video API data
		videos_parameters = {
			'key': api_key, 
			'id': ','.join(video_ids), 
			'part': 'snippet,contentDetails'
		}
		videos_response = requests.get('https://www.googleapis.com/youtube/v3/videos', params=videos_parameters)
		videos_data = videos_response.json()

		for video in videos_data['items']:
			# Get desired info on the current video
			video_title = video['snippet']['title']
			video_duration = video['contentDetails']['duration']	# format of duration is in Youtube's ISO 8601 format
			video_index += 1	# for output purposes
			print(f"Video #{video_index}\nTitle: {video_title}\nDuration: {video_duration}\n")

			# Update total_time with the current video's duration
			pattern = re.compile(r'^P(.*?W)?(.*?D)?T(.*?H)?(.*?M)?(.*?S)?')		# regex of the ISO 8601 format
			weeks, days, hours, minutes, seconds = pattern.search(video_duration).groups()
			if weeks: total_time['hours'] += int(hours[:-1]) * 24 * 7
			if days: total_time['hours'] += int(hours[:-1]) * 24
			if hours: total_time['hours'] += int(hours[:-1])
			if minutes: total_time['minutes'] += int(minutes[:-1])
			if seconds: total_time['seconds'] += int(seconds[:-1])

		# Check if playlist_data has a nextPageToken (aka more videos in the playlist to account for)
		if 'nextPageToken' in playlist_data.keys(): 
			page_token = playlist_data['nextPageToken']
			# print("nextPageToken:", page_token)
		else: 
			# print("No nextPageToken.")
			break

	# Simplify total_time
	total_time['minutes'] += total_time['seconds'] // 60
	total_time['seconds'] = total_time['seconds'] % 60
	total_time['hours'] += total_time['minutes'] // 60
	total_time['minutes'] = total_time['minutes'] % 60
	print(f"Duration of entire playlist = {total_time}\n")
