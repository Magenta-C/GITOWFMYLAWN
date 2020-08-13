# -*- coding: utf-8 -*-

import random_poem
from random import randint
from time import sleep
import smtplib, ssl
from tinydb import TinyDB, Query
port = 465  # For SSL
password = "s4UfZBfN9Swzztd"
context = ssl.create_default_context()
PC = 0
print("I'm QWERT the freindly poem loving chatbot")
print("What is your name?")
name = input()
print(name, "is a nice name")
print("do you want a poem? (yes or no)")
poem = input()
if 'yes' in poem:
  print("here is a poem, it reads:")
  print(random_poem.get_poem())
  print("")
  print("Do you want a poem sent to your email? (yes or no)")
  Eyn = input()
  if 'yes' in Eyn:
    print("")
    print("how many Poems?")
    PC = input()
    PC1 = int(PC)
    print("")
    print("what is your email?")
    EMAIL = input()
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login("peombot@gmail.com", "s4UfZBfN9Swzztd")
        subj3ct = name, "just asked for a poem"
        emsg = f'Subject: {subj3ct} \n\n{EMAIL}'
        smtp.sendmail("peombot@gmail.com", "theverymagentapuppy@gmail.com", emsg)
    while PC1 >= int(1):
      with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        ranpm = random_poem.get_poem()
        smtp.login("peombot@gmail.com", "s4UfZBfN9Swzztd")
        subject = 'Here is your poem', name
        ranpom = ranpm.encode('utf-8')
        Emsg = f'Subject: {subject} \n\n{ranpom}'
        smtp.sendmail("peombot@gmail.com", EMAIL, Emsg)
      print("done email", PC1)
      PC1 -= 1
    print("I made same poems for you, do you want to see them? (yes or no)") 
    AIPOM = input()
    if 'yes' in AIPOM:
      db = TinyDB('AI_Poem_DataBase.json')
      db.update({'\n': 'SHEEPDADOOP'})
      poemAi = Query()
      #db.search(poemAi.id == randint(0, 36))
      ghff = db.get(poemAi.id == randint(0, 36))
      print(ghff)
elif poem == "no":
  print("You are no friend of mine")
else:
  print("Speak louder please")