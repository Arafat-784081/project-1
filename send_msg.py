import pywhatkit
phone=input("Enter Phone Number: ")
message=input("Enter message: ")

pywhatkit.sendwhatmsg_instantly(phone,message,10)