from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel
# Create your views here.

def post_model_list_view(request):
    qs=PostModel.objects.all()
    print(qs)
    return HttpResponse("we make def and use web->urls and go to views->urls and map web urls in to /web/ and now we see all views of web")
