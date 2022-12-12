
DOC_TYPES = ["txt", "word", "pdf"]
VIDEO_TYPES = ["mp4", "mov", "wmv"]
PHOTO_TYPES = ["jpeg", "jpg", "png"]
AUDIO_TYPES = ["mp3", "wav"]
SUSPICIOUS_TYPES = ["exe", "zip"]

# Classify the file and return the correct path for the file to be stored at


def file_classification(file_dits):
    extension = file_dits[2].split(".")[-1]
    if extension.lower() in DOC_TYPES:
        return ".\\Documents"
    elif extension.lower() in VIDEO_TYPES:
        return ".\\Videos"
    elif extension.lower() in PHOTO_TYPES:
        return ".\\Photos"
    elif extension.lower() in AUDIO_TYPES:
        return ".\\Audio"
    elif extension.lower() in SUSPICIOUS_TYPES:
        return ".\\Suspicious"
    else:
        return 5

# A function to build a data and target matrices to be used as training dataset for a decision tree algorithm later on


