from C4CApplication.views import BranchOfficer


class BPAdministrator(BranchOfficer):
    """
    This class represents a kind of Users called BPAdministrator
    """

    def delete_member_from_branch(self, branch_name, deleted_one_email):


    def delete_member_from_site(self, deleted_one_email):


    def log_as_member(self, email):


    def give_branch_control(self, new_branch_officer_email):


    def modify_tag_member(self, email, new_tag):


    def transfer_money_from_branch(self, branch_name, destination_email):


    def create_job(self, is_demand=False, comment=None, start_time=0, frequency=0, km=0,
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

    def create_branch(self, name, town, branch_officer_email, address):
        """

        :param name:
        :param town:
        :param branch_officer_email:
        :param address:
        :return:
        """

    def remove_branch(self, branch_name):
        """

        :param branch_name:
        :return:
        """

    def transfer_bp_admin_rights(self, new_bp_admin_email):
        """

        :param new_bp_admin_email:
        :return:
        """