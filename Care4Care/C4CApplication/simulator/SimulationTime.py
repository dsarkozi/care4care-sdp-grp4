from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.conf import settings


def change_server_time(time):

    #Create a new session
    s = SessionStore(session_key='')
    s.save()
    old_s = Session.objects.get(session_key=s.session_key)

    #Copy it to a column with an id fixed
    new_session = Session(session_key=settings.SESSION_ID_SIMU, session_data=old_s.session_data,
                          expire_date=old_s.expire_date)
    new_session.save()

    #Change the current date
    session_dictionary = SessionStore(session_key=settings.SESSION_ID_SIMU)
    session_dictionary['current_date'] = time
    session_dictionary.save()