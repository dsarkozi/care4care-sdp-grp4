from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.simulation.SimulationTime import SimulationTime

from C4CApplication.simulation.BranchOfficerActor import BranchOfficerActor


class Scheduler(MySeleniumTests):

    actor_list = None

    def get_actors_list(self):

        if self.actor_list is None:
            self.actor_list = [
                BranchOfficerActor()
            ]

        return self.actor_list

    def test_simulation(self):

        # We populate the database
        self.populate_db()

        # TODO program the change of time

        i = -1

        while len(self.get_actors_list()) != 0:  # We continue the test as long as there are actors that have to act

            i = (i+1) % len(self.get_actors_list())

            actor = (self.get_actors_list())[i]

            result = actor.act(self.selenium, self.live_server_url)

            if result is None:
                print('An actor has finished')
                self.get_actors_list().remove(actor)

            elif not result:
                print('An actor has failed')
                return False
            else:  # The actor has succeeded
                pass

        return True