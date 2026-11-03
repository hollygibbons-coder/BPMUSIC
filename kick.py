# New TunePad cell
import random

#  SETTINGS: keep identical in every cell 
bpm = 140               # set to match the BPM at the top of TunePad: 120, 140 or 160
target_seconds = 150    # aimed track length (change to 180 for 3 minutes)

# Preset level: controls how busy the music is
if bpm <= 120:
    level = 1           # chill: sparse and relaxed
elif bpm <= 140:
    level = 2           # driving
else:
    level = 3           # intense: busiest rhythms

# One "phrase" = 4 bars = 16 beats. Work out how many phrases fill the target
# length, and give the leftover to the second main section.
total_phrases = round(target_seconds * bpm / 960)
second_main = max(2, total_phrases - 12)   # 12 phrases are used by the other sections

plan = [("intro", 2), ("build", 2), ("main", 4),
        ("breakdown", 2), ("main", second_main), ("outro", 2)]


KICK = 36    # placeholder: find your drum cell's real kick note first

def play_phrase(section):
    if section == "breakdown":
        rest(16)                                 # kick drops out for the breakdown
    else:
        for beat in range(16):                   # four-on-the-floor
            playNote(KICK, beats = 1, velocity = 100)

for section, phrases in plan:
    for p in range(phrases):
        play_phrase(section)
