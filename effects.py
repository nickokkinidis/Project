# Here the terminaltexteffects will be stored as functions to be easily accessible.
# You have to import the effect and the corresponding function to use it.

# Types of Effects      imports
# 1. Print              from terminaltexteffects.effects.effect_print import Print
# 2. Beams              from terminaltexteffects.effects.effect_beams import Beams
# 3. BinaryPath         from terminaltexteffects.effects.effect_binarypath import BinaryPath
# 4. RandomSequence     from terminaltexteffects.effects.effect_random_sequence import RandomSequence
# 5. Rain               from terminaltexteffects.effects.effect_rain import Rain
# 6. Expand             from terminaltexteffects.effects.effect_expand import Expand
# 7. Decrypt            from terminaltexteffects.effects.effect_decrypt import Decrypt
# 8. Burn               from terminaltexteffects.effects.effect_burn import Burn



#from terminaltexteffects.effects.effect_print import Print
def print1(text):
    effect = Print(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

#from terminaltexteffects.effects.effect_beams import Beams
def print2(text):
    effect = Beams(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

#from terminaltexteffects.effects.effect_binarypath import BinaryPath
def print3(text):
    effect = BinaryPath(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

#from terminaltexteffects.effects.effect_random_sequence import RandomSequence
def print4(text):
    effect = RandomSequence(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

#from terminaltexteffects.effects.effect_rain import Rain
def print5(text):
    effect = Rain(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

#from terminaltexteffects.effects.effect_expand import Expand
def print6(text):
    effect = Expand(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

#from terminaltexteffects.effects.effect_decrypt import Decrypt
def print7(text):
    effect = Decrypt(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

#from terminaltexteffects.effects.effect_burn import Burn
def print8(text):
    effect = Burn(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)