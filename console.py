from synthesizer import Player, Synthesizer, Waveform
from pychord import Chord

from util import to_real_chord


player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

# Play A4
# player.play_wave(synthesizer.generate_constant_wave(440.0, 3.0))


def play_c_major():
    # Play C major
    chord = ["C3", "E3", "G3"]
    player.play_wave(synthesizer.generate_chord(chord, 3.0))


def play_freqs():
    # You can also specify frequencies to play just intonation
    chord = [440.0, 550.0, 660.0]
    player.play_wave(synthesizer.generate_chord(chord, 3.0))



def play_chord(ch):
    # >>> play_chord(to_real_chord(Chord("C").components()))
    player.play_wave(synthesizer.generate_chord(ch, 2.0))

def play_cadence():
    # Play cadence
    ch1 = ["C3", "E3", "G3"]
    ch4 = ["C3", "F3", "A3"]
    ch57 = ["B2", "F3", "G3"]

    player.play_wave(synthesizer.generate_chord(ch1, 1.0))
    player.play_wave(synthesizer.generate_chord(ch4, 1.0))
    player.play_wave(synthesizer.generate_chord(ch57, 1.0))
    player.play_wave(synthesizer.generate_chord(ch1, 4.0))

play_cadence()
