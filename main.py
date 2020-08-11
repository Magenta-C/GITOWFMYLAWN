
import random_poem
from time import sleep


import smtplib, ssl

port = 465  # For SSL
password = "s4UfZBfN9Swzztd"

context = ssl.create_default_context()



PC = 0

'''def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems'''


print("I'm QWERT the freindly poem loving chatbot")
print("What is your name?")
name = input()
print(name, "is a nice name")
print("do you want a poem? (yes or no)")
poem = input()
if poem == "yes":
  print("here is a poem, it reads:", random_poem.get_poem())
  print("Do you want a poem sent to your email? (yes or no)")
  Eyn = input()
  if Eyn == "yes":
    print("how many Poems?")
    PC = input(int)
    PC1 = int(PC)
    print("what is your email?")
    EMAIL = input()

    while PC1 >= 1:
      with smtplib.SMTP_SSL(EMAIL, port, context=context) as server:
        server.login("peombot@gmail.com", password)
    # TODO: Send email here
      PC -= 1
      sleep(0.5)
elif poem == "no":
  print("You are no friend of mine")
else:
  print("Speak louder please")




import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)
    # TODO: Send email here
