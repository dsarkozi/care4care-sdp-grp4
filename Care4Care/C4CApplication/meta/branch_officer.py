from time import strftime, gmtime
from C4CApplication.meta import Member
from C4CApplication.models import Branch, Job

from C4CApplication import models


class BranchOfficer(Member):
    """
    This class represents a kind of Users called Branch Officers
    """

    def is_job_visible(self, job, db_member):
        # The branch officer can see all the jobs
        return True

    def see_job_details(self, job_number, job_creator_mail):
        return self.see_job_details_base(job_number, job_creator_mail, self.is_job_visible)

    def get_job_list(self, show_offers):
        return self.get_visible_job_list_base(show_offers, self.is_job_visible)

    def accept_job(self, job_number, job_creator_mail):
        return self.accept_job_base(job_number, job_creator_mail, self.is_job_visible)

    def is_branch_officer(self, member):
        """
        :param member:
        :return: True if the current user is the branch officer of the member
        """
        member_branch = None
        for branch in member.branch.all():
            if branch.branch_officer == self.db_member.mail:  # The branch officer handles this branch
                member_branch = branch

        return member_branch is not None

    def delete_member_from_branch(self, branch_name, deleted_one_email):
        """
        Delete the member from the branch
        
        :param branch_name: The name of the branch that the branch_officer belong
        :param deleted_one_email: the mail of the member the branch_officer want to remove from
                                    the branch.
        :return: False if there was a problem and True otherwise.
        """
        branch = Branch.objects.filter(name=branch_name)
        if len(branch) != 1:
            return False
        branch = branch[0]
        if branch.branch_officer != self.db_member.mail:
            return False
        member = models.Member.objects.filter(mail=deleted_one_email)
        if len(member) != 1:
            return False
        member = member[0]
        member.branch.remove(branch)
        member.save()
        branch.save()
        return True

    def log_as_member(self, email, session):

        if email == self.db_member.mail:  # If the user is already logged as himself...
            return False

        member = models.Member.objects.filter(mail=email)
        if len(member) != 1:
            return False
        member = member[0]

        member_branch = None
        for branch in member.branch:
            if branch.branch_officer == self.db_member.mail:  # The branch officer handles this branch
                member_branch = branch

        if member_branch is None:  # The branch officer have no power on this user
            return False

        # Change the session variable
        session['super_user_mail'] = session['mail']
        session['mail'] = email

        return True

    def give_branch_control(self, branch_name, new_branch_officer_email):
        """
        Set the control of a branch to an another branch_officer, which is represent by the mail
        :param new_branch_officer_email: the new branch_officer that will control the branch
        :return: False if there was a problem and True otherwise.
        """
        branchlist = Branch.objects.filter(name=branch_name)
        if len(branchlist) != 1:
            return False
        branch = branchlist[0]
        if branch.branch_officer != self.db_member.mail:
            return False
        branch.branch_officer = new_branch_officer_email
        branch.save()
        return True

    def modify_tag_member(self, member_mail, new_tag):
        """
        Modify the tag of the member represented by the member_mail,
        and set his tag to the new_tag
        :param member_mail: mail of the member we need to modify the tag
        :param new_tag: new tag to assign to the member
        :return: False if there was a problem and True otherwise.
        """

        member = models.Member.objects.filter(mail=member_mail)
        if len(member) != 1:
            return False
        member = member[0]

        member_branch = None
        for branch in member.branch.all() :
            if branch.branch_officer == self.db_member.mail:  # The branch officer handles this branch
                member_branch = branch

        if member_branch is None:  # The branch officer have no power on this user
            return False
        
        if member.tag & 4 : # if 4
            if member.tag & 8 : # if 4 and 8
                if new_tag == 4 or new_tag == 8 :
                    member.tag = member.tag ^ new_tag
                else :
                    member.tag = new_tag
            else : # not 8 but 4
                if new_tag == 4 :
                    member.tag = 2
                elif new_tag == 8:
                    member.tag = 12
                else :
                    member.tag = new_tag
        else : # not 4
            if member.tag & 8 : # not 4 but 8
                if new_tag == 4 :
                    member.tag = 12
                elif new_tag == 8 :
                    member.tag = 2
                else :
                    member.tag = new_tag
            else : # not 4 and not 8
                member.tag = new_tag

        member.save()
        return True

    def transfer_money_from_branch(self, time, branch_name, destination_email):
        """
        Make a gift by taking some time from the branch to the member represented
        by the destinaion_mail.
        :param time: the amount of time that we give as a gift
        :param branch_name: the branch that give the donation
        :param destination_email: the member that receive the donation
        :return: False if there was a problem and True otherwise.
        """
        branch = Branch.objects.filter(name=branch_name)
        if len(branch) != 1:
            return False
        branch = branch[0]
        if branch.branch_officer != self.db_member.mail:
            return False
        member = models.Member.objects.filter(mail=destination_email)
        if len(member) != 1:
            return False
        member = member[0]
        branch.donation -= time
        member.time_credit += time
        branch.save()
        member.save()
        return True
    
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

    def is_member_visible(self, member):
        if member.deleted : return False
        return True

    def get_visible_members(self, branch):
        return self.get_visible_members_base(self.is_member_visible, branch)
