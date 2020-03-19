#Gives the current time. 
import time
import os
from google.cloud import texttospeech
from pygame import mixer

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/Yathartha/Documents/codes/myenv/project/files/My First Project-1cc2e314e6fa.json'

def playSound(sound):
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play()

def mainSpeech(textInput, file_name):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=textInput)

    # Build the voice request, select the language code ("en-US")
    # ****** the NAME
    # and the ssml voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        name='en-US-Wavenet-F',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    #response.speak()
    # The response's audio_content is binary.
    with open(file_name, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        #print('Audio content written to file "output.mp3"')



#mainSpeech("My name is yathartha regmi")
#playSound()
