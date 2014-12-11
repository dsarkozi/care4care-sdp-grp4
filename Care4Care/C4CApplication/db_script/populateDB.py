from C4CApplication.models import *


'''
Command to execute in terminal :
exec(open('./C4CApplication/db_script/populateDB.py').read())
'''

def popule_db():
    #Delete all members
    list_member = Member.objects.all()
    for member in list_member:
        member.delete()
        
    #Delete all branches
    list_branch = Branch.objects.all()
    for branch in list_branch:
        branch.delete()
    
    #Delete all messages to avoid conflicts
    list_message = Message.objects.all()
    for message in list_message :
            message.delete()
            
    #Delete all mailbox to avoid duplication
    list_mailbox = Mailbox.objects.all()
    for mailbox in list_mailbox :
        mailbox.delete()
    
    #Delete all relations to avoid duplication
    list_relation = Relationship.objects.all()
    for relation in list_relation :
        relation.delete()
    
    #Delete jobs before creation
    list_job = Job.objects.all()
    for job in list_job :
        job.delete()
    
    # Creation of members
    m1 = Member(mail="kim.mens@gmail.com")
    m1.password = "azertyuiop"
    m1.first_name = "Kim"
    m1.last_name = "Mens"
    m1.gender = 'M'
    m1.birthday = "1967-10-03"
    m1.tag = Member.TAG['branch_officer']
    m1.mobile = "0477985632"
    m1.street = "Rue du Software, 3"
    m1.zip = "2255"
    m1.town = "Development"
    m1.time_credit = 59
    m1.visibility = Member.MEMBER_VISIBILITY['anyone']
    m1.save()
    
    m2 = Member(mail="yves.delaville@gmail.com")
    m2.password = "azertyuiop"
    m2.first_name = "Yves"
    m2.last_name = "Delaville"
    m2.gender = 'M'
    m2.birthday = "1956-08-23"
    m2.tag = Member.TAG['branch_officer']
    m2.mobile = "0478745963"
    m2.street = "Rue de l'intelligence, 7"
    m2.zip = "2261"
    m2.town = "Artificial"
    m2.time_credit = 170
    m2.visibility = Member.MEMBER_VISIBILITY['anyone']
    m2.save()
    
    m3 = Member(mail="olivier.mauvaisaventure@gmail.com")
    m3.password = "azertyuiop"
    m3.first_name = "Olivier"
    m3.last_name = "Mauvaisaventure"
    m3.gender = 'M'
    m3.birthday = "1970-05-25"
    m3.tag = Member.TAG['member']
    m3.mobile = "0476526987"
    m3.street = "Rue du Computer, 27"
    m3.zip = "2141"
    m3.town= "Network"
    m3.time_credit = 18
    m3.save()
    
    m4 = Member(mail="armand.bosquillon@student.uclouvain.be")
    m4.password = "azertyuiop"
    m4.first_name = "Armand"
    m4.last_name = "Bosquillon"
    m4.gender = 'M'
    path = "images/images_profile/%s" % (m4.mail)
    m4.picture = path.replace('@', '.').replace('.', '')+".jpg"
    m4.birthday = "1993-03-20"
    m4.tag = Member.TAG['member']
    m4.mobile = "0472695784"
    m4.street = "Rue de l'Eglise, 40"
    m4.zip = "1330"
    m4.town = "Rixensart"
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
    m5.gender = 'M'
    path = "images/images_profile/%s" % (m5.mail)
    m5.picture = path.replace('@', '.').replace('.', '')+".jpg"
    m5.birthday = "1993-01-31"
    m5.tag = Member.TAG['bp_admin']
    m5.mobile = "0487793533"
    m5.street = "Rue du Leader, 3"
    m5.zip = "2255"
    m5.town = "LeaderVille"
    m5.time_credit = 10000000000
    m5.visibility = Member.MEMBER_VISIBILITY['anyone']
    m5.save()
    
    m6 = Member(mail="dr.robotnik@gmail.com")
    m6.password = "azertyuiop"
    m6.first_name = "Docteur"
    m6.last_name = "Robotnik"
    m6.gender = 'M'
    m6.birthday = "1957-11-23"
    m6.tag = Member.TAG['non_member']
    m6.mobile = "0477987632"
    m6.street = "Boosaardigheidstraat, 3"
    m6.zip = "8500"
    m6.town = "Nivelles"
    m6.time_credit = -999999
    m6.visibility = Member.MEMBER_VISIBILITY['anyone']
    m6.save()
    
    
    #Creation de branch
    b1 = Branch(name="LLN")
    b1.branch_town = "Louvain-La-Neuve"
    b1.branch_officer = "kim.mens@gmail.com"
    m1.tag = 16
    b1.donation = 54
    b1.save()
    
    b2 = Branch(name="Nivelles")
    b2.branch_town = "Nivelles"
    b2.branch_officer = "yves.delaville@gmail.com"
    m2.tag = 16
    b2.donation = 10
    b2.save()
    
    #Link member and branch
    m1.branch.add(b1)
    m2.branch.add(b2)
    m3.branch.add(b1)
    m4.branch.add(b1)
    m5.branch.add(b1)
    m6.branch.add(b2)
    m1.save()
    m2.save()
    m3.save()
    m4.save()
    m5.save()
    m6.save()
    
    #Creation of messages
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
    
    #Creation of mailboxes
    a1 = Mailbox()  # message e1 for Kim Mens
    a1.member_receiver = m1  #Kim Mens
    a1.message = e1
    a1.save()
    
    a2 = Mailbox()
    a2.member_receiver = m2 #Yves Devilles
    a2.message = e2
    a2.save()
    
    #Creation of relations between members
    r1 = Relationship()
    r1.member_source = m4   #Armand put Obo in his friends
    r1.member_target = m3
    r1.save()
    
    r2 = Relationship()
    r2.member_source = m4   #Armant put Yves in his friends
    r2.member_target = m2
    r2.save()
    
    r3 = Relationship()
    r3.member_source = m1   #Kim put Obo in his friends
    r3.member_target = m3
    r3.save()
    
    r4 = Relationship()
    r4.member_source = m3   #Obo put Armand in his friends
    r4.member_target = m4
    r4.save()
    
    r5 = Relationship()
    r5.member_source = m3   #Obo put Yves in his friends
    r5.member_target = m2
    
    #Creation of jobs
    j1 = Job(mail=m4.mail, number=1)   #Armand
    j1.title = "Aide pour mes courses"
    j1.description = "Bonjour, j'ai besoin d'aide pour aller faire mes courses."
    j1.date = "2014-12-27"  #Samedi 27 decembre
    j1.start_time = 840 #14h *60
    j1.frequency = 0   #Once
    j1.km = 30
    j1.duration = 60    #1h *60
    j1.category = 1 #Shopping
    j1.type = True  #True = Demand
    j1.visibility = 1
    j1.place = "%s, %s, %s" % (m4.street, m4.zip, m4.town)
    j1.branch = b1
    j1.save()
    j1.member_set.add(m4)
    j1.save()
    
    j2 = Job(mail=m4.mail, number=2)   #Armand
    j2.title = "Me conduire a LLN"
    j2.description = "Bonjour, j'ai besoin de quelqu'un pour m'amener a LLN exceptionnelement, \
                    car je n'ai pas de transport en commun ce jour la."
    j2.date = "2014-12-19"  #Lundi 19 decembre
    j2.start_time = 480 #8h *60
    j2.frequency = 0   #Once
    j2.km = 30
    j2.duration = 60    #1h *60
    j2.category = 3 #Transport
    j2.type = True  #True = Demand
    j2.visibility = 1
    j2.place = "%s, %s, %s" % (m4.street, m4.zip, m4.town)
    j2.visibility = Job.JOB_VISIBILITY['favorites']
    j2.branch = b1
    j2.save()
    j2.member_set.add(m4)
    j2.member_set.add(m2)
    j2.member_set.add(m3)
    j2.save()
    
    j3 = Job(mail=m3.mail, number=1)    #Olivier
    j3.title = "Visiter l'Atomium"
    j3.description = "Bonjour, j'aimerai visiter l'Atomium, mais je ne veux pas le faire seul.\
                    Quelqu'un pour m'accompagner ?"
    j3.date = "2015-01-27"  #Mardi 27 janvier
    j3.start_time = 600 #10h *60
    j3.frequency = 0   #Once
    j3.km = 50
    j3.duration = 120    #2h *60
    j3.category = 2 #Visite
    j3.type = True  #True = Demand
    j3.place = "Square de l'Atomium, 1020, Bruxelles"
    j3.accepted = True
    j3.visibility = Job.JOB_VISIBILITY['favorites']
    j3.branch = b1
    j3.save()
    j3.member_set.add(m3)
    j3.member_set.add(m2)
    j3.save()
    
    j4 = Job(mail=m2.mail, number=1) #Yves
    j4.title = "Me conduire a Bruxelles"
    j4.description = "Bonjour, j'aimerai quelqu'un pour me conduire a Bruxelles"
    j4.date = "2015-01-29"  #Jeudi 29 janvier
    j4.start_time = 540 #9h *60
    j4.frequency = 0   #Once
    j4.km = 50
    j4.duration = 120    #2h *60
    j4.category = 3 #Transport
    j4.type = True  #True = Demand
    j4.place = "Square de l'Atomium, 1020, Bruxelles"
    j4.accepted = True
    j4.done = True
    j4.branch = b1
    j4.save()
    j4.member_set.add(m2)
    j4.member_set.add(m1)
    j4.save()
    
    j5 = Job(mail=m1.mail, number=1)    #Kim
    j5.title = "Me conduire a l'universite de Bruxelles"
    j5.description = "Bonjour, j'aimerai quelqu'un pour me conduire a Bruxelles.\
                    Plus precisement, a l'universite de Bruxelles."
    j5.date = "2014-12-09"  #Vendredi 9 janvier
    j5.start_time = 540 #9h *60
    j5.frequency = 0   #Once
    j5.km = 50
    j5.duration = 60    #1h *60
    j5.category = 3 #Transport
    j5.type = True  #True = Demand
    j5.place = "Avenue Franklin Roosevelt, 50, 1050, Bruxelles"
    j5.accepted = True
    j5.done = True
    j5.done = True
    j5.branch = b1
    j5.save()
    j5.member_set.add(m1)
    j5.member_set.add(m4)
    j5.save()
    
    j6 = Job(mail=m4.mail, number=3)   #Armand
    j6.title = "Aide shopping Esplanade"
    j6.description = "Bonjour, je met a disposition mon aide pour faire du shopping a l'Esplanade."
    j6.date = "2015-01-24"  #Samedi 24 janvier
    j6.start_time = 780 #13h *60
    j6.frequency = 0   #Once
    j6.km = 0
    j6.duration = 240    #4h *60
    j6.category = 1 #Shopping
    j6.type = False  #False = Offer
    j6.visibility = 1
    j6.place = "Place de l'Accueil, 10 bte 1, 1348, Louvain-la-Neuve"
    j6.branch = b1
    j6.save()
    j6.member_set.add(m4)
    j6.save()
    
    j7 = Job(mail=m5.mail, number=1)    #Mathieu Jadin
    j7.title = "Aide Care4Care"
    j7.description = "Bonjour, je met a disposition mon aide pour le projet Care4Care."
    j7.date = "2014-12-05"  #Vendredi 5 Decambre
    j7.start_time = 480 #8h *60
    j7.frequency = 0   #Once
    j7.km = 0
    j7.duration = 2520    #4h *60
    j7.category = 4 #Other
    j7.other_category = "Aide informatique"
    j7.type = False  #False = Offer
    j7.visibility = 1
    j7.place = "Place Sainte Barbe, 2 bte L6.11.01, Salle Intel, 1348, Louvain-la-Neuve"
    j7.branch = b1
    j7.save()
    j7.member_set.add(m5)
    j7.save()
    
    j8 = Job(mail=m1.mail, number=2)    #Kim
    j8.title = "Projet Care4Care"
    j8.description = "Bonjour, je donne mon aide pour le projet de Care4Care"
    j8.start_time = 510 #8h30
    j8.frequency = 1    #Weekly
    j8.recursive_day = "0"
    j8.km = 0
    j8.duration = 120   #2h
    j8.category = 4 #Other
    j8.other_category = "Aide projet"
    j8.type = False #False = Offer
    j8.visibility = 1
    j8.place = "Place Sainte Barbe, 2 bte L6.11.01, Barb93, 1348, Louvain-la-Neuve"
    j8.branch = b1
    j8.save()
    j8.member_set.add(m1)
    j8.save()
    
    j9 = Job(mail=m1.mail, number=3)    #Kim
    j9.title = j8.title
    j9.description = j8.description
    j9.date = "2014-12-29"
    j9.start_time = j8.start_time #8h30
    j9.frequency = 0    #Once
    j9.km = j8.km
    j9.duration = j8.duration   #2h
    j9.category = j8.category #Other
    j9.other_category = j8.other_category
    j9.type = j8.type
    j9.visibility = j8.visibility
    j9.place = j8.place
    j9.branch = j8.branch
    j9.regular_job = j8
    j9.save()
    j9.member_set.add(m1)
    j9.member_set.add(m4)
    j9.save()
    
    j10 = Job(mail=m2.mail, number=2)    #Kim
    j10.title = "Projet Zombies"
    j10.description = "Bonjour, je donne mon aide pour le projet de Zombies"
    j10.start_time = 510 #8h30
    j10.frequency = 2    #Monthly
    j10.recursive_day = "10, 20, 30"
    j10.km = 0
    j10.duration = 120   #2h
    j10.category = 4 #Other
    j10.other_category = "Aide projet"
    j10.type = False #False = Offer
    j10.visibility = 1
    j10.place = "Place Sainte Barbe, 2 bte L6.11.01, Barb01, 1348, Louvain-la-Neuve"
    j10.branch = b1
    j10.save()
    j10.member_set.add(m2)
    j10.save()
    
    j11 = Job(mail=m2.mail, number=3)    #Kim
    j11.title = j10.title
    j11.description = j10.description
    j11.date = "2014-12-20"
    j11.start_time = j10.start_time #8h30
    j11.frequency = 0    #Once
    j11.km = j10.km
    j11.duration = j10.duration   #2h
    j11.category = j10.category #Other
    j11.other_category = j10.other_category
    j11.type = j10.type
    j11.visibility = j10.visibility
    j11.place = j10.place
    j11.branch = j10.branch
    j11.regular_job = j10
    j11.save()
    j11.member_set.add(m2)
    j11.member_set.add(m4)
    j11.save()
    
    
popule_db()