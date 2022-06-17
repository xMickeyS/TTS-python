from gtts import gTTS
import playsound
import os 

###      methods    ####

def tts(mes):
    speech = gTTS(text = mes, lang = "en", slow = False)
    speech.save("TTS.mp3")
    playsound.playsound("TTS.mp3", True)
    os.remove("TTS.mp3") # I can't playsound seraval times so I decided to delete it every time

def mesRemoveLink(toSpeak):
    index = toSpeak.find("https://")
    if index >= 0:
        rawlink = toSpeak[index:len(toSpeak)]
        link = rawlink[:rawlink.find(" ")]
        toSpeak = toSpeak.replace(link,"")      
        return mesRemoveLink(toSpeak)
    return toSpeak

def mesRemoveEmoji(toSpeak):
    index = toSpeak.find("<")
    if index >= 0:
        rawtext = toSpeak[index:len(toSpeak)]
        emoji = rawtext[:rawtext.find(">")+1]
        toSpeak = toSpeak.replace(emoji,"emoji")
        return mesRemoveEmoji(toSpeak)
    return toSpeak

def mesCheck(loopInput):
    print("Please fill out the input in this format.\nname:message") #you can change it later
    for i in range(loopInput): 
        name, text = input().split(":")
        toSpeak = mesRemoveLink(text)
        toSpeak = mesRemoveEmoji(toSpeak)
        tts(toSpeak)
        
loopInput = int(input("How many times will you enter word?: "))
mesCheck(loopInput)