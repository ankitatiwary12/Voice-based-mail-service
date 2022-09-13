import pyttsx3
import speech_recognition as sr
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 180)

def speak(sentence):

    engine.say(sentence)
    print("Machine said:" + sentence)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Reocgnizing ....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        speak("say that again please ...")
        return "none"
    query = query.lower()
    return query
def mail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    sender_mail_id = "your mail id"
    password = "your password"
    mail_id_list = {"Ankita": "ankitatiwary14@gmail.com",
                    "diwesh": "singhdiwesh104@gmail.com",
                    "Aditya": "aditya.kumar.6nov@gmail.com"
                    }

    speak("Hello sir, who do you want to send mail?")
    receiver_mail_id = takeCommand()

    s.starttls()

    s.login(sender_mail_id, password)
    speak("What is the email body?")
    message = takeCommand()
    s.sendmail(sender_mail_id, receiver_mail_id, message)
    speak("sending mail...")
    s.quit()
    speak("mail sent succesfully")


if __name__ == '__main__':
    mail()
