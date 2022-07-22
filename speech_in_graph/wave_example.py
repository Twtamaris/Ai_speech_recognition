import wave
obj = wave.open('1.wav', "rb")

#Reading Inside of Sound Input
print("Number of Channels", obj.getnchannels())
print('Sample width', obj.getsampwidth())
print('Frame rate', obj.getframerate())
print('Number of frames', obj.getnframes())
print('Parameters', obj.getparams())
time_audio = obj.getnframes()/obj.getframerate()
print(time_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

print(len(frames)/4)
obj.close()

obj_new = wave.open('Hello.wav', 'wb')
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(44100)

obj_new.writeframes(frames)
obj_new.close()