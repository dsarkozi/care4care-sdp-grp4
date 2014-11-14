from C4CApplication.views import Member


class BranchOfficer(Member):
    """
    This class represents a kind of Users called Branch Officers
    """

    def delete_member_from_branch(self, branch_name, deleted_one_email):


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