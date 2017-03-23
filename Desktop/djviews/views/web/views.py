from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , Http404 , HttpResponseRedirect
from .models import PostModel
from .forms import PostModelform
# Create your views here.
@login_required(login_url='/login')


def post_model_create_view(request):
    form=PostModelform(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        print(form.cleaned_data)
        # return HttpResponseRedirect("web/{num}".format(num=obj.id))
        # why not run correct???
    template_path = "web/create_view.html"
    context_dictioanry = {"form":form}
    return render(request, template_path, context_dictioanry)

def post_model_detail_view(request,id=None):
    # qs=PostModel.objects.get(id=120)
    # if not qs.exists():
    #     raise Http404
    # else:
    #     obj=qs.first()
    obj=PostModel.objects.get(id=id)
    template_path = "web/detail_view.html"
    context_dictioanry={"object":obj}
    return render(request,template_path,context_dictioanry)

def post_model_list_view(request):
    # qs=PostModel.objects.all()
    # # return HttpResponse("we make def and use web->urls and go to views->urls and map web urls in to /web/ and now we see all views of web")
    # template_path="web/list_view.html"
    # context_dictioanry={"query_list":qs}
    # # but dont show list.title when use query_list???
    # return render(request,template_path,context_dictioanry)

    print(request.user)
    qs=PostModel.objects.all()
    context={"object_list":qs}
    if request.user.is_authenticated():
        template="web/list_view.html"
    else:
        template="web/list_view_public.html"
    return render(request,template,context)