from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import MySQLdb
import time
import datetime
import os
from manager.models import Writers
from manager.models import Users

def index(request):
    try:
        loginbean = request.session['loginbean']
        if loginbean==None:
            return HttpResponse("<script>alert('登录过期,请重新登录');location.href='/';</script>")
        if loginbean['role']==0:
            return render(request, 'admin/adminhome.html',{'loginbean':loginbean})
        else:
            return HttpResponse("<script>alert('您无权限进入');location.href='/;</script>")
    except Exception as err:
        print(err)
        return HttpResponse("<script>alert('请登录');location.href='/';</script>")

def writerApplyList(request):
    try:
        loginbean = request.session['loginbean']
        if loginbean == None:
            return HttpResponse("<script>alert('登录过期,请重新登录');location.href='/';</script>")
        if loginbean['role'] == 0:
            sql = 'select u.id,w.realname,w.biming,w.updtime from users u,writers w where u.role=2 and u.id=w.id';
            rs = Users.objects.raw(sql)
            #print(rs[0].realname)
            # print('------------------')
            # for row in rs:
            #         print(row.realname)

            return render(request, 'admin/writerApplyList.html', {'loginbean': loginbean,'rs':rs})
        else:
            return HttpResponse("<script>alert('您无权限进入');location.href='/;</script>")
    except Exception as err:
        print(err)
        return HttpResponse("<script>alert('请登录');location.href='/';</script>")

def applyInfo(request):
    try:
        loginbean = request.session['loginbean']
        if loginbean == None:
            return HttpResponse("<script>alert('登录过期,请重新登录');location.href='/';</script>")
        if loginbean['role'] == 0:
            id = request.GET.get('id')
            rs = Writers.objects.filter(id=id).first()
            return render(request, 'admin/applyInfo.html', {'loginbean': loginbean,'rs':rs,'id':id})
        else:
            return HttpResponse("<script>alert('您无权限进入');location.href='/;</script>")
    except Exception as err:
        print(err)
        return HttpResponse("<script>alert('请登录');location.href='/';</script>")


def applyPass(request):
    try:
        loginbean = request.session['loginbean']
        if loginbean == None:
            return HttpResponse("<script>alert('登录过期,请重新登录');location.href='/';</script>")
        if loginbean['role'] == 0:
            id = request.GET.get('id')
            Users.objects.filter(id=id).update(role=3)
            return redirect('/writerapplylist')

            # rs = Writers.objects.filter(id=id).first()
            # return render(request, 'admin/applyInfo.html', {'loginbean': loginbean,'rs':rs,'id':id})
        else:
            return HttpResponse("<script>alert('您无权限进入');location.href='/;</script>")
    except Exception as err:
        print(err)
        return HttpResponse("<script>alert('请登录');location.href='/';</script>")