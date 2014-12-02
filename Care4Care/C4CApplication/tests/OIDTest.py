from base64 import b64decode, standard_b64decode, urlsafe_b64decode
from io import StringIO
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openid2rp
from Care4Care.settings import STATICFILES_DIRS


def oidtest(request):
    ax = (("http://axschema.org/eid/card-validity/end",
           "http://axschema.org/person/gender",
           "http://axschema.org/contact/postalAddress/home",
           "http://axschema.org/namePerson/first",
           "http://axschema.org/eid/photo",
           "http://axschema.org/eid/card-validity/begin",
           "http://axschema.org/contact/city/home",
           "http://axschema.org/contact/postalCode/home",
           "http://axschema.org/birthDate",
           "http://openid.net/schema/birthDate/birthYear",
           "http://openid.net/schema/birthDate/birthMonth",
           "http://openid.net/schema/birthDate/birthday",
           "http://axschema.org/eid/pob",
           "http://axschema.org/eid/card-number",
           "http://axschema.org/eid/nationality",
           "http://axschema.org/namePerson/last",
           "http://axschema.org/namePerson",
           "http://axschema.org/eid/rrn",
           # "http://axschema.org/eid/cert/auth",
           "http://axschema.org/eid/age"), ())
    uri = "https://www.e-contract.be/eid-idp/endpoints/openid/ident"
    kind, claimedId = openid2rp.normalize_uri(uri)
    res = openid2rp.discover(claimedId)
    if res is not None:
        services, op_endpoint, op_local = res
        session = openid2rp.associate(services, op_endpoint)
        redirect_url = openid2rp.request_authentication(
            services,
            op_endpoint,
            session['assoc_handle'],
            "http://127.0.0.1:8000/tests/openid2",
            claimedId, op_local,
            sreg=((), ()),
            ax=ax
        )

        response = HttpResponse()
        response['Location'] = redirect_url
        response.status_code=303
        return response

        # return render_to_response('OIDTest.html',
        #                           {
        #                               'services' : services,
        #                               'op_endpoint' : op_endpoint,
        #                               'op_local' : op_local,
        #                               'kind' : kind,
        #                               'claimedID' : claimedId,
        #                               'redirect_url' : redirect_url
        #                               }
        # )

@csrf_exempt
def oidtest2(request):
    # signed, claimedID = openid2rp.verify(request.POST, None, None, True)
    # printy(get_ax(request.POST))
    ax = get_ax(request.POST)
    args = ax.copy()
    args.update({'ax' : ax})
    strIO = StringIO()
    print(ax, file=strIO)
    args.update({'printy' : strIO.getvalue()})
    return render(request, "OIDTest.html", args)

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
    return _get_readable_ax(res)

def _get_readable_ax(ax):
    res = {}
    AX = {"http://axschema.org/eid/card-validity/end" : 'card_validity_end',
           "http://axschema.org/person/gender" : 'gender',
           "http://axschema.org/contact/postalAddress/home" : 'address',
           "http://axschema.org/namePerson/first" : 'firstname',
           "http://axschema.org/eid/photo" : 'photo',
           "http://axschema.org/eid/card-validity/begin" : 'card_validity_start',
           "http://axschema.org/contact/city/home" : 'city',
           "http://axschema.org/contact/postalCode/home" : 'postal_code',
           "http://axschema.org/birthDate" : 'birth_date',
           "http://openid.net/schema/birthDate/birthYear" : 'birth_year',
           "http://openid.net/schema/birthDate/birthMonth" : 'birth_month',
           "http://openid.net/schema/birthDate/birthday" : 'birth_day',
           "http://axschema.org/eid/pob" : 'birth_place',
           "http://axschema.org/eid/card-number" : 'card_number',
           "http://axschema.org/eid/nationality" : 'nationality',
           "http://axschema.org/namePerson/last" : 'lastname',
           "http://axschema.org/namePerson" : 'fullname',
           "http://axschema.org/eid/rrn" : 'register_number',
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