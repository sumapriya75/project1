from django.http import HttpResponse
def index(request):
    return HttpResponse("hello world")
def page2(request):
    return HttpResponse("<h1>hello</h1>")
def page3(request):
    content="""<h1>hii</h1>
               <h2>good morning...</h2>"""
    return HttpResponse(content)
    