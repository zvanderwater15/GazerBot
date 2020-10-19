# GazerBot

Python CLI tool that creates a file of lyrical phrases based on lyrics taken from a given spotify playlist.

## Install
Clone this repository and use `pip install .`

## Run
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
### Install
`pip install .`
### Run
`gazerbot lyrics --user zoiaran --playlist Calmest --numsongs 5 --fout results.txt`
### Results
In results.txt or whichever file was specified:
```
Calmest

STATS:
 AVE WORDS: 260
AVE LINES: 52

RANDOMIZED LYRICS

was was you only 
 million to me turning this were 
 drift call won't a 
 
 the 
 then long the are the thought and turned thought one one you free never was one obey drift from to need when 
 
 all finish and everyone only on the yes turned the 
 harm to side to was up of 
 we're to but one find only you him 
 
 will 
 a awake harm 
 the thought 
 ...

```


