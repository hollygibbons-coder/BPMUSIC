# New TunePad cell
import random

#  SETTINGS: keep identical in every cell 
bpm = 140               # set to match the BPM at the top of TunePad: 120, 140 or 160
target_seconds = 150

if bpm <= 120:
    level = 1           # chill
elif bpm <= 140:
    level = 2           # driving
else:
    level = 3           # intense

total_phrases = round(target_seconds * bpm / 960)
second_main = max(2, total_phrases - 12)

plan = [("intro", 2), ("build", 2), ("main", 4),
        ("breakdown", 2), ("main", second_main), ("outro", 2)]

#  LEAD MELODY 
# Notes that fit each chord (chord tones in a higher register).
# Order matches the chord cell: Cm7, Abmaj7, Fm7, Gm7
melody_notes = [
    [79, 75, 72],   # over Cm7:    G, Eb, C
    [75, 72, 79],   # over Abmaj7: Eb, C, G
    [77, 75, 72],   # over Fm7:    F, Eb, C
    [74, 77, 79],   # over Gm7:    D, F, G
]

def lead_bar(options, vel):
    # One 4-beat bar of melody. Busier as the preset level goes up.
    if level == 1:
        # chill: one long note, then space
        playNote(options[0], beats = 2, velocity = vel)
        rest(2)
    elif level == 2:
        # driving: a short phrase (1.5 + 0.5 + 1 + 1 = 4 beats)
        playNote(options[0], beats = 1.5, velocity = vel)
        playNote(options[1], beats = 0.5, velocity = vel - 5)
        rest(1)
        playNote(options[2], beats = 1, velocity = vel)
    else:
        # intense: running eighth notes with random choices and gaps
        for i in range(8):
            if random.random() < 0.7:
                playNote(random.choice(options), beats = 0.5,
                         velocity = random.randint(vel - 10, vel))
            else:
                rest(0.5)

def play_phrase(section):
    # 4 bars x 4 beats = 16 beats, matching the other cells
    for bar_index, options in enumerate(melody_notes):
        if section == "intro":
            rest(4)                                          # stay out of the way
        elif section == "build":
            if bar_index >= 2:
                playNote(options[0], beats = 4, velocity = 50)   # fade in during the second half
            else:
                rest(4)
        elif section == "breakdown":
            playNote(options[0], beats = 4, velocity = 60)       # long notes carry the breakdown
        elif section == "outro":
            if bar_index == 0:
                playNote(options[0], beats = 4, velocity = 50)   # one last note
            else:
                rest(4)
        else:
            lead_bar(options, 70)                                # main groove

#  RUN THE SONG 
for section, phrases in plan:
    for p in range(phrases):
        play_phrase(section)
