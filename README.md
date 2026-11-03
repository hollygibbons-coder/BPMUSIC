# BPMUSIC
Creative Coding project A2
this is where you add details

# BPMUSIC: BPM focused, coded House Music preset for Runners

An instrumental house track built in TunePad (Python) for runners. One song adapts to three tempo presets (120, 140 and 160 BPM): the higher the tempo, the busier the music.

# By: Holly  | Student number: 25814652 | 
# Subject: 52685 Creative Coding (A2 Code Prototype Project)

# Links
TunePad project: https://tunepad.com/project/135105#code
Explainer video:  To be added***

# Project overview 

Finding music that matches my running pace is difficult, and lyrics can distract from technique. This prototype is a lyric-free house track with a steady four-on-the-floor pulse that a runner can lock onto, like a metronome. Rather than three separate songs, one set of code changes how busy each layer is depending on the chosen preset.

# How it works

The song is split across five TunePad cells, one per instrument layer. They play at the same time, so each cell must add up to the same number of beats.
Cell
Layer
File
1
Chord stabs (Cm7, Abmaj7, Fm7, Gm7)
chords.py
2
Bass (chord roots)
bass.py
3
Kick drum
kick.py
4
Hi-hats
hats.py
5
Lead melody
lead.py

# Key ideas in the code:

bpm and level: bpm is set to 120, 140 or 160. An if/elif/else chain turns it into a level of 1, 2 or 3, which every cell reads to decide how busy to be.
plan: a list of (section, phrases) pairs (intro, build, main, breakdown, main, outro) that works as the song's blueprint. Every cell follows it.
16-beat phrases: each cell's play_phrase(section) function fills exactly 16 beats (4 bars of 4 beats), which keeps all the layers in sync.
Track length: the code calculates how many phrases fit the target length for the chosen BPM and gives the remainder to the second main section.
Variation: Python's random module varies velocities and, at the highest level, which notes the bass and lead play, so each run differs slightly.

# The three presets

Preset
Level
Feel


120 BPM
1
Relaxed and sparse

140 BPM
2
Driving and consistent

160 BPM
3
Intense and busiest


# How to run

Open the TunePad project link above 
Set the project tempo at the top of TunePad to 120, 140 or 160.
In every cell, set bpm to the same value as the project tempo.
Press play on each cell, or play the project from the top.

OR 

Open up the Desired m4a and hit play - there are 3 presets representative of each BPM (each are labelled)

# Dependencies

TunePad (free, browser-based): https://tunepad.com
Python random module (part of the standard library, imported at the top of each cell)
No other libraries or external assets. All sounds come from TunePad's built-in instruments, and no samples were used.

# Repository contents

chords.py, bass.py, kick.py, hats.py, lead.py: the code for each TunePad cell
README.md: this file
audio/: recordings of each preset (120,140 & 160 upload separately )
screenshots/: screenshots of the TunePad project

# Limitations and next steps

bpm is set by hand in each cell and has to match the TunePad project tempo, because I did not find a way for the code to read the project tempo.
The shared settings are repeated at the top of every cell, because I was not sure whether TunePad cells can share variables.
Possible next steps if i were to add: a clap layer, more variation between sections, and testing whether the repeated settings can be avoided.

# References
***To be finalised →>>

Ballmann, C. G. (2021). The influence of music preference on exercise responses and performance: A review. Journal of Functional Morphology and Kinesiology, 6(2), 33.
https://doi.org/10.3390/jfmk6020033doi

Northwestern University TIDAL Lab. (2026). TunePad (Version 1.0) [Computer software]. 
https://tunepad.com

Runners Need. (n.d.). Running and music: Finding your BPM. https://www.runnersneed.com/expert-advice/training/running-and-music-finding-your-bpm.htmlrunnersneed

Start Fitness. (2024, September 24). What music is good for running and what are the benefits?
https://startfitness.co.uk/blogs/news/what-music-is-good-for-running-and-what-are-the-benefits



