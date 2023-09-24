value_error_messages = {
    100: "PlugLead Alphabets must not be the same",
    101: "PlugLead must be 2 alphabets only",
    102: "Input for encoding must be one alphabet only",
    103: "You entered a letter already connected to other lead",
    104: "The Lead already in the Leads list",
    105: "Leads List is full, you cannot insert more than 10 leads",
    106: "Invalid reflector",
    107: "The position should be one alphabetical letter",
    108: "The ring setting should be between 01 to 26"
}


class ClassValueError(ValueError):
    def __init__(self, error_code):
        self.error_code = value_error_messages[error_code]
        print(value_error_messages[error_code])


