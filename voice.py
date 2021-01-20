import requests
import speech_recognition as sr     
import subprocess
from gtts import gTTS


r = sr.Recognizer()  # initialize recognizer

while True:
	message = ''
	with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
		r.adjust_for_ambient_noise(source, duration=1)
		print("Speak Something :")
		audio = r.listen(source)  # listen to the source
		try:
			message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
			print("You said : {}".format(message))
		except:
			print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
	if len(message)==0:
		continue

	bot_message = ""
	inp = message
	res = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": inp})

	for i in res.json():
		bot_message = i['text']
		print('Bot said: ' + str(bot_message + '\n'))


		# t2s = gTTS(text = bot_message)
		# t2s.save("t2s.mp3")
		# # Playing the converted file
		# subprocess.call(['mpg321', "t2s.mp3", '--play-and-exit'])