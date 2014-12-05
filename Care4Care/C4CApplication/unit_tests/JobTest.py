from C4CApplication.unit_tests.super_class import MySeleniumTests
from selenium.webdriver.support.ui import Select
from C4CApplication.page_objects.CreateJobPage import CreateJobPage
from C4CApplication.page_objects.ConfirmJobDonePage import ConfirmJobDonePage
from C4CApplication.page_objects.JobDetailsPage import JobDetailsPage
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.models.job import Job

import time


class JobTest(MySeleniumTests):

    # test pour creer une demande de job (I need help -> demander un service)
    def test_offer_job(self):
        #login
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        # Create the page object
        self.selenium.get('%s%s' % (self.live_server_url, '/newjob/offer'))
        time.sleep(2)
        page = CreateJobPage(self.selenium)
        
        # Test create job
        page = page.create_job("New job test", "New job description", "At my place", 0, "12:30", \
                               "00:30", "10", 1, 2, "", "", "", [], [2, 9, 7, 14], [1, 2])
        
        page = page.click_on_post_req()
        
        job = Job.objects.filter(title="New job test", description="New job description")
        self.assertEqual(len(job), 1)
        job = job[0]
        self.assertEqual(job.title, "New job test")
        self.assertEqual(job.description, "New job description")
        self.assertEqual(job.place, "At my place")
        self.assertEqual(job.branch.name, "LLN")
        self.assertEqual(job.type, False)
        return True
    
    # test pour creer une offre de job (I want to help -> offrir ses services)
    def test_demand_job(self):
        #login
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        # Create the page object
        self.selenium.get('%s%s' % (self.live_server_url, '/newjob/demand'))
        page = CreateJobPage(self.selenium)
        
        # Test create job
        page = page.create_job("New job test 2", "New job description 2", "Somewhere", 0, "00:10", \
                               "05:15", "30", 2, 0, "4", "septembre", "2015", [], [], [3])
        
        page = page.click_on_post_req()
        
        job = Job.objects.filter(title="New job test 2", description="New job description 2")
        self.assertEqual(len(job), 1)
        job = job[0]
        self.assertEqual(job.title, "New job test 2")
        self.assertEqual(job.description, "New job description 2")
        self.assertEqual(job.place, "Somewhere")
        self.assertEqual(job.branch.name, "LLN")
        self.assertEqual(job.type, True)
        return True
    
    def test_accept_offer(self):
        #login
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        # accept page
        self.selenium.get('%s%s' % (self.live_server_url, '/jobdetails/1'))
        
        page = JobDetailsPage(self.selenium)
        
        page = page.click_on_participate()
        time.sleep(1)        
        
        job = Job.objects.filter(description="Bonjour, j'ai besoin d'aide pour aller faire mes courses.", place="Rue de l'Eglise, 40, 1330, Rixensart")
        self.assertEqual(len(job), 1)
        job = job[0]
        bool = False
        for mem in job.member_set.all():
            if mem.mail == "mathieu.jadin@student.uclouvain.be":
                bool = True
        self.assertEqual(bool, True)
        return True
    
    def test_accept_help(self):
        #login
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('armand.bosquillon@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        # accept page
        job = Job.objects.get(title="Me conduire a LLN")
        self.selenium.get('%s%s' % (self.live_server_url, '/jobdetails/%d' % job.id))
        page = JobDetailsPage(self.selenium)
        time.sleep(1)
        
        page = page.click_on_choose_member(1)
        time.sleep(3)        
        
        job = Job.objects.filter(title="Me conduire a LLN", date="2014-12-19")
        self.assertEqual(len(job), 1)
        job = job[0]
        bool = False
        for mem in job.member_set.all():
            if mem.mail == "olivier.mauvaisaventure@gmail.com":
                bool = True
        self.assertEqual(bool, True)
        self.assertEqual(job.accepted, True)
        return True
    
    def test_confirm_job_is_done(self):
        #login
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('yves.delaville@gmail.com', 'azertyuiop')
        time.sleep(1)
        
        # Test confirm job
        job = Job.objects.filter(title="Visiter l'Atomium")[0]
        self.selenium.get('%s%s' % (self.live_server_url, '/confirmjobdone/%d' % (job.id)))
        
        page = ConfirmJobDonePage(self.selenium)
        page = page.enter_time_to_pay('40')
        time.sleep(1)
        page = page.click_on_confirm()
        time.sleep(1)
        self.assertEqual(0, 0)
        return True
    
    # TODO wait for this to be implemented
    def test_search_job(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True
