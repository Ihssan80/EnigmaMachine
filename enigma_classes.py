from errors import *
import string


class PlugLead:
    def __init__(self, mapping):
        self.mapp = mapping
        # check if plug leads are two and both are letters,then check if paired letters are not similar,
        # if not error msg will show error type.
        if (len(self.mapp) == 2) and (self.mapp.isalpha()):
            if self.mapp[0] != self.mapp[1]:
                self.mapp = self.mapp.upper()
            else:
                raise ClassValueError(ClassValueError(100).error_code)
        else:
            raise ValueError(ClassValueError(101).error_code)

    # this method will check if the type to be encoded is letter and len of the letter is 1
    def encode(self, encoded_letter):
        if (len(encoded_letter) == 1) and (encoded_letter.isalpha()):
            # if the entered letter is small transform it to capital letter:
            encoded_letter = encoded_letter.upper()
            if encoded_letter in self.mapp:
                if encoded_letter == self.mapp[0]:
                    return self.mapp[1]
                else:
                    return self.mapp[0]
            else:
                return encoded_letter
        else:
            raise ValueError(ClassValueError(102).error_code)


class Plugboard:
    def __init__(self):
        self.leads_list = []

    # before adding the plug leads to the list of plugboard below condition need to be satisfied first
    def add(self, lead1):
        # 1. check if current plug leads list not more than 10 pairs
        if len(self.leads_list) < 10:
            # check if the lead not available and mapped to any pair of the plug leads list otherwise rise an error from ClassValueError
            if lead1.mapp not in self.leads_list:

                if ((lead1.mapp[0] in [x[0] for x in self.leads_list]) or (
                        lead1.mapp[1] in [x[1] for x in self.leads_list])):

                    raise ClassValueError(ClassValueError(103).error_code)
                elif ((lead1.mapp[0] in [x[1] for x in self.leads_list]) or (
                        lead1.mapp[1] in [x[0] for x in self.leads_list])):
                    raise ClassValueError(ClassValueError(103).error_code)
                else:
                    self.leads_list.append(lead1.mapp[0] + lead1.mapp[1])

            else:
                raise ClassValueError(ClassValueError(104).error_code)
        else:
            raise ClassValueError(ClassValueError(105).error_code)

    # check if the lead to encode one letter only and if it is an alphabet letter if yes return the paired letter else rise error from ClassValueError
    def encode(self, pl_enc):
        if (len(pl_enc) == 1) and (pl_enc.isalpha()):
            pl_enc = pl_enc.upper()
            for map_char in self.leads_list:

                if pl_enc == map_char[0]:
                    return map_char[1]
                elif pl_enc == map_char[1]:
                    return map_char[0]

            return pl_enc
        else:
            raise ValueError(ClassValueError(102).error_code)


class Rotors:
    def __init__(self, wiring, position, ring_setting):
        self.wiring = wiring

        if position not in list(string.ascii_uppercase):
            raise ValueError(ClassValueError(107).error_code)

        if ring_setting not in ["{:02d}".format(ring) for ring in range(1, 27)]:
            raise ValueError(ClassValueError(108).error_code)

        self.position = (ord(position)-ord("A")) % 26
        self.ring = int(ring_setting) - 1

    def encode_right_to_left(self, chara):
        index = (ord(chara) - ord("A") + self.position - self.ring) % 26
        encoded = self.wiring[index]
        enc_index = (ord(encoded) - ord("A") - self.position + self.ring) % 26
        return chr(enc_index + ord("A"))

    def encode_left_to_right(self, chara):
        index = (ord(chara) - ord("A") + self.position - self.ring) % 26
        encoded = chr(index + ord("A"))
        index = self.wiring.find(encoded)
        return chr((index - self.position + self.ring) % 26 + ord("A"))

    def rotate(self):
        self.position = (self.position + 1) % 26


class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def mapping(self, chara):
        index = (ord(chara)-ord("A")) % 26
        return self.wiring[index]