# youtube_playlist_summary
Ever been curious how long it would take to watch through an entire Youtube playlist?

Well, look no further!


## Functionality
This Python script will tally up the total watch time of all public videos, for any Youtube playlist of your choice.


## Install/Setup
```bash
git clone "https://github.com/jamessu2/youtube_playlist_summary.git"
cd youtube_playlist_summary
pip install -r requirements.txt
```

**Note #1**: You will need a Youtube API key. If you don't know how to get one: don't worry, it's super simple. Just follow the quick instructions in the **Getting A Youtube API Key** section below.

**Note #2**: You need **Python 3** installed.

**Note #3**: If you're using a Mac and you're running into a *"certificate verify failed"* error, you will need to do a one-time:

```bash
cd /Applications/Python3.7	# or whatever your Python version is
./Install\ Certificates.command
```

Why? This will, according to https://github.com/nficano/pytube/issues/241, install "a set of default Root Certificates for the python ssl module by installing the certifi https://pypi.python.org/pypi/certifi."


## Usage
From the `youtube_playlist_summary` directory, run: 

```
python3 youtube_playlist_summary.py <paste link to a youtube playlist>
```


## Getting A Youtube API Key
Don't worry, getting a Youtube API key is a **piece of cake**. Like, 10 clicks.

1. Go to https://console.developers.google.com/ (sign in with a gmail account)
2. Create a "NEW PROJECT" 
	- (which will be under a "Select a project" option in the topbar, if you've never created a project before)
	- Name the project whatever you want (I just called mine "python_youtube")
	- The project will then take a few seconds to create.
3. Go back to the [API home page](https://console.developers.google.com/): you should be in the Dashboard section, where there's an option near the top to "ENABLE APIS AND SERVICES". Click that option.
4. Search for "Youtube Data API v3", and select it.
5. Click "ENABLE", to enable the API
	- Now you have created your own Youtube API
6. Back at the [API home page](https://console.developers.google.com/):, in the "Credentials" section, click on "CREATE CREDENTIALS" in the topbar, and select the "API key" option

Done! Now just copy the API key that was generated, and paste it into the `youtube_playlist_summary.py` file, as indicated by comments (near the top).


## Future Developments
*1st stage: completed Dec 9th, 2019.*

Next-level functionality:

1. Make the playlist argument be an actual `input` once the script has started running. *(Simple adjustment.)*
2. Allow user to provide **either** a link **or** the playlist id itself
3. Figure out a more efficient way to add durations.
	- Is there built-in functionality to convert ISO 8601 to times? Perhaps the [parser module](https://dateutil.readthedocs.io/en/stable/parser.html)?


## Misc Comments
- Code was functional with Youtube API as of Dec 2019.
- Youtube's video durations are supplied in a format called: ["ISO 8601"](https://en.wikipedia.org/wiki/ISO_8601#Durations)
- With an API key, we can retrieve a count of *"Total items in playlist"*, which includes non-public / non-published videos. However, the videos themselves can't actually be retrieved with API alone.
	- You'd need an OAuth client ID, which is a different ballgame and outside the scope of this project.
- A "[Deleted video]" in a Youtube playlist won't count to this project's calculated total watch time, but it will still count as one of the max 50 videoIds in a single video GET request. (50 is the max allowed.)
	- So for example, if a Youtube playlist has 52 videos, 5 of which are labeled as "[Deleted video]", this script will ping the Youtube API 4 times:
		1. Pinging "playlist" once for the first 50 videos
		2. Pinging "video" once for the title and duration of those 50 videos
		3. Pinging "playlist" again for the next 2 videos
		4. Pinging "video" again for the title and duration of those 2 videos
