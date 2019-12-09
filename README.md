# youtube_playlist_summary
Ever been curious how long it would take to watch through an entire Youtube playlist?

Well, look no further!

This Python script will tally up the total watch time for any Youtube playlist of your choice.


# Improvements To Make
- Account for playlists that have more than 50 videos (i.e. nextPageToken(s))
- Figure out a more efficient way to add durations.
	- Is there built-in functionality to convert ISO 8601 to times? Perhaps the [parser module](https://dateutil.readthedocs.io/en/stable/parser.html)?
- Account for days and weeks in total duration printout
- Change playlist id to be a user input


# Install/Setup
```
git clone "https://github.com/jamessu2/youtube_playlist_summary.git"
cd youtube_playlist_summary
pip install -r requirements.txt
```

You will need to go to the Youtube API page, log in with your account, and quickly click a few buttons to get a API key – which you will put into the script.

Assuming you've never created an API key before, don't worry: it's super simple.

1. Go to https://console.developers.google.com/ (sign in if needed)
2. Create a "NEW PROJECT" 
	- (which will be under a "Select a project" option in the topbar if you've never created a project before)
	- Name the project whatever you want (I called mine "python_youtube")
	- It will take a few seconds to create.
3. Again, make sure you're at the API home page: https://console.developers.google.com/. You should be in the Dashboard section, where there's an option near the top to "ENABLE APIS AND SERVICES". Click on that option.
4. Search for "Youtube Data API v3"
5. Click "ENABLE" to enable the API
	- Now you have created your own API
6. Back at the home page, click on the "Credentials" section, click on "CREATE CREDENTIALS" in the topbar, and select the "API key" option
7. Copy the API key that was generated, and paste it into the youtube_playlist_summary.py file near the top, as indicated by comments in the file

Note: Code was tested with Youtube API as of Dec 2019.

Note: You need **Python 3** installed.


# Usage
From the `youtube_playlist_summary` directory, run: 

```
python3 youtube_playlist_summary.py <paste link to a youtube playlist>
```


# Sidenotes
If you're using a Mac and you're running into a *"certificate verify failed"* error, you will need to do a one-time:

```
cd /Applications/Python3.7	# or whatever your Python version is
./Install\ Certificates.command
```

This will, according to https://github.com/nficano/pytube/issues/241: "installs a set of default Root Certificates for the python ssl module by installing the certifi https://pypi.python.org/pypi/certifi."


Youtube video durations are in a format called: ["ISO 8601"](https://en.wikipedia.org/wiki/ISO_8601#Durations)


(There is a difference between "Total items in playlist" vs "Public items in playlist")

