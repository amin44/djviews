from django.http import HttpResponse

def homepage(request):
    print(dir(request))
    return HttpResponse("<!DOCTYPE html><html><head><h1 style=text-align:center>hello django learner</h1></head><body style=background-color:orange></body></html>")

# def home(request):
#     response=HttpResponse()
#     response.write("this is from respond")
#     return (response)