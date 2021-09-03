from django.shortcuts import render
import requests
import json

# Create your views here.
def get_geopraphicinfo(request):
    ip=request.META.get('HTTP_X_FORWARDED_FOR',"") or (request.META.get('REMOTE_ADDR'))
    url='http://api.ipstack.com/60.243.227.53?access_key=24c240d2bec53d3b24cc028f53d2b9d9'
    response=requests.get(url)
    data=response.json()
    return render(request,'testapp/home.html',data)
