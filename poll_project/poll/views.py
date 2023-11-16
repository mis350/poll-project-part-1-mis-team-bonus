from django.shortcuts import render

from .models import Poll

# Create your views here.

def list_poll_view(request):

     p = list_poll_view.objects.all()

     context = {}
     context = ['poll']
     
     return render(request, "list_poll.html" ,context)


# Create your views here.

