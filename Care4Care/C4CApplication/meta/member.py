from C4CApplication.meta import NonMember
from C4CApplication.models import Job, Branch
from C4CApplication import models


class Member(NonMember):
    """
    This class represents a kind of Users called Members
    """

    def accept_bill(self, job_number, job_creator_mail, amount):
        """
        Accepts the bill and transfers money to the helper

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :param amount: amount of the bill
        :return: False if there was a problem and True otherwise.
        """
        job = Job.objects.filter(mail=job_creator_mail, number=job_number)
        if len(job) != 1 or job[0].payed:
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

    def transfer_time(self, destination_email, time, message):
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
        content = "You've received a gift from "+str(sender_gift.mail)+'. Here is the message :\n' + message
        type = 3
        return self.send_mail(sender_gift.mail, receiver_gift.mail, subject, content, type)

    def make_donation(self, time, message, branch_name=None):
        """
        Makes a donation to the branch of the member

        :param branch_name:
        :param time:
        :return: True if donation proceeds correctly
        """
        branch = Branch.objects.filter(name=branch_name)
        if len(branch) != 1:
            return False
        branch = branch[0]
        branch_off = models.Member.objects.filter(mail=branch.branch_officer)
        if len(branch_off) != 1:
            return False
        branch_off=branch_off[0]
        if branch_off.mail == self.db_member.mail :
            return False
        #We make the donation
        self.db_member.time_credit -= time
        branch_off.time_credit += time
        branch.donation += time
        self.db_member.save()
        branch.save()
        branch_off.save()

        #Send the message
        subject = "Branch donation"
        content = "You've received a donation from "+str(self.db_member.mail)+'. Here is the message :\n' + message
        type = 3
        return self.send_mail(self.db_member.mail, branch_off.mail, subject, content, type)
