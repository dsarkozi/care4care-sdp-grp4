from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import openid2rp


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
           "http://axschema.org/eid/cert/auth",
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