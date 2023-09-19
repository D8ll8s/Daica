from django.views import generic


class HomeView(generic.ListView):
    template_name = 'basic/home.html'
    def get_queryset(self):
        return 0