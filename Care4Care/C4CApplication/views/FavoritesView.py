from django.views.generic import DetailView
from C4CApplication.models.member import Member

class FavoritesView(DetailView):
    
    model = Member
    context_object_name = "member"
    template_name = "C4CApplication/Favorites.html"

    def get_object(self):
        
        #member = Member.objects.filter(mail=self.request.session['email'])
        member = Member.objects.filter(mail="armand.bosquillon@student.uclouvain.be")[0]
    
        return member