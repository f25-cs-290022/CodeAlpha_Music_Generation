import numpy as np
from music21 import converter, instrument, note, chord, stream
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Activation

# ==========================================
# CodeAlpha Task 3: Music Generation with AI
# ==========================================

def build_music_model(input_shape, n_vocab):
    """Builds an LSTM deep learning model to learn music patterns."""
    model = Sequential()
    model.add(LSTM(128, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(128))
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(n_vocab))
    model.add(Activation('softmax'))
    
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
    return model

def convert_to_midi(prediction_output, filename="generated_music.mid"):
    """Converts predicted note sequences into a downloadable MIDI file."""
    offset = 0
    output_notes = []
    
    for pattern in prediction_output:
        if ('.' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('.')
            notes = []
            for current_note in notes_in_chord:
                new_note = note.Note(int(current_note))
                new_note.storedInstrument = instrument.Piano()
                notes.append(new_note)
            new_chord = chord.Chord(notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
        else:
            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)
        
        offset += 0.5

    midi_stream = stream.Stream(output_notes)
    midi_stream.write('midi', fp=filename)
    print(f"Generated music successfully saved as {filename}")

if __name__ == "__main__":
    print("==================================================")
    print("   CodeAlpha Task 3: AI Music Generator Active    ")
    print("==================================================")
    print("Dependencies: pip install music21 tensorflow numpy")
    print("Model Architecture: LSTM Neural Network for Sequence Learning[span_2](start_span)[span_2](end_span)")
