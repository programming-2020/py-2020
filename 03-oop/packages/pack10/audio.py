'''
Polymorphism
'''


class AudioFile(object):

    def __init__(self, filename):
        super().__init__()
        if not filename.endswith(self.ext):
            raise Exception("Invalid format")
        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print(f"Playing {self.filename} as mp3")


class FLACFile(AudioFile):
    ext = "flac"

    def play(self):
        print(f"Playing {self.filename} as flac")
