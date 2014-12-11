from time import strftime, gmtime, time

from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.conf import settings


class Time:
    """
    This class is used to retrieve the time of the server
    In case of simulation, We can use it to simulate the date that we want
    """

    current_date = None
    debug = None

    @staticmethod
    def str_to_ftime(date_format='%Y-%m-%d'):

        # If we didn't test yet if we are in a simulation or if we know that there is one
        additional_seconds = 0
        if Time.debug is None or Time.debug:
            session_list = Session.objects.filter(pk=settings.SESSION_ID_SIMU)
            if len(session_list) == 1:  # If the session variable exits
                session_dictionary = SessionStore(session_key=settings.SESSION_ID_SIMU)

                Time.current_date = session_dictionary['current_date']

                additional_seconds = Time.current_date

        return strftime(date_format, gmtime(time() + additional_seconds))