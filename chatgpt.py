"""

Justin Hatch March 2, 2024

This project was copied from CS Coach's video 
"Creating Jarvis powered by OpenAI and Python | ChatGPT"

https://youtu.be/BEw5EFqCCEI?si=CRkYGo2kCsfJyo6p

This project intended to learn how to access/use API's
and how to use sound (in/out) in Python.

I have learned a lot from this project, coping it from CS coach. I hope 
to add facial recognition, and face ID systems to use this bot. I also would like to add automation ie, to send text/ email. This is just the beginning and hope to add/learn more to this
in the years to come

"""

from openai import OpenAI
import pyttsx3 
import speech_recognition as sr



client = OpenAI(

    api_key= "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"
)




def SpeakText(command):

    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

    return

r = sr.Recognizer()

def Record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration = 0.2)
                


                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)

                print(MyText)
                return MyText

        
        except sr.RequestError as e:
            print("couls not request: {0}".formate(e))

        except sr.UnknownValueError:
            print( "Unknown error")
            
def send_to_chatGPT(messages, model ="gpt-3.5-turbo"):

    response = client.chat.completions.create(

        model = model,
        messages = messages
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)

    return message

messages = [ ]

while (1):
    text = Record_text()
    messages.append({"role": "user", "content": text}) 
    response = send_to_chatGPT(messages)


    SpeakText(response)
    print(response)
    break
 
