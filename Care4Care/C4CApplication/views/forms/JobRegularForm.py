#-*- coding: utf-8 -*-
from django import forms
import datetime
import time

class JobRegularForm(forms.Form):
    
    WEEKDAYS_DIC = {
        'monday'    : 0,
        'tuesday'   : 1,
        'wednesday' : 2,
        'thursday'  : 3,
        'friday'    : 4,
        'saturday'  : 5,
        'sunday'    : 6,
    }
    
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
                        list_days.append(JobRegularForm.WEEKDAYS_DIC[ee])
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
                date = JobRegularForm.next_weekday(date, day)
                list_proposition += ((date,date),)
        return list_proposition
    
    def get_propositions_monthly(job, nbr_prop):
        date = time.strftime("%Y-%m-%d")
        date = date.split('-')
        date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        list_day = purify_days(job.recursive_day)
        list_proposition = ()
        for i in rang(nbr_prop) :
            for day in list_day:
                date = next_weekday(date, day)
                list_proposition += ((date,date),)
        return list_proposition
    
    def __init__(self, job=None, nbr_prop=5, *args, **kwargs):
        super(JobRegularForm, self).__init__(*args, **kwargs)
        PROPOSITION = ()
        if job is not None :
            if job.frequency == 1:  #Weekly
                PROPOSITION = JobRegularForm.get_propositions_weekly(job, nbr_prop)
            elif job.frequency == 2:    #monthly
                PROPOSITION = get_propositions_monthly(job, nbr_prop)
            else :
                pass
        self.fields['proposition'] = forms.CharField(widget=forms.Select(choices=PROPOSITION))
        