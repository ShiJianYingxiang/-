from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import MySQLdb
import time
from os import path

def showImg(request):
    imgurl = request.GET.get('imgurl')
    #print(imgurl)
    d = path.dirname(__file__)
    #print(d)
    imgPath = path.join(d,"static/imgs/"+imgurl)
    image_data = open(imgPath, "rb").read()
    return HttpResponse(image_data, content_type="image/png")