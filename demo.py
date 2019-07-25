from django.http.response import HttpResponse

def index(request):

    print('123')

    return HttpResponse('哈哈哈哈')

def hello(request):
    print('fsdfd')
    return HttpResponse('sdfdsfdf')