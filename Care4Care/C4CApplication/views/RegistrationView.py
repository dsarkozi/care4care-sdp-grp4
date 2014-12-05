from base64 import urlsafe_b64decode
from django.core.urlresolvers import reverse_lazy
from django.http.request import QueryDict
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from C4CApplication.views.forms.RegistrationForm import RegistrationForm
from Care4Care.settings import STATICFILES_DIRS

@never_cache
class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "C4CApplication/Registration.html"
    success_url = reverse_lazy('home')
    ax = None

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.session['ax'] = {}
        return super(RegistrationView, self).get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(RegistrationView, self).get_form_kwargs()
        self.ax = self.request.session['ax']
        if not self.ax:
            self.ax = RegistrationView.get_ax(self.request.POST)
        if self.ax:
            ax_data = {
                    'first_name' : self.ax['firstname'].split(maxsplit=1)[0] if 'firstname' in self.ax.keys() else None,
                    'last_name' : self.ax['lastname'] if 'lastname' in self.ax.keys() else None,
                    'gender' : self.ax['gender'] if 'gender' in self.ax.keys() else None,
                    'street' : self.ax['address'] if 'address' in self.ax.keys() else None,
                    'town' : self.ax['city'] if 'city' in self.ax.keys() else None,
                    'zip' : self.ax['postal_code'] if 'postal_code' in self.ax.keys() else None,
                    'birthday_day' : self.ax['birth_day'] if 'birth_day' in self.ax.keys() else None,
                    'birthday_month' : self.ax['birth_month'] if 'birth_month' in self.ax.keys() else None,
                    'birthday_year' : self.ax['birth_year'] if 'birth_year' in self.ax.keys() else None
            }
            data = QueryDict('', mutable=True)
            data.update(ax_data)
            if 'data' in kwargs.keys():
                data.update(kwargs['data'])
            kwargs['data'] = data
            kwargs.update({'eid' : True})
        else:
            kwargs.update({'eid' : False})
        self.request.session['ax'] = self.ax
        return kwargs

    def form_valid(self, form):
        self.request.session.pop('ax')
        member = form.save(commit=False)
        member.tag = form.cleaned_data['tag']
        member.gender = form.cleaned_data['gender']
        member.save()
        return super(RegistrationView, self).form_valid(form)

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
               "http://axschema.org/person/gender" : 'gender',
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
               "http://axschema.org/eid/age" : 'age',
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