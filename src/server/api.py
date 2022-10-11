from django.http import HttpRequest, HttpResponse

def root(request: HttpRequest):
    return HttpResponse("This is the root")