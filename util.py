from pychord import Chord




cname_to_note = {
    "B" : "B2",
    "C" : "C3",
    "D" : "D3",
    "E" : "E3",
    "F" : "F3",
    "G" : "G3",
    "A" : "A3",
}


def to_real_chord(c):

   return [cname_to_note[n] for n in c]

