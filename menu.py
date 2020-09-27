import webbrowser
import speech_recognition as sr
print("welcome to my tools\n\n")
print("Enter your requirements.......we r listening.....", end='')
#ch=input()
r = sr.Recognizer()
with sr.Microphone() as source :
    print('start saying......')
    audio  =r.listen(source)
    print('we got it,plz wait.....')
ch=r.recognize_google(audio)
if  ('date'in ch)and ('run' in ch) or ('execute' in ch): 
	webbrowser.open("http://192.168.43.229/cgi-bin/iiec.py?x=date&p=") 
elif ('calender' in ch) and ('run' in ch)or ('execute' in ch):
	webbrowser.open("http://192.168.43.229/cgi-bin/iiec.py?x=cal&p=")
else:
	print("not uderstand")
      