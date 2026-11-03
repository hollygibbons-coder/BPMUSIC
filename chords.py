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

# One "phrase" = 4 bars = 16 beats
total_phrases = round(target_seconds * bpm / 960)
second_main = max(2, total_phrases - 12)

plan = [("intro", 2), ("build", 2), ("main", 4),
        ("breakdown", 2), ("main", second_main), ("outro", 2)]

# ===== CHORDS =====
# Cm7 - Abmaj7 - Fm7 - Gm7, inverted so each chord sits close to the last
chords = [[60, 63, 67, 70], [60, 63, 67, 68], [60, 63, 65, 68], [58, 62, 65, 67]]

# Sparse stab pattern for the chill preset (1 = stab, 0 = rest)
stab_pattern = [1, 0, 1, 0]

# ===== PATTERN FUNCTIONS (these must sit ABOVE play_phrase) =====
def stab_bar(notes, pattern, vel):
    # 4 beats. Each beat = half a beat of silence, then the stab (offbeat push)
    for hit in pattern:
        rest(0.5)
        if hit == 1:
            playNote(notes, beats = 0.5, velocity = random.randint(vel - 7, vel))
        else:
            rest(0.5)

def stab_bar_syncopated(notes, vel):
    # 0.5 + 1 + 0.5 + 1 + 0.5 + 0.5 = 4 beats: syncopated house piano pattern
    playNote(notes, beats = 0.5, velocity = vel)
    rest(1)
    playNote(notes, beats = 0.5, velocity = vel - 5)
    rest(1)
    playNote(notes, beats = 0.5, velocity = vel)
    rest(0.5)

# ===== SONG SECTIONS =====
def play_phrase(section):
    for notes in chords:                              # 4 bars = 16 beats
        if section == "intro":
            rest(4)                                   # drums only to start
        elif section == "build":
            playNote(notes, beats = 4, velocity = 55) # soft held chords
        elif section == "breakdown":
            playNote(notes, beats = 4, velocity = 65) # chords alone, no stabs
        elif section == "outro":
            stab_bar(notes, [1, 0, 1, 0], 60)         # thin out to finish
        else:
            # main groove: sparse at 120 BPM, syncopated piano at 140 and 160
            if level == 1:
                stab_bar(notes, stab_pattern, 85)
            else:
                stab_bar_syncopated(notes, 85)

# ===== RUN THE SONG =====
for section, phrases in plan:
    for p in range(phrases):
        play_phrase(section)
