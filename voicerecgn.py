#IMPORTAM BIBLIOTECILE NECESARE DUPA CE LE-AM INSTALAT CU PIP INSTALL
import speech_recognition as sr
import webbrowser as web
import os
import shutil

#CREAM FUNCTIA PRINCIPALA MAIN
def main():
    #SPECIFICAM SURSA BROWSERULUI PENTRU CAUTARI
    path="C:\Program Files\Google\Chrome\Application\chrome.exe %s"

    r=sr.Recognizer()

    with sr.Microphone() as source:
        #PENTRU INDEPARTAREA ZGOMOTULUI DE FUNDAL
        r.adjust_for_ambient_noise(source)

        print("spune ceva")
        #ASCULTA COMANDA
        audio=r.listen(source)

        print("identificare comanda...")

        try:
            #IDENTIFICAM COMANDA UTILIZAND GOOGLE SPEECH SI O DAM UNEI VARIABILE
            dest=r.recognize_google(audio)

            print("ai spus :"+dest)

            #PENTRU A SE PUTEA DESCHIDE VA ROG SA VA MODIFICATI LOCATIA FISIERULUI IN FUNCTIE DE NUMELE UTILIZATORULUI

            #DESCHIDEM NOTEPADUL

            if dest=='notepad':
                 os.startfile('C:\Proiect LP\proiectlp/requirements.txt')
                 try:
                    shutil.move("C://LP Folder test//Notepad.txt", "D://LP Folder test")
                 except:
                     print("Fisierul a fost deja mutat!")

            #DESCHIDEM FISIERUL PRIMIT DE LA MINE
            elif dest=='open lab':
                # os.startfile('C:\Proiect LP\proiectlp')
                os.startfile(('C:\\Users\\lenovo\\Desktop\\test'))
                try:
                    shutil.move("C://LP Folder test//Open Lab.txt", "D://LP Folder test")
                except:
                    print("Fisierul a fost deja mutat!")
            #DESCHIDEM WhatsApp
            elif dest=='call':
                os.startfile(r'C:\Users\lenovo\AppData\Local\WhatsApp\WhatsApp.exe')

                try:
                    shutil.move("C://LP Folder test//Whatsapp.txt", "D://LP Folder test")
                except:
                    print("Fisierul a fost deja mutat!")
            #DESCHIDEM ORICE ADRESA DE PE INTERNET CU SPECIFICAREA '.COM '
            #EXEMPLU : facebook.com , google.com etc
            else:
                web.open(dest)

                try:
                    shutil.move("C://LP Folder test//Pagina.com.txt", "D://LP Folder test")
                except:
                    print("Fisierul a fost deja mutat!")
            #exceptie in cazul in care nu recunoaste comanda
        except Exception as e:
            print("eroare"+str(e))

if __name__=="__main__":
     main()
