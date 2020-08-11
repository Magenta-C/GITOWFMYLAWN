from cheesefactory-Email import Email
import random_poem



import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
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
    return problems



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
    email = Email(
    recipients=['bob@example.com',],
    host='localhost',
    port='25',
    username='Peom Bot',
    password='s4UfZBfN9Swzztd',
    sender='peombot@gmail.com',
    subject='here is your poem',
    body= random_poem.get_poem(),
    use_tls=False,
    attachments=['file1.txt', 'file2.txt']
    )
elif poem == "no":
  print("You are no friend of mine")
else:
  print("Speak louder please")