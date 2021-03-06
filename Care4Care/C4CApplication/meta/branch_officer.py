from C4CApplication import models
from C4CApplication.models.branch import Branch

from C4CApplication.meta.member import Member as MetaMember


class BranchOfficer(MetaMember):
    """
    This class represents a kind of Users called Branch Officers
    """
    
    def delete(self):
        return False

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

        # If the member is another branch officer or a bp administrator, it cannot log as them
        if member.tag >= 16:
            return False

        member_branch = None
        for branch in member.branch.all():
            if branch.branch_officer == self.db_member.mail:  # The branch officer handles this branch
                member_branch = branch

        if member_branch is None:  # The branch officer have no power on this user
            return False

        # Change the session variable
        session['super_user_mail'] = session['email']
        session['email'] = email

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
        if branch.branch_officer != self.db_member.mail:  # If he is branch officer of this branch
            return False

        new_branch_officer = models.Member.objects.filter(mail=new_branch_officer_email)
        # If the member doesn't exist
        if len(new_branch_officer) != 1 or new_branch_officer[0].deleted:
            return False
        new_branch_officer = new_branch_officer[0]

        # Change rights
        branch = branchlist[0]
        old_branch_officer = models.Member.objects.filter(mail=branch.branch_officer)
        if len(old_branch_officer) != 1:  # If the branch officer doesn't exists
            return False
        old_branch_officer = old_branch_officer[0]
        keep_tag = False
        for br in Branch.objects.all():
            # If the branch officer handles other branches
            if br.name != branch_name and br.branch_officer == old_branch_officer.mail:
                keep_tag = True
                break

        if not keep_tag:  # The branch officer looses its tags
            old_branch_officer.tag ^= 16  # We revoke its branch officer rights
            old_branch_officer.tag |= 12  # We degrade him to a volunteer and verified member

        new_branch_officer.tag |= 16  # We promote him branch officer

        branch.branch_officer = new_branch_officer_email
        new_branch_officer.branch.add(branch)
        branch.save()
        new_branch_officer.save()
        old_branch_officer.save()
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

    def is_member_visible(self, member):
        if member.deleted : return False
        return True

    def get_visible_members(self, branch):
        return self.get_visible_members_base(self.is_member_visible, branch)
