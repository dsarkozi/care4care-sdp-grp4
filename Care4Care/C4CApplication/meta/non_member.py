from time import strftime, gmtime
from C4CApplication.meta import User
from C4CApplication.models import Job, Member, Branch, Message, Mailbox
from django.db.models import Max
from C4CApplication.models.relationship import Relationship


class NonMember(User):
    """
    This class represents a kind of Users called Non Members
    """

    def __init__(self, db_member):
        self.db_member = db_member
        
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
        member_sender = Member.objects.filter(mail=sender_mail)
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
        member_receiver = Member.objects.filter(mail=receiver_mail)
        if len(member_receiver) != 1:
            return False
        mailbox.member_receiver = member_receiver[0]
        mailbox.message = message
        member_sender[0].save()  # TODO Member sender or mailbox.member ???
        message.save()
        mailbox.save()
        
        return True

    def is_job_visible(self, job, db_member):
        """
        :param job:
        :param db_member:
        :return: True if the job created by the member is visible
        """

        #This line have to change if we add the personal network
        return job.visibility & Job.JOB_VISIBILITY['anyone'] == 1\
               or (job.visibility & Job.JOB_VISIBILITY['favorites'] == 1
                   and db_member.is_favorite(self.db_member))\
               or db_member == self.db_member

    def see_job_details(self, job_number, job_creator_mail):
        """
        :param job_number: id of the job to return
        :param job_creator_mail: the email of the 'owner' of the job
        :return: the instance of Job object represented by the 'job_number' if the user can see it
                        otherwise, it returns None
        """
        return self.see_job_details_base(job_number, job_creator_mail, self.is_job_visible)

    def see_job_details_base(self, job_number, job_creator_mail, function):
        """
        :param job_number: id of the job to return
        :param job_creator_mail: the email of the 'owner' of the job
        :param function: the function to check visibility of the job
        :return: the instance of Job object represented by the 'job_number' if the user can see it
                        otherwise, it returns None
        """

        job_list = Job.objects.filter(number=job_number, mail=job_creator_mail)
        if len(job_list) == 0:
            return None

        db_member = (Member.objects.filter(mail=job_list.mail))[0]

        if function(job_list[0], db_member):
            return job_list[0]
        else:
            return None

    def get_visible_job_list(self, show_offers):
        """
        :param show_offers: the type of the list of the jobs to return
        :return: the list of Job objects visible by the user
            (offers if 'show_offers' is true and otherwise the demands)
        """
        return self.get_visible_job_list_base(show_offers, self.is_job_visible)

    def get_visible_job_list_base(self, show_offers, function):
        """
        :param show_offers: the type of the list of the jobs to return
        :param function: the function to check visibility of the job
        :return: the list of Job objects visible by the user
            (offers if 'show_offers' is true and otherwise the demands)
        """

        jobs_list = Job.objects.filter(type=show_offers)
        if len(jobs_list) == 0:
            return []
        
        filtered_jobs_list = []
        for job in jobs_list :
            db_member = (Member.objects.filter(mail=job.mail))[0]
            if function(job, db_member):
                filtered_jobs_list.append(job)

        return filtered_jobs_list
    
    def get_involved_job_list(self, show_offers):
        """
        :param show_offers: the type of the list of the jobs to return
        :return: the list of Job objects in which the user is involved
            (offers if 'show_offers' is true and otherwise the demands)
        """
        jobs_list = Job.objects.filter(type=show_offers)
        if len(jobs_list) == 0:
            return []
        
        filtered_jobs_list = []
        for job in jobs_list :
            if self.db_member == job.member_set[0] or self.db_member == job.member_set[1] :
                filtered_jobs_list.append(job)

        return filtered_jobs_list

    def accept_job(self, job_number, job_creator_mail):
        """
        Puts the member on the list of possible helpers for a pending job.
        The helped one will be warned by email (this email is the parameter 'job_creator_mail').

        :param job_number: the if of the job to accept
        :param job_creator_mail: the email of the 'owner' of the job
        :return: False if there was a problem and True otherwise
        """
        return self.accept_job_base(job_number, job_creator_mail, self.is_job_visible)

    def accept_job_base(self, job_number, job_creator_mail, function):
        """
        Puts the member on the list of possible helpers for a pending job.
        The helped one will be warned by email (this email is the parameter 'job_creator_mail').

        :param job_number: the if of the job to accept
        :param job_creator_mail: the email of the 'owner' of the job
        :param function: the function to check visibility of the job
        :return: False if there was a problem and True otherwise
        """
        
        job_list = Job.objects.filter(number=job_number, mail=job_creator_mail)
        if len(job_list) == 0:
            return False

        job = job_list[0]

        if function(job, self.db_member):
            job.member_set.add(self.db_member)

            subject = "A member want to participate to your job"
            content = "The member "+str(self.db_member.first_name)+" "+str(self.db_member.last_name)+\
                        " has been added to the list of the potential participant."
            type = 3
            return self.send_mail(self.db_member.mail, job_creator_mail, subject, content, type)
            
            #Message.send_new_helper_accept(self.db_member, db_member)

        return False
    
    def stop_participate_job(self, job_number, job_creator_mail):
        """
        Remove the member on the list of possible helpers for a pending job.

        :param job_number: the if of the job to accept
        :param job_creator_mail: the email of the 'owner' of the job
        :return: False if there was a problem and True otherwise
        """
        return self.stop_participate_job_base(job_number, job_creator_mail, self.is_job_visible)
    
    def stop_participate_job_base(self, job_number, job_creator_mail, function):
        """
        Remove the member on the list of possible helpers for a pending job.

        :param job_number: the if of the job to accept
        :param job_creator_mail: the email of the 'owner' of the job
        :param function: the function to check visibility of the job
        :return: False if there was a problem and True otherwise
        """

        job_list = Job.objects.filter(number=job_number, mail=job_creator_mail)
        if len(job_list) == 0:
            return False

        job = job_list[0]

        if function(job, self.db_member):
            job.member_set.remove(self.db_member)

            #Message.send_new_helper_accept(self.db_member, db_member)

            return True

        return False

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

        job_list = Job.objects.filter(mail=self.db_member.mail)
        if len(job_list) == 0:
            number = 0
        else:
            job_dic = job_list.aggregate(Max('number'))
            number = job_dic['number__max']

        if branch_name is None:
            return False
        else:
            branch_list = Branch.objects.filter(branch_name=branch_name)
            if len(branch_list) == 0:
                return False

        job = Job()
        job.number = number+1
        job.accepted = False
        job.address = address
        job.category = category
        job.comment = comment
        job.done = False
        job.frequency = frequency
        job.km = km
        job.mail = self.db_member.mail
        job.payed = False
        job.date = date
        job.start_time = start_time
        job.time = time
        job.type = False
        job.visibility = Job.JOB_VISIBILITY[visibility]
        job.save()
        job.branch = branch_list[0]
        job.member_set = [self.db_member]

        job.save()
        return True
    
    def delete_job(self, job_number):
        """
        Delete the number eme job of the user

        :param job_number: The number of the job of the user to delete.
        """
        job = Job.objects.filter(mail=self.db_member.mail, number=job_number)
        if len(job) != 1 :
            return False
        job = job[0]
        job.delete()
        return True
    
    def choose_participant_for_job(self, job_number, job_creator_mail, participant_mail):
        """
        Chooses the member (with email stored in 'helper_email') to do the job (with id stored in 'number')
        The chosen helper is warned by email

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :param participant_mail: The person that has been accepted for the job.
        :return: False if there was a problem and True otherwise
        """
        job = Job.objects.filter(number=job_number, mail=job_creator_mail)
        if len(job) != 1:
            return False
        job = job[0]
        job.member_set.clear()  # We clear all relationships with the members (only one member can be accepted)
        creator = Member.objects.filter(mail=job.mail)  # TODO -> show : je pref des filter, ca ne crash pas ca.
        if len(creator) != 1:
            return False
        creator = creator[0]
        job.member_set.add(creator)  # We add the creator of the job
        helper = Member.objects.filter(mail=participant_mail)
        if len(helper) != 1:
            return False
        helper = helper[0]
        job.member_set.add(helper)
        job.accepted = True
        job.save()
        
        # We send a mail
        subject = ''
        content = ''
        if job.type :   #Demand
            subject = 'Your help is accepted'
            content = 'Congratulation ! Your help has been accepted by '+str(creator.mail)+' for the job '+str(job.id)
        else :  #Offer
            subject = 'Your demand of help is accepted'
            content = 'Congratulation ! Your demand of help has been accepted by '+str(creator.mail)+' for the job '+str(job.id)
        type = 3
        return self.send_mail(creator.mail, helper.mail, subject, content, type)
    
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
        job.time = 0
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
        subject = 'The job number '+str(job.number)+' is done'
        content = 'The job number '+str(job.number)+' is done. Please, consult your account to accept or not the bill'
        type = 1
        return self.send_mail(helper_mail, helped_one_email, subject, content, type)

    def add_favorite(self, favorite_mail):
        """
        Add a favorite to self.db_member
        :param favorite_mail : the mail of the favorite
        :return : false if the member is not added to favorites (because it doesn't exist for example)
        """
        favorite = None
        for mem in self.get_visible_members(None):
            if mem.mail == favorite_mail:
                favorite=mem
        if (favorite is None) or (self.db_member==favorite) or (self.db_member.is_favorite(favorite)):
            return False
        relation = Relationship()
        relation.member_source = self.db_member
        relation.member_target = favorite
        relation.save()
        return True
        
    def remove_favorite(self, favorite_mail):
        """
        Remove a favorite to self.db_member
        :param favorite_mail : the mail of the favorite
        :return : false if the member is not removed from favorites (because it doesn't exist for example)
        """  
        favorite = Member.objects.filter(mail=favorite_mail)[0]
        if favorite is None:
            return False
        relation = Relationship.objects.filter(member_source=self.db_member, member_target=favorite)[0]
        if relation is None:
            return False
        relation.delete()
        return True

    def is_member_visible(self, member):

        #this line must be modified if we add the personal network
        return member.visibility & Member.MEMBER_VISIBILITY['anyone']\
               or (member.visibility & Member.MEMBER_VISIBILITY['favorites']
                   and member.is_favorite(self.db_member))\
               or member == self.db_member

    def get_visible_members(self, branch):
        return self.get_visible_members_base(self.is_member_visible, branch)

    def get_visible_members_base(self, function, branch):
        """
        :param branch: if it is set, it gets only the members that are in a specific branch
        :param function: the function to check visibility of the member
        :return: the list of the visible members (of the branch specified if the parameter is set)
        """

        if branch is not None:
            list_members = Member.objects.filter(branch=branch)
        else:  # We get the list of all the members
            list_members = Member.objects.all()

        # We filter the member that are hidden to the current member
        filtered_list = []
        for member in list_members:
            if function(member):
                filtered_list.append(member)

        return filtered_list
