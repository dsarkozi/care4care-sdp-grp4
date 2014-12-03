from base64 import urlsafe_b64decode
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from C4CApplication.views.forms.RegistrationForm import RegistrationForm
from Care4Care.settings import STATICFILES_DIRS


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = "C4CApplication/Registration.html"
    success_url = reverse_lazy('home')
    form = None

    def get(self, request, *args, **kwargs):
        self.form = RegistrationForm()
        return super(RegistrationView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        ax = RegistrationView.get_ax(request.POST)
        self.form = RegistrationForm(
            initial={
                'first_name' : ax['firstname'].split(maxsplit=1)[0],
                'last_name' : ax['lastname'],
                'address' : ax['address'],
                'birthday' : ax['birth_date']
            }
        )

    @staticmethod
    def get_ax(response):
        ax = 'ax' + "."
        oax = 'openid.' + ax
        res = {}
        for k, v in response.items():
            if k.startswith(oax+"type."):
                k = k.rsplit('.',1)[1]
                value_name = oax+"value."+k
                if ax+"value."+k not in response['openid.signed']:
                    continue
                res[v] = response[value_name]
        return RegistrationView._get_readable_ax(res)

    @staticmethod
    def _get_readable_ax(ax):
        res = {}
        AX = { "http://axschema.org/contact/postalAddress/home" : 'address',
               "http://axschema.org/namePerson/first" : 'firstname',
               "http://axschema.org/contact/city/home" : 'city',
               "http://axschema.org/contact/postalCode/home" : 'postal_code',
               "http://axschema.org/birthDate" : 'birth_date',
               "http://openid.net/schema/birthDate/birthYear" : 'birth_year',
               "http://openid.net/schema/birthDate/birthMonth" : 'birth_month',
               "http://openid.net/schema/birthDate/birthday" : 'birth_day',
               # "http://axschema.org/eid/pob" : 'birth_place',
               # "http://axschema.org/eid/nationality" : 'nationality',
               "http://axschema.org/namePerson/last" : 'lastname',
               "http://axschema.org/namePerson" : 'fullname',
               "http://axschema.org/eid/age" : 'age'
        }
        for key, value in ax.items():
            if key.endswith('photo'):
                filename = STATICFILES_DIRS[0] + '/images/photo.jpg'
                #value = value.replace('-', '+').replace('_', '/')
                if len(value) % 3 != 0: value += '=';
                if len(value) % 3 != 0: value += '=';
                with open(filename, 'wb') as fd:
                    fd.write(urlsafe_b64decode(value))
                    fd.close()
                value = filename
            res[AX[key]] = value
        return res