from django.test import TestCase
from C4CApplication.models import *


'''
Commande a executer dans le terminal :
exec(open('./C4CApplication/tests/populateDB.py').read())
'''

# Creation de membre
m1 = Member()
m1.mail = "kim.mens@gmail.com"
m1.first_name = "Kim"
m1.last_name = "Mens"
m1.birthday = "1967-10-03"
m1.tag = Member.TAG['member']
m1.mobile = "0477985632"
m1.address = "Rue du Software, 3, Development, 2255"
m1.time_credit = 59
m1.save()

m2 = Member()
m2.mail = "yves.deville@gmail.com"
m2.first_name = "Yves"
m2.last_name = "Deville"
m2.birthday = "1956-08-23"
m2.tag = Member.TAG['member']
m2.mobile = "0478745963"
m2.address = "Rue de l'intelligence, 7, Artificial, 2261"
m2.time_credit = 170
m2.save()

m3 = Member()
m3.mail = "olivier.bonaventure@gmail.com"
m3.first_name = "Olivier"
m3.last_name = "Bonaventure"
m3.birthday = "1970-05-25"
m3.tag = Member.TAG['member']
m3.mobile = "0476526987"
m3.address = "Rue du Computer, 27, Network, 2141"
m3.time_credit = 18
m3.save()

m4 = Member()
m4.mail = "armand.bosquillon@student.uclouvain.be"
m4.first_name = "Armand"
m4.last_name = "Bosquillon"
m4.birthday = "1993-03-20"
m4.tag = Member.TAG['member']
m4.mobile = "0472695784"
m4.address = "Rue de l'Eglise, 40, Rixensart, 1330"
m4.time_credit = 9999
m4.save()


#Creation de branch
b1 = Branch()
b1.name = "LLN"
b1.town = "Louvain-La-Neuve"
b1.mail = "kim.mens@gmail.com"
b1.donation = 54
b1.save()

b2 = Branch()
b2.name = "Nivelles"
b2.town = "Nivelles"
b2.mail = "yves.deville@gmail.com"
b2.donation = 10
b2.save()

#Lien membre et branch
m1.branch.add(b1)
m2.branch.add(b2)
m3.branch.add(b1)
m1.save()
m2.save()
m3.save()

#Suppression des messages pour eviter les conflits
list_message = Message.objects.all()
for message in list_message :
        message.delete()

#Creation de messages
e1 = Message()
e1.member_sender = m3   #Olivier Bonaventure
e1.number = 1
e1.subject = "Comment faire une donation ?"
e1.content = "Bonjour, j'aimerai savoir comment il faut procéder pour faire une donation ? Corialement, Olivier."
e1.type = 2
e1.date = "2014-11-20"
e1.save()

e2 = Message()
e2.member_sender = m3   #Olivier Bonaventure
e2.number = 2
e2.subject = "Rejoindre votre branch ?"
e2.content = "Bonjour, j'aimerai savoir s'il est possible de rejoindre votre branch, et si oui, comment ? Corialement, Olivier."
e2.type = 2
e2.date = "2014-11-03"
e2.save()

#Creation des mailboxs
a1 = Mailbox()  # message e1 pour Kim Mens
a1.member_receiver = m1  #Kim Mens
a1.message = e1
a1.save()

a2 = Mailbox()
a2.member_receiver = m2 #Yves Devilles
a2.message = e2
a2.save()

#Creation des relations entre les membres
r1 = Relationship()
r1.member_source = m4   #Armand met Obo dans ses amis.
r1.member_target = m3
r1.save()

r2 = Relationship()
r2.member_source = m4   #Armant met Yves dans ses amis
r2.member_target = m2
r2.save()

r3 = Relationship()
r3.member_source = m1   #Kim met Obo dans ses amis
r3.member_target = m3
r3.save()