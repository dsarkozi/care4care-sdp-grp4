from time import strftime, gmtime
from C4CApplication.meta import NonMember#, SystemEmail
from C4CApplication.models import Message, Job, Branch, Mailbox
from C4CApplication import models


class Member(NonMember):
    """
    This class represents a kind of Users called Members
    """

    def create_job(self, branch_name, title, date=strftime('%Y-%m-%d', gmtime()), is_demand=False,\
                   comment=None, description='', start_time=0, frequency=0, km=0, duration=0, category=1,\
                   other_category='', place='', visibility='volunteer', recursive_day=''):
        """
        Creates a help offer (the parameters will be used to fill the database).

        :param branch_name: The branch to which belongs the job
        :param date: The date of the job
        :param is_demand: True if it's a demand, false otherwise
        :param comment: Comment of the job
        :param start_time: The hour of the beginning of the job in minute. Example : 14h30 -> 14*60+30 = 870
        :param frequency: The frequency of the job. (0=Once, 1=daily, 2=weekly, ...)
        :param km: The number of km to do the job
        :param duration: The duration to do the job
        :param category: The category of the job. (1=shopping, 2=visit, 3=transport)
        :param address: The address where the job will be done
        :param visibility: Which people can see the job.
        :return: False if there was a problem and True otherwise.
        """

        job = Job()
        job.title = title
        job.mail = self.db_member.mail
        n = 0
        jobs_created_by_me = Job.objects.filter(mail=self.db_member.mail)
        for j in jobs_created_by_me:
            if j.number > n:
                n = j.number
        job.number = n+1
        job.comment = comment
        job.description = description
        job.date = date
        job.start_time = start_time
        job.frequency = frequency
        job.recursive_day = recursive_day
        job.km = km
        job.duration = duration
        job.category = category
        job.other_category = other_category
        job.type = is_demand
        job.place = place
        job.visibility = Job.JOB_VISIBILITY[visibility]
        job.save()
        if branch_name is None:
            branch_name = self.db_member.branch[0]
        branch = Branch.objects.filter(name=branch_name)
        if len(branch) != 1:
            return False
        job.branch = branch[0]
        job.member_set.add(self.db_member)
        job.save()
        return job

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
        job.duration = new_time
        job.save()
        
        #We send a mail
        helper_mail = ''
        if not job.type : # offer
            helper_mail = job_creator_mail
        else : # demand
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

    def accept_bill(self, job_number, job_creator_mail, amount):
        """
        Accepts the bill and transfers money to the helper

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :param amount: amount of the bill
        :return: False if there was a problem and True otherwise.
        """
        job = Job.objects.filter(mail=job_creator_mail, number=job_number)
        if len(job) != 1:
            return False
        job = job[0]
        job.payed = True
        job.save()

        helper_mail = None
        if not job.type:  # offer
            helper_mail = job_creator_mail
        else:  # demand
            participants = job.member_set.all()
            for participant in participants:
                if participant.mail != self.db_member.mail:
                    helper_mail = participant.mail
                    break
        if helper_mail is None:
            return False
        helper = models.Member.objects.filter(mail=helper_mail)
        if len(helper) != 1:
            return False
        helper = helper[0]
        
        #We transfer money
        self.db_member.time_credit -= amount
        helper.time_credit += amount
        helper.save()
        self.db_member.save()
        
        #We send a mail to warn
        subject = "You've been payed"
        content = "You've been payed by "+str(self.db_member.mail)
        type = 3
        return self.send_mail(self.db_member.mail, helper.mail, subject, content, type)

    def refuse_bill(self, job_number, job_creator_mail):
        """
        Refuses the bill and warns the branch officer by email

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :return: False if there was a problem and True otherwise.
        """
        job = Job.objects.filter(mail=job_creator_mail, number=job_number)
        if len(job)!=1:
            return False
        job = job[0]
        mail_branch_officer = job.branch.branch_officer
        
        helper_email = None
        if not job.type:  # offer
            helper_email = job_creator_mail
        else:  # demand
            participants = job.member_set.all()
            for participant in participants:
                if participant.mail != self.db_member.mail:
                    helper_email = participant.mail
                    break
        
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
        if self.db_member.mail == destination_email:
            return False
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
        if len(branch) != 1:
            return False
        branch = branch[0]
        
        #We make the donation
        self.db_member.time_credit -= time
        branch.donation += time
        self.db_member.save()
        branch.save()
        return True
