from pychord import Chord




cname_to_note = {
    "B" : "B3",
    "Bb" : "Bb3",
    "C" : "C4",
    "C#" : "C#4",
    "D" : "D4",
    "Db" : "Db4",
    "D#" : "D#4",
    "E" : "E4",
    "Eb" : "Eb4",
    "F" : "F4",
    "F#" : "F#3",
    "G" : "G3",
    "Gb" : "Gb3",
    "G#" : "G#3",
    "A" : "A3",
    "Ab" : "Ab3",
    "A#" : "A#3",
}


def to_real_chord(c):

   return [cname_to_note[n] for n in c]

