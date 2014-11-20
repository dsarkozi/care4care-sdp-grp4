from C4CApplication.views import User, Message
from C4CApplication.models import Job, Member, Branch
from django.db.models import Max


class NonMember(User):
    """
    This class represents a kind of Users called Non Members
    """

    def __init__(self, db_member):
        self.db_member = db_member

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
        return self.get_job_list_base(show_offers, self.is_job_visible)

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

        job_list = Job.objects.filter(number=job_number, mail=job_creator_mail, type=True)
        if len(job_list) == 0:
            return False

        job = job_list[0]

        db_member = (Member.objects.filter(mail=job_list.mail))[0]

        if function(job, db_member):
            job.member_set.add(self.db_member)

            Message.send_new_helper_accept(self.db_member, db_member)

            return True

        return False

    def create_job(self, start_time, time, branch_name, comment=None, frequency=0, km=0,
                   category=1, address=None, visibility='anyone'):
        """
        Creates a help offer (the parameters will be used to fill the database).

        :param start_time:
        :param time:
        :param branch_name:
        :param comment:
        :param frequency:
        :param km:
        :param category:
        :param address:
        :param visibility:
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
        job.start_time = start_time
        job.time = time
        job.type = False
        job.visibility = Job.JOB_VISIBILITY[visibility]
        job.save()
        job.branch = branch_list[0]
        job.member_set = [self.db_member]

        job.save()
        return True


    def register_job_done(self, job_number, job_creator_mail):
        """
        Registers a job as done (with no time because a Non Member cannot 'earn' time)

        :param job_number:
        :param job_creator_mail: the email of the 'owner' of the job
        :return: False if there was a problem and True otherwise.
        """

        job_list = Job.objects.filter(number=job_number, mail=job_creator_mail)
        if len(job_list) == 0:
            return False

        job = job_list[0]
        if self.db_member not in job.member_set:
            return False

        job.done = True
        return True
