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



HAT = 42     # placeholder: check your drum cell's hi-hat note

def hat_bar(style, vel):
    # every style fills exactly 4 beats
    if style == "offbeat":
        for beat in range(4):
            rest(0.5)
            playNote(HAT, beats = 0.5, velocity = vel)
    elif style == "eighths":
        for i in range(8):
            playNote(HAT, beats = 0.5, velocity = random.randint(vel - 15, vel))
    else:   # sixteenths
        for i in range(16):
            accent = 10 if i % 4 == 0 else 0       # accent every 4th hit
            playNote(HAT, beats = 0.25, velocity = random.randint(vel - 20, vel - 5) + accent)

if level == 1:
    main_style = "offbeat"
elif level == 2:
    main_style = "eighths"
else:
    main_style = "sixteenths"

def play_phrase(section):
    for bar in range(4):
        if section == "breakdown":
            rest(4)
        elif section == "intro" or section == "outro":
            hat_bar("offbeat", 60)
        elif section == "build":
            hat_bar("eighths", 70)
        else:
            hat_bar(main_style, 80)

for section, phrases in plan:
    for p in range(phrases):
        play_phrase(section)
