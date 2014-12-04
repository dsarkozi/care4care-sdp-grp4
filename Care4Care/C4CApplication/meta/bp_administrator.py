from C4CApplication.meta.time import Time

from C4CApplication.meta.branch_officer import BranchOfficer
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
        member = member[0]
        branch = Branch.objects.filter(name=branch_name)
        if len(branch) != 1:
            return False
        branch = branch[0]
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
        deleted_member = Member.objects.filter(mail=deleted_one_email)
        # If the member doesn't exist or if it's the bp admin
        if len(deleted_member) != 1 or deleted_one_email == self.db_member.mail:
            return False
        deleted_member = deleted_member[0]

        # Delete all jobs that the member to delete is involved in
        jobs_of_member = self.db_member.job.all()
        for job in jobs_of_member:
            # He is the creator of the job => we delete the job
            if not job.accepted and job.mail == self.db_member.mail:
                job.delete()
            elif not job.accepted and job.mail != self.db_member.mail:
                job.member_set.all().remove(self.db_member)  # We remove him from the list of participants
            elif not job.payed:  # If the job is accepted but pending, we remove it
                job.delete()

        deleted_member.deleted = True
        deleted_member.save()
        return True

    def log_as_member(self, email, session):

        if email == self.db_member.mail:  # If the user is already logged as himself...
            return False

        # Change the session variable
        session['super_user_mail'] = session['email']
        session['email'] = email

        return True

    def give_branch_control(self, branch_name, new_branch_officer_email):
        """
        Set the control of a branch to an another branch_officer, which is represented by his mail
        :param branch_name: the name of the branch that will change of the branch_officer
        :param new_branch_officer_email: the new branch_officer that will control the branch
        :return: False if there was a problem and True otherwise.
        """
        branch = Branch.objects.filter(name=branch_name)
        if len(branch) != 1:
            return False

        new_branch_officer = Member.objects.filter(mail=new_branch_officer_email)
        # If the member doesn't exist
        if len(new_branch_officer) != 1 or new_branch_officer[0].deleted:
            return False
        new_branch_officer = new_branch_officer[0]

        # Change rights
        branch = branch[0]
        old_branch_officer = Member.objects.filter(mail=branch.branch_officer)
        if len(old_branch_officer) != 1:  # If the branch officer doesn't exists
            return False
        old_branch_officer = old_branch_officer[0]
        keep_tag = False
        for branch in Branch.objects.all():
            # If the branch officer handles other branches
            if branch.name != branch_name and branch.branch_officer == old_branch_officer.mail:
                keep_tag = True
                break

        if not keep_tag:  # The branch officer looses its tags
            old_branch_officer.tag ^= 16  # We revoke its branch officer rights
            old_branch_officer.tag |= 12  # We degrade him to a volunteer and verified member

        new_branch_officer.tag |= 16  # We promote him branch officer

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
        member = member[0]
        
        
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
        member = Member.objects.filter(mail=destination_email)
        if len(member) != 1:
            return False
        member = member[0]
        branch.donation -= time
        member.time_credit += time
        branch.save()
        member.save()
        return True

    def create_job(self, branch_name, title, date=Time.str_to_ftime('%Y-%m-%d'), is_demand=False,\
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
        branch = Branch.objects.filter(name=branch_name)
        if len(branch) != 1:
            return False
        job.branch = branch[0]
        job.member_set.add(self.db_member)
        job.save()
        return job

    def create_branch(self, name, branch_town, branch_officer_email=None, street='', zip='', town=''):
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
        branch.town = branch_town
        branch.street = street
        branch.zip = zip
        branch.town = town

        branch_officer = Member.objects.filter(mail=branch_officer_email)
        if len(branch_officer) != 1 or branch_officer[0].deleted:  # If the member does not exist
            return False
        branch_officer = branch_officer[0]
        branch_officer.tag = 16  # We upgrade his rights

        branch.branch_officer = branch_officer_email
        branch.save()
        branch_officer.save()
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
        branch = branch[0]
        
        branch_officer = Member.objects.filter(mail=branch.branch_officer)
        if len(branch_officer) != 1:
            return False
        branch_officer = branch_officer[0]
        
        #Change rights
        keep_tag = False
        for branch in Branch.objects.all():
            # If the branch officer handles other branches
            if branch.name != branch_name and branch.branch_officer == branch_officer.mail:
                keep_tag = True
                break

        if not keep_tag:  # The branch officer looses its tags
            branch_officer.tag ^= 16  # We revoke its branch officer rights
            branch_officer.tag |= 12  # We degrade him to a volunteer and verified member
        
        branch.member_set.clear()
        branch.delete()
        branch_officer.save()
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
        member = member[0]
        member.tag = Member.TAG['bp_admin']
        self.db_member.tag = Member.TAG['volunteer and verified']
        member.save()
        self.db_member.save()
        return True
