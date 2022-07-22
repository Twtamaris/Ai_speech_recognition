import pydub
from pydub import AudioSegment
pydub.AudioSegment.ffmpeg = "/absolute/path/to/ffmpeg"
audio = AudioSegment.from_wav('1.wav')


audio = audio + 6

audio = audio * 2

audio = audio.fade_in(2000)

audio.export('good.mp3', format='mp3')

audio2 = AudioSegment.from_wav('good.mp3')
print("Done")

