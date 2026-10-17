
# CodeAlpha Internship - Task 3
# Music Generation with Python

from midiutil import MIDIFile
import random

# Step 1: Create a MIDI file
music = MIDIFile(1)

track = 0
channel = 0
time = 0
tempo = 120
volume = 100

music.addTempo(track, time, tempo)

# Step 2: Define musical notes
notes = [60, 62, 64, 65, 67, 69, 71, 72]

# Step 3: Generate a melody
print("Generating music...")

for i in range(16):
    pitch = random.choice(notes)
    duration = 1

    music.addNote(
        track,
        channel,
        pitch,
        time,
        duration,
        volume
    )

    time += duration

# Step 4: Save music as a MIDI file
with open("generated_music.mid", "wb") as file:
    music.writeFile(file)

print("Music generated successfully!")
print("File saved as generated_music.mid")


    
    
    
  
        
       
          
            
                
