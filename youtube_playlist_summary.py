import json
import re
import urllib.request


print("***** Fetching Data From A Youtube Playlist *****")

api_key = "AIzaSyCiDDX-Nm8dLqQ0Id59YNhzJDss6RkGjZg"
# video_id = "pSudEWBAYRE"	# EXO's Love Shot MV
playlist_id = "PLAzDHex22XQz25EiHGjLPATj1C2ScT-hx"	# ShadyPenguinn's Link's Awakening Let's Play Series
max_results = 50


# url_snippet = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
full_url = f"{base_url}?part=snippet&playlistId={playlist_id}&key={api_key}&maxResults={max_results}"
# url_snippet = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&key={api_key}&maxResults={max_results}"

json_playlist = urllib.request.urlopen(full_url)		# outputs an object of class 'http.client.HTTPResponse'
print(type(json_playlist))
temp = json_playlist.read()				# read the response into bytes
print(type(temp))
data_playlist = json.loads(temp)		# load the bytes as a dict, which is JSON
print(type(data_playlist))

print(data_playlist)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data_playlist, f, ensure_ascii=False, indent=4)






# url_content_details = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={video_id}&key={api_key}"

# json_url_content_details = urllib.request.urlopen(url_contentDetails)
# data_content_details = json.loads(json_url_content_details.read())

# print(data_content_details['items'][0]['contentDetails']['duration'])













