#-*- coding: utf-8 -*-
from django import forms
import datetime
import time, calendar
from calendar import monthrange


class JobRegularForm(forms.Form):
    
    def job_already_created(job, date):
        for j in job.job_set.all():
            if j.date == date:
                return True
        return False
    
    def next_weekday(date, weekday):
        '''
        Return the next weekday after the date.
        :param date: date like this : datetime.date(yyyy, mm, dd). Ex : (2014, 12, 3)
        :param weekday: The day of the week. 0 = monday, 1 = tuesday, ...
        '''
        days_ahead = weekday - date.weekday()
        if days_ahead <= 0: # Target day already happened this week
            days_ahead += 7
        return date + datetime.timedelta(days_ahead)
    
    def get_day_of_month_from_int(date, day):
        day_ahead = day - date.day
        if day_ahead <= 0:  # Target day already happened this month
            day_ahead += monthrange(date.year, date.month)[1]
            
        if monthrange(date.year, date.month)[1] >= day :
            date = datetime.date(date.year, date.month, day)
        else :
            date = datetime.date(date.year, date.month, monthrange(date.year, date.month)[1])
        
        return date
    
    def next_monthday(date):
        '''
        Return the next weekday after the date.
        :param date: date like this : datetime.date(yyyy, mm, dd). Ex : (2014, 12, 3)
        :param weekday: The day of the week. 0 = monday, 1 = tuesday, ...
        '''
        month = date.month - 1 + 1
        year = date.year + month // 12
        month = month % 12 + 1
        day = min(date.day,calendar.monthrange(year,month)[1])
        return datetime.date(year,month,day)
    
    def purify_days(recursive_day):
        '''
        :param recursive_day: string recursive_day from job
        :return: the list of the number corresponding to the days in the string recursive_day, and sorted
        '''
        recursive_day = recursive_day.split(',')
        list_days = []
        for e in recursive_day:
            if e != '':
                temp = e.split(' ')
                for ee in temp:
                    if ee != '':
                        list_days.append(int(ee))
        list_days.sort()
        return list_days
    
    def get_propositions_weekly(job, nbr_prop):
        date = time.strftime("%Y-%m-%d")
        date = date.split('-')
        date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        list_day = JobRegularForm.purify_days(job.recursive_day)
        list_proposition = ()
        for i in range(nbr_prop) :
            for day in list_day:
                temp_date = JobRegularForm.next_weekday(date, day)
                if not JobRegularForm.job_already_created(job, temp_date) and (temp_date,temp_date) not in list_proposition:
                    list_proposition += ((temp_date,temp_date),)
            date = JobRegularForm.next_weekday(date, date.weekday())
        return list_proposition
    
    def get_propositions_monthly(job, nbr_prop):
        date = time.strftime("%Y-%m-%d")
        date = date.split('-')
        date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        list_day = JobRegularForm.purify_days(job.recursive_day)
        list_proposition = ()
        for i in range(nbr_prop) :
            for day in list_day:
                temp_date = JobRegularForm.get_day_of_month_from_int(date, day)
                if not JobRegularForm.job_already_created(job, temp_date) and (temp_date,temp_date) not in list_proposition:
                    list_proposition += ((temp_date,temp_date),)
            date = JobRegularForm.next_monthday(date)
        return list_proposition
    
    def __init__(self, job=None, nbr_prop=5, *args, **kwargs):
        super(JobRegularForm, self).__init__(*args, **kwargs)
        PROPOSITION = ()
        if job is not None :
            if job.frequency == 1:  #Weekly
                PROPOSITION = JobRegularForm.get_propositions_weekly(job, nbr_prop)
            elif job.frequency == 2:    #monthly
                PROPOSITION = JobRegularForm.get_propositions_monthly(job, nbr_prop)
            else :
                pass
        self.fields['proposition'] = forms.CharField(widget=forms.Select(choices=PROPOSITION))
        