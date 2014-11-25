from time import strftime, gmtime
from C4CApplication.meta import NonMember#, SystemEmail
from C4CApplication.models import Message, Job, Branch, Mailbox
from C4CApplication import models


class Member(NonMember):
    """
    This class represents a kind of Users called Members
    """
    #TODO Why don't you put this on the specific file system_email ?
    def send_mail(self, sender_mail, receiver_mail, subject, content, type):
        """
        Send a mail from from_mail to to_mail, with the subject, 
        the content, and the type passed in parameter

        :param sender_mail: mail of the sender
        :param receiver_mail: mail of the receiver
        :param subject: subject of the mail
        :param content: content of the mail
        :param type: type of the mail
        :return: False if there was a problem and True otherwise
        """
        message = Message()
        member_sender = models.Member.objects.filter(mail=sender_mail)
        if len(member_sender)!=1 :
            return False
        message.member_sender = member_sender[0]
        n = 0
        list_message = member_sender[0].message_set.all()
        for m in list_message:
            if m.number > n:
                n = m.number
        message.number = n + 1
        message.subject = subject
        message.content = content
        message.type = type
        message.date = strftime('%Y-%m-%d', gmtime())  # TODO put this in a special module for simulation purposes
        message.save()
        
        mailbox = Mailbox()
        member_receiver = models.Member.objects.filter(mail=receiver_mail)
        if len(member_receiver) != 1:
            return False
        mailbox.member_receiver = member_receiver[0]
        mailbox.message = message
        member_sender[0].save()  # TODO Member sender or mailbox.member ???
        message.save()
        mailbox.save()
        
        return True

    def accept_help(self, job_number, job_creator_mail, helper_email):
        """
        Chooses the member (with email stored in 'helper_email') to do the job (with id stored in 'number')
        The chosen helper is warned by email

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :param helper_email:
        :return: False if there was a problem and True otherwise
        """
        job = Job.objects.filter(number=job_number, mail=job_creator_mail)
        if len(job) != 1:
            return False
        job = job[0]
        job.member_set.clear()  # We clear all relationships with the members (only one member can be accepted)
        creator = models.Member.objects.filter(mail=job.mail)  # TODO -> show : je pref des filter, ca ne crash pas ca.
        if len(creator) != 1:
            return False
        job.member_set.add(creator[0])  # We add the creator of the job
        helper = models.Member.objects.filter(mail=helper_email)
        if len(helper) != 1:
            return False
        job.member_set.add(helper[0])
        job.accepted = True
        job.save()
        
        # We send a mail
        subject = 'Your help is accepted'
        content = 'Congratulation ! Your help has been accepted by '+str(creator.mail)+' for the job '+str(job.id)
        type = 3
        return self.send_mail(creator.mail, helper.mail, subject, content, type)

    def create_job(self, branch_name, date=strftime('%Y-%m-%d', gmtime()), is_demand=False, comment=None, 
                   start_time=0, frequency=0, km=0, time=0, category=1, address=None, visibility='volunteer'):
        """
        Creates a help offer (the parameters will be used to fill the database).

        :param branch_name: The branch to which belongs the job
        :param date: The date of the job
        :param is_demand: True if it's a demand, false otherwise
        :param comment: Comment of the job
        :param start_time: The hour of the beginning of the job in minute. Example : 14h30 -> 14*60+30 = 870
        :param frequency: The frequency of the job. (0=Once, 1=daily, 2=weekly, ...)
        :param km: The number of km to do the job
        :param time: The time to do the job
        :param category: The category of the job. (1=shopping, 2=visit, 3=transport)
        :param address: The address where the job will be done
        :param visibility: Which people can see the job.
        :return: False if there was a problem and True otherwise.
        """

        # TODO Why my aggregate solution does not work :p ?
        job = Job()
        job.mail = self.db_member.mail
        n = 0
        jobs_created_by_me = Job.objects.filter(mail=self.db_member.mail)
        for j in jobs_created_by_me:
            if j.number > n:
                n = j.number
        job.number = n+1
        job.comment = comment
        job.date = date
        job.start_time = start_time
        job.frequency = frequency
        job.km = km
        job.time = time
        job.category = category
        job.type = is_demand
        job.address = address
        job.visibility = Job.JOB_VISIBILITY[visibility]
        job.save()
        branch = Branch.objects.filter(name=branch_name)
        if len(branch) != 1:
            return False
        job.branch = branch[0]
        job.member_set = self.db_member
        job.save()
        return True

    #TODO Where do you change the time ?
    def register_job_done(self, job_number, job_creator_mail, helped_one_email=None, new_time=0):
        """
        Registers a job as done (with the new time to put).
        The helped one will be warned by email and will be able to accept the 'payment' or not

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :param helped_one_email: it can't be None
        :param new_time:
        :return: False if there was a problem and True otherwise.
        """

        if helped_one_email is None:
            return False
        job = Job.objects.filter(mail=job_creator_mail, number=job_number)
        if len(job) != 1:
            return False
        job = job[0]
        job.done = True
        job.save()
        
        #We send a mail
        helper_mail = ''
        participants = job.member_set.all()
        for participant in participants:
            if participant.mail != helped_one_email:
                helper_mail = participant.mail
                break
        if helper_mail == '':
            return False
        subject = 'The job number '+str(job.id)+' is done'  # TODO Better to put the number I think...
        content = 'The job number '+str(job.id)+' is done. Please, consult your account to accept or not the bill'
        type = 1
        return self.send_mail(helper_mail, helped_one_email, subject, content, type)

    def accept_bill(self, job_number, job_creator_mail, helper_email, amount):
        """
        Accepts the bill and transfers money to the helper

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :param helper_email:
        :param amount: amount of the bill
        :return: False if there was a problem and True otherwise.
        """
        job = Job.objects.filter(mail=job_creator_mail, number=job_number)
        if len(job) != 1:
            return False
        job = job[0]
        job.payed = True
        job.save()
        
        helped_one = None  # TODO What ? -> the helped one is simply the self.db_member
        participants = job.member_set.all()
        for participant in participants:
            if participant.mail != helper_email:
                helper = participant  # TODO unused
                break
        if helped_one is None:
            return False
        helper = models.Member.objects.filter(mail=helper_email)
        if len(helper) != 1:
            return False
        helper = helper[0]
        
        #We transfer money
        helped_one.time_credit -= amount
        helper.time_credit += amount
        helper.save()
        helped_one.save()
        
        #We send a mail to warn
        subject = "You've been payed"
        content = "You've been payed by "+str(helped_one.mail)
        type = 3
        return self.send_mail(helped_one.mail, helper.mail, subject, content, type)

    def refuse_bill(self, job_number, job_creator_mail, helper_email):
        """
        Refuses the bill and warns the branch officer by email

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :param helper_email:
        :return: False if there was a problem and True otherwise.
        """
        job = Job.objects.filter(mail=job_creator_mail, number=job_number)
        if len(job)!=1:
            return False
        job = job[0]
        mail_branch_officer = job.branch.branch_officer
        
        #Send the mails
        subject = "bill refused"
        content = "Your bill has been refused by "+str(self.db_member.mail)
        type = 1
        res = self.send_mail(self.db_member.mail, helper_email, subject, content, type)
        if not res:
            return False
        
        content = "A bill has been refused by "+str(self.db_member.mail)
        return self.send_mail(self.db_member.mail, mail_branch_officer, subject, content, type)

    def transfer_time(self, destination_email, time):
        """
        Transfers 'time' to a member with 'destination_email' as email

        :param destination_email: the email address of the member to transfer time
        :return: False if there was a problem and True otherwise.
        """
        sender_gift = self.db_member
        receiver_gift = models.Member.objects.filter(mail=destination_email)
        if len(receiver_gift) != 1:
            return False
        receiver_gift = receiver_gift[0]
        
        sender_gift.time_credit -= time
        receiver_gift.time_credit += time
        sender_gift.save()
        receiver_gift.save()
        
        #Send the message
        subject = "You've received a gift"
        content = "You've received a gift from "+str(sender_gift.mail)
        type = 3
        return self.send_mail(sender_gift.mail, receiver_gift.mail, subject, content, type)

    def make_donation(self, time, branch_name=None):
        """
        Makes a donation to the branch of the member

        :param branch_name:
        :param time:
        :return:
        """
        branch = Branch.objects.filter(name=branch_name)
        if len(branch) == 0:  # <=> if branch_name==None
            branches_member = self.db_member.branch.all()  # We still try to find a branch
            if len(branches_member) != 1:
                return False
            else:
                branch = branches_member[0]
        
        #We make the donation
        self.db_member.time_credit -= time
        branch.donation += time
        self.db_member.save()
        branch.save()
        return True
