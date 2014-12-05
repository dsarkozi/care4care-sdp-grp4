from urllib.parse import unquote
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.base import RedirectView
import openid2rp


class EIDRedirectView(RedirectView):
    url = None

    def get(self, request, *args, **kwargs):
        ax = (("http://axschema.org/contact/postalAddress/home",
           "http://axschema.org/namePerson/first",
           "http://axschema.org/person/gender",
           "http://axschema.org/contact/city/home",
           "http://axschema.org/contact/postalCode/home",
           "http://axschema.org/birthDate",
           "http://openid.net/schema/birthDate/birthYear",
           "http://openid.net/schema/birthDate/birthMonth",
           "http://openid.net/schema/birthDate/birthday",
           # "http://axschema.org/eid/pob",
           # "http://axschema.org/eid/nationality",
           "http://axschema.org/namePerson/last",
           "http://axschema.org/namePerson",
           # "http://axschema.org/eid/cert/auth",
           "http://axschema.org/eid/age"), ())
        uri = "https://www.e-contract.be/eid-idp/endpoints/openid/ident"
        kind, claimedId = openid2rp.normalize_uri(uri)
        res = openid2rp.discover(claimedId)
        if res is not None:
            services, op_endpoint, op_local = res
            session = openid2rp.associate(services, op_endpoint)
            self.url = openid2rp.request_authentication(
                services,
                op_endpoint,
                session['assoc_handle'],
                self.request.build_absolute_uri(reverse('registration')),
                claimedId, op_local,
                sreg=((), ()),
                ax=ax
            )
            self.url = unquote(self.url)
        return super(EIDRedirectView, self).get(request, *args, **kwargs)