from terminaltexteffects.effects.effect_print import Print
effect = Print("YourTextHere")
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)


from terminaltexteffects.effects.effect_beams import Beams
effect = Beams("YourTextHere")
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)

        

from terminaltexteffects.effects.effect_binarypath import BinaryPath
effect = BinaryPath("YourTextHere")
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)



from terminaltexteffects.effects.effect_random_sequence import RandomSequence
effect = RandomSequence("YourTextHere")
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)



from terminaltexteffects.effects.effect_rain import Rain
effect = Rain("YourTextHere")
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)



from terminaltexteffects.effects.effect_expand import Expand
effect = Expand("YourTextHere")
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)




from terminaltexteffects.effects.effect_decrypt import Decrypt
effect = Decrypt("YourTextHere")
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)


from terminaltexteffects.effects.effect_burn import Burn
effect = Burn("YourTextHere")
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)