import json
from enigma_classes import *

def rotor_func(enigma_settings, rotor_reflector, enigma_rotors, char):

    rotate_next = False
    rotate_third = False

    # Check if the right rotor on its notch
    if chr(ord("A") + enigma_rotors[-1].position) == notch_settings(enigma_settings['rotors'][-1]):
        rotate_next = True

    # Check if the second rotor on its notch
    if chr(ord("A") + enigma_rotors[-2].position) == notch_settings(enigma_settings['rotors'][-2]):
        rotate_third = True

    # Always rotate the right rotor
    enigma_rotors[-1].rotate()

    # Rotate second rotor
    if rotate_next or rotate_third:
        enigma_rotors[-2].rotate()

    # Rotate third rotor
    if rotate_third:
        enigma_rotors[-3].rotate()

    # Rotor: Right to left
    for forward_rotor in reversed(enigma_rotors):
        char = forward_rotor.encode_right_to_left(char)

    # Reflector
    char = rotor_reflector.mapping(char)

    # Rotor: left to right
    for backward_rotor in enigma_rotors:
        char = backward_rotor.encode_left_to_right(char)

    return char

def notch_settings(char):
    notch = {
            "I": "Q",
            "II": "E",
            "III": "V",
            "IV": "J",
            "V": "Z",
            "Beta": "",
            "Gamma": ""
    }
    return notch[char]

def simulator(settings_, msg_, rot_ref=''):

    if not rot_ref:
        with open('rotors_reflectors.json', 'r') as f:
            rot_ref = json.load(f)

    # Add the Leads to the created Plugboard object:
    plugboard = Plugboard()
    for lead in settings_["pairs"]:
        plugboard.add(PlugLead(lead))

    # Rotors
    rotors = []
    for rot, pos, ring in zip(settings_['rotors'], settings_["initial_positions"], settings_["ring_settings"]):
        rotors.append(Rotors(rot_ref[rot], pos, ring))

    # Reflector
    reflector = Reflector(rot_ref[settings_["reflector"]])

    enc_msg = ''

    for char in msg_:
        # Plugboard
        char = plugboard.encode(char)

        # Rotors demonstration
        char = rotor_func(settings_, reflector, rotors, char)

        # Plugboard
        char = plugboard.encode(char)

        enc_msg += char

    return f"Is Encoded to : {enc_msg}"


if __name__ == "__main__":

    # Declaring notch's to be used with rotors:

    # Open and read Wiring settings for rotors and reflectors from json files:
    #------------------------------------------------------------------------
    with open('rotors_Demonstration.json', 'r') as f:
        rotors_Demonstration = json.load(f)

        if "settings1" in rotors_Demonstration:
            settings = rotors_Demonstration["settings1"]

    with open('rotors_reflectors.json', 'r') as f:
        rot_ref = json.load(f)
    #--------------------------------------------------------------------------
    msg = "HELLOWORLD"
    print(f"TEST1 :\nThe text      : {msg}\n{simulator(settings, msg)}\n\nThis result is based on below rotors demonstrations settings : \n{settings}")

    print('\n""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""\n')

    # Open and read Wiring settings for rotors and reflectors from json files:
    #------------------------------------------------------------------------
    with open('rotors_Demonstration.json', 'r') as f:
        rotors_Demonstration = json.load(f)

        if "settings2" in rotors_Demonstration:
            settings = rotors_Demonstration["settings2"]
    #-------------------------------------------------------------------------
    msg = "BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI"

    print(f"TEST2 :\nThe text      : {msg}\n{simulator(settings, msg)}\n\nThis result is based on below rotors demonstrations settings : \n{settings}")