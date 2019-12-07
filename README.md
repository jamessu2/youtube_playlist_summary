# youtube_playlist_summary
Print out the videos in a Youtube playlist, and count the total watch time for the entire playlist

# Goals
- Create a Youtube API key
- Fetch the JSON data for the playlist, and load it to a dictionary
- Loop through the data to retrieve all video titles
- Loop through the data to retrieve all video time lengths
- Calculate the sum of all video time lengths
- Print out a summary of video titles, their lenghts, 
	and the name of the playlist, as well as the total time of the playlist


# Install/Setup
```
git clone "https://github.com/jamessu2/youtube_playlist_summary.git"
cd youtube_playlist_summary
```

You will need to go to the Youtube API page, log in with your account, and quickly click a few buttons to get a API key – which you will put into the script.



# Usage
```
python3 youtube_playlist_summary.py <insert link to youtube playlist>
```

