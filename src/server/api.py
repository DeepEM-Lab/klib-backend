from django.http import HttpRequest, HttpResponse

async def root(request: HttpRequest):
    return HttpResponse("This is the root")