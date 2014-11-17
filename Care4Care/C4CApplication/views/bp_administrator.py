from C4CApplication.views import BranchOfficer
from C4CApplication.models import Member, Branch, Job


class BPAdministrator(BranchOfficer):
    """
    This class represents a kind of Users called BPAdministrator
    """

    def delete_member_from_branch(self, branch_name, deleted_one_email):
        """
        Delete the member from the branch
        
        :param branch_name: The name of the branch that the branch_officer belongs to
        :param deleted_one_email: The mail of the member the branch_officer want to remove from
                                    the branch.
        :return: False if there was a problem and True otherwise.
        """
        member = Member.objects.filter(mail=deleted_one_email)
        if len(member) != 1:
            return False
        branch = Branch.objects.filter(name=branch_name)
        if len(branch) != 1:
            return False
        member.branch.remove(branch)
        member.save()
        branch.save()
        return True

    def delete_member_from_site(self, deleted_one_email):
        """
        Put the status of the member as deleted (TODO add a deleted field to member ?)
        :param deleted_one_email: the email of the person to delete
        :return: False if there was a problem and True otherwise.
        """
        # TODO

    def log_as_member(self, email):
        """
        :param email: the email of the member to log in as
        :return: the object Member or None if there is a problem
        """
        # TODO -> go throught sessions variables ?

    def give_branch_control(self, branch_name, new_branch_officer_email):
        """
        Set the control of a branch to an another branch_officer, which is represented by his mail
        :param branch_name: the name of the branch that will change of the branch_officer
        :param new_branch_officer_email: the new branch_officer that will control the branch
        :return: False if there was a problem and True otherwise.
        """
        branch = Branch.objects.filter(name=branch_name)
        branch.branch_officer = new_branch_officer_email
        branch.save()
        return True

    def modify_tag_member(self, email, new_tag):
        """
        Modify the tag of the member represented by the email,
        and set his tag to the new_tag
        :param email: mail of the member we need to modify the tag
        :param new_tag: new tag to assign to the member
        :return: False if there was a problem and True otherwise.
        """
        member = Member.objects.filter(mail=email)
        if len(member) != 1:
            return False
        member.tag = Member.TAG[new_tag]
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
        member = Member.objects.filter(mail=destination_email)
        if len(member) != 1:
            return False
        branch.donation -= time
        member.time_credit += time
        branch.save()
        member.save()
        return True

    def create_job(self, branch_name, is_demand=False, comment=None, start_time=0, frequency=0, km=0,
                   time=0, category=1, address=None, visibility='volunteer'):
        """
        Creates a help offer (the parameters will be used to fill the database).

        :param is_demand:
        :param comment:
        :param start_time:
        :param frequency:
        :param km:
        :param time:
        :param category:
        :param address:
        :param visibility:
        :return: False if there was a problem and True otherwise.
        """
        # TODO Why my aggregate solution does not work :p ?
        job = Job()
        job.mail = self.db_member.mail
        n = 0
        jobs_created_by_me = Job.objects.filter(mail=self.db_member.mail)
        for j in jobs_created_by_me:
            if j.number > n:
                n = m
        job.number = n+1
        job.comment = comment
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
        job.branch = branch
        job.save()
        return True

    def create_branch(self, name, town, branch_officer_email=None, address=None):
        """
        Create a new branch with the parameter
        :param name: name of the new branch
        :param town: town of the new branch
        :param branch_officer_email: mail of the branch_officer that will manage the branch
        :param address: address of the branch, for meeting, or other
        :return: False if there was a problem and True otherwise.
        """
        branch = Branch()
        branch.name = name
        branch.town = town
        branch.address = address
        branch.branch_officer = branch_officer_email
        branch.save()
        return True

    def remove_branch(self, branch_name):
        """
        Remove a branch from the application
        :param branch_name: the name of the branch to remove
        :return: False if there was a problem and True otherwise.
        """
        branch = Branch.objects.filter(name=branch_name)
        if len(branch) != 1:
            return False
        branch.member_set.clear()
        branch.delete()
        return True

    def transfer_bp_admin_rights(self, new_bp_admin_email):
        """
        The bp admin abandon his rights, and give them to someone else.
        :param new_bp_admin_email:
        :return: False if there was a problem and True otherwise.
        """
        member = Member.objects.filter(mail=new_bp_admin_email)
        if len(member) != 1:
            return False
        member.tag = Member.TAG['bp_admin']
        self.db_member.tag = Member.TAG['verified']
        member.save()
        self.db_member.save()
        return True