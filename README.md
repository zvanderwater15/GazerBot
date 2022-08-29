# GazerBot

Python CLI tool that creates a file of lyrical phrases based on lyrics taken from a given spotify playlist. The algorithm walks through a Markov chain generated from the given songs. Works better for medium-sized playlists (>150 songs, <1000), as small playlists will start to repeat exact phrases from the given songs, and large playlists will take too long to run. Best used to get inspiration!

## Install

Clone this repository and navigate inside the repo. This repo does not include access to the Spotify and Genius APIs, you must first get your own API credentials and fill in the empty variables in the gazerbot/secrets.py file.
After the credentials have been added, use `pip install .` in the main project directory.


This has only been tested on Windows and is not guaranteed to work in other environments.


## Test
```
pytest tests/
```

## Run
At the moment, you must navigate to the gazerbot directory to run this command as it uses the lyrics/ folder to cache Genius API responses. 

```
Usage: gazerbot lyrics [OPTIONS]

Options:
  --user TEXT         spotify user that owns the playlist
  --playlist TEXT     playlist to grab songs from
  --numsongs INTEGER  number of lyric groups to generate
  --fout TEXT         Output file to print generate lyrics to
  --help              Show this message and exit.
```
## Example
### Run
`gazerbot lyrics --user fakeuser --playlist "elliott smith discography" --numsongs 5 --fout results.txt`
### Results
In results.txt or whichever file was specified:

```
PLAYLIST:
elliott smith discography

STATS:
 AVE WORDS: 260
AVE LINES: 52

RANDOMIZED LYRICS

-----outto------

dollar bill
 her steps in the rest
 and was dim
 when go away
 it's just told me all pretension never good to close the same mistake twice
 and can't lose
 it's never meant to bring some kind of the world is the soaring high on night
 to a sound
 you're not surprised at times a world rock 'n' roller acting under the bay with the lane

 you lose
 in black
 standing out to know
 with a game baby
 don't start
 fought him pain
 but lost and stay out
 she sees behind my room
 wish could be apart
 believe it's your last call
 seen how to do
 'cause it something sweet smile crossing your letters
 now that shoots back
 so bought up mine
 new game of a vision in the jet stream of no one's gonna drag us on 
 ...

```


