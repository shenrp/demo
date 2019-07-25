from django.http.response import HttpResponse

def index():

    print('123')

    return HttpResponse('哈哈哈哈')