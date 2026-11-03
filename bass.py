# New TunePad cell

import random

# ===== SETTINGS: keep identical in every cell =====
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


roots = [36, 32, 29, 31]    # C, Ab, F, G, the roots of the chords above

def bass_bar(root, vel):
    if level == 1:
        playNote(root, beats = 2, velocity = vel)          # relaxed: two long notes
        playNote(root, beats = 2, velocity = vel - 10)
    else:
        for beat in range(4):
            rest(0.5)                                      # offbeat bass
            note = root
            if level == 3 and random.random() < 0.3:
                note = root + 12                           # octave jump for energy
            playNote(note, beats = 0.5, velocity = vel)

def play_phrase(section):
    for root in roots:
        if section == "intro" or section == "breakdown":
            rest(4)                                        # bass drops out for contrast
        elif section == "build" or section == "outro":
            playNote(root, beats = 4, velocity = 60)       # quiet held root
        else:
            bass_bar(root, 95)

for section, phrases in plan:
    for p in range(phrases):
        play_phrase(section)
