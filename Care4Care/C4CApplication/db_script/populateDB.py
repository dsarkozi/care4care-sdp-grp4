from django.core.files import File
from C4CApplication.models import *


'''
Commande a executer dans le terminal :
exec(open('./C4CApplication/db_script/populateDB.py').read())
'''

def popule_db():
    #Suppression des messages pour eviter les conflits
    list_message = Message.objects.all()
    for message in list_message :
            message.delete()
    
    #Suppression des relations pour eviter les doublons
    list_relation = Relationship.objects.all()
    for relation in list_relation :
        relation.delete()
    
    #Suppression des jobs avant creation
    list_job = Job.objects.all()
    for job in list_job :
        job.delete()
    
    # Creation de membre
    m1 = Member(mail="kim.mens@gmail.com")
    m1.password = "azertyuiop"
    m1.first_name = "Kim"
    m1.last_name = "Mens"
    m1.birthday = "1967-10-03"
    m1.tag = Member.TAG['branch_officer']
    m1.mobile = "0477985632"
    m1.address = "Rue du Software, 3, Development, 2255"
    m1.time_credit = 59
    m1.visibility = Member.MEMBER_VISIBILITY['anyone']
    m1.save()
    
    m2 = Member(mail="yves.delaville@gmail.com")
    m2.password = "azertyuiop"
    m2.first_name = "Yves"
    m2.last_name = "Deville"
    m2.birthday = "1956-08-23"
    m2.tag = Member.TAG['branch_officer']
    m2.mobile = "0478745963"
    m2.address = "Rue de l'intelligence, 7, Artificial, 2261"
    m2.time_credit = 170
    m2.visibility = Member.MEMBER_VISIBILITY['anyone']
    m2.save()
    
    m3 = Member(mail="olivier.mauvaventure@gmail.com")
    m3.password = "azertyuiop"
    m3.first_name = "Olivier"
    m3.last_name = "Bonaventure"
    m3.picture = "images/images_profile/olivierbonaventuregmailcom.jpg"
    m3.birthday = "1970-05-25"
    m3.tag = Member.TAG['member']
    m3.mobile = "0476526987"
    m3.address = "Rue du Computer, 27, Network, 2141"
    m3.time_credit = 18
    m3.save()
    
    m4 = Member(mail="armand.bosquillon@student.uclouvain.be")
    m4.password = "azertyuiop"
    m4.first_name = "Armand"
    m4.last_name = "Bosquillon"
    path = "images/images_profile/%s" % (m4.mail)
    m4.picture = path.replace('@', '.').replace('.', '')+".jpg"
    m4.birthday = "1993-03-20"
    m4.tag = Member.TAG['member']
    m4.mobile = "0472695784"
    m4.address = "Rue de l'Eglise, 40, Rixensart, 1330"
    m4.time_credit = 9999
    m4.save()
    
    #path = './C4CApplication/static/images/armand.jpg'
    #photo = File(open(path))
    #m4.picture.save("armand.jpg", photo)
    #m4.picture = photo
    #m4.save()
    
    m5 = Member(mail="mathieu.jadin@student.uclouvain.be")
    m5.password = "azertyuiop"
    m5.first_name = "Mathieu"
    m5.last_name = "Jadin"
    path = "images/images_profile/%s" % (m5.mail)
    m5.picture = path.replace('@', '.').replace('.', '')+".jpg"
    m5.birthday = "1993-01-31"
    m5.tag = Member.TAG['bp_admin']
    m5.mobile = "0487793533"
    m5.address = "Rue du Leader, 3, LeaderVille, 2255"
    m5.time_credit = 10000000000
    m5.visibility = Member.MEMBER_VISIBILITY['anyone']
    m5.save()
    
    
    #Creation de branch
    b1 = Branch(name="LLN")
    b1.town = "Louvain-La-Neuve"
    b1.branch_officer = "kim.mens@gmail.com"
    m1.tag = 16
    b1.donation = 54
    b1.save()
    
    b2 = Branch(name="Nivelles")
    b2.town = "Nivelles"
    b2.branch_officer = "yves.deville@gmail.com"
    m2.tag = 16
    b2.donation = 10
    b2.save()
    
    #Lien membre et branch
    m1.branch.add(b1)
    m2.branch.add(b2)
    m3.branch.add(b1)
    m4.branch.add(b1)
    m5.branch.add(b1)
    m1.save()
    m2.save()
    m3.save()
    m4.save()
    m5.save()
    
    #Creation de messages
    e1 = Message()
    e1.member_sender = m3   #Olivier Bonaventure
    e1.number = 1
    e1.subject = "Comment faire une donation ?"
    e1.content = "Bonjour, j'aimerai savoir comment il faut proceder pour faire une donation ? Corialement, Olivier."
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
    
    #Suppression des mailbox pour eviter les doublons
    list_mailbox = Mailbox.objects.all()
    for mailbox in list_mailbox :
        mailbox.delete()
    
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
    
    r4 = Relationship()
    r4.member_source = m3   #Obo met Armand dans ses amis
    r4.member_target = m4
    r4.save()
    
    r5 = Relationship()
    r5.member_source = m3   #Obo met Yves dans ses amis
    r5.member_target = m2
    
    #Creation des jobs
    j1 = Job(mail="armand.bosquillon@student.uclouvain.be", number=1)
    j1.description = "Bonjour, j'ai besoin d'aide pour aller faire mes courses."
    j1.date = "2014-12-27"  #Samedi 27 decembre
    j1.start_time = 840 #14h *60
    j1.frenquency = 2   #Weekly
    j1.km = 30
    j1.time = 60    #1h *60
    j1.category = 1 #Shopping
    j1.type = True  #True = Demand
    j1.address = m4.address
    j1.branch = b1
    j1.save()
    j1.member_set.add(m4)
    j1.save()
    
    j2 = Job(mail="armand.bosquillon@student.uclouvain.be", number=2)
    j2.description = "Bonjour, j'ai besoin de quelqu'un pour m'amener a LLN exceptionnelement, \
                    car je n'ai pas de transport en commun ce jour la."
    j2.date = "2014-12-19"  #Lundi 19 decembre
    j2.start_time = 480 #8h *60
    j2.frenquency = 1   #Once
    j2.km = 30
    j2.time = 60    #1h *60
    j2.category = 3 #Transport
    j2.type = True  #True = Demand
    j2.address = m4.address
    j2.visibility = Job.JOB_VISIBILITY['favorites']
    j2.branch = b1
    j2.save()
    j2.member_set.add(m4)
    j2.member_set.add(m2)
    j2.member_set.add(m3)
    j2.save()
    
    j3 = Job(mail="olivier.bonaventure@gmail.com", number=1)
    j3.description = "Bonjour, j'aimerai visiter l'Atomium, mais je ne veux pas le faire seul.\
                    Quelqu'un pour m'accompagner ?"
    j3.date = "2015-01-27"  #Mardi 27 janvier
    j3.start_time = 600 #10h *60
    j3.frenquency = 1   #Once
    j3.km = 50
    j3.time = 120    #2h *60
    j3.category = 2 #Transport
    j3.type = True  #True = Demand
    j3.address = "Square de l'Atomium, B-1020 BRUXELLES"
    j3.accepted = True
    j3.visibility = Job.JOB_VISIBILITY['favorites']
    j3.branch = b1
    j3.save()
    j3.member_set.add(m3)
    j3.member_set.add(m2)
    j3.save()
    
    j4 = Job(mail="yves.deville@gmail.com", number=1)
    j4.description = "Bonjour, j'aimerai quelqu'un pour me conduire a Bruxelles"
    j4.date = "2015-01-29"  #Jeudi 29 janvier
    j4.start_time = 540 #9h *60
    j4.frenquency = 1   #Once
    j4.km = 50
    j4.time = 120    #2h *60
    j4.category = 2 #Transport
    j4.type = True  #True = Demand
    j4.address = "Square de l'Atomium, B-1020 BRUXELLES"
    j4.accepted = True
    j4.done = True
    j4.branch = b1
    j4.save()
    j4.member_set.add(m2)
    j4.member_set.add(m1)
    j4.save()
    
    j5 = Job(mail="kim.mens@gmail.com", number=1)
    j5.description = "Bonjour, j'aimerai quelqu'un pour me conduire a Bruxelles.\
                    Plus precisement, a l'universite de Bruxelles."
    j5.date = "2014-12-09"  #Vendredi 9 janvier
    j5.start_time = 540 #9h *60
    j5.frenquency = 1   #Once
    j5.km = 50
    j5.time = 60    #1h *60
    j5.category = 2 #Transport
    j5.type = True  #True = Demand
    j5.address = "Avenue Franklin Roosevelt 50 - 1050 Bruxelles"
    j5.accepted = True
    j5.done = True
    j5.done = True
    j5.branch = b1
    j5.save()
    j5.member_set.add(m1)
    j5.member_set.add(m4)
    j5.save()
    
    j6 = Job(mail="armand.bosquillon@student.uclouvain.be", number=3)
    j6.description = "Bonjour, je met a disposition mon aide pour faire du shopping a l'Esplanade."
    j6.date = "2015-01-24"  #Samedi 24 janvier
    j6.start_time = 780 #13h *60
    j6.frenquency = 1   #Once
    j6.km = 0
    j6.time = 240    #4h *60
    j6.category = 1 #Transport
    j6.type = False  #False = Offer
    j6.address = "Place de l'Accueil, 10 bte 1, 1348, Louvain-la-Neuve"
    j6.branch = b1
    j6.save()
    j6.member_set.add(m4)
    j6.save()
    
    j7 = Job(mail="mathieu.jadin@student.uclouvain.be", number=1)
    j7.description = "Bonjour, je met a disposition mon aide pour le projet Care4Care."
    j7.date = "2014-12-05"  #Vendredi 5 Decambre
    j7.start_time = 480 #8h *60
    j7.frenquency = 1   #Once
    j7.km = 0
    j7.time = 2520    #4h *60
    j7.category = 1 #Transport
    j7.type = False  #False = Offer
    j7.address = "Place Sainte Barbe, 2 bte L6.11.01 B-1348 Louvain-la-Neuve, Salle Intel"
    j7.branch = b1
    j7.save()
    j7.member_set.add(m5)
    j7.save()
    
    
    
popule_db()