from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import MySQLdb
import time
from .models import Users


def index(request):
    # return HttpResponse("Hello 世界")
    loginBean = None
    try:
        loginBean = request.session['loginbean']
    except Exception as err:
        pass
    return render(request, 'novel.html',{'loginbean':loginBean});

def zhucePanel(request):
    return render(request, 'users/register.html');

def loginPanel(request):
    return render(request, 'users/login.html');

def zhuce(request):
    if request.method == 'POST':
        dict = request.POST.dict()  #转成字典形式
        # email = request.POST.get('email')
        # pwd = request.POST.get('pwd')
        # nicheng = request.POST.get('nicheng')
        try:
            del dict['csrfmiddlewaretoken']
            #dict['createtime']=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            user = Users.objects.create(createtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),**dict) #**dict必须放到最后
            dict['id']=user.id
            #Users.objects.create(email=email, pwd=pwd, nicheng=nicheng) #创建一个对象实例
            request.session['dict']=dict
            return redirect('/userLogin')
        except Exception as err:
            errStr = err.args[1]
            if 'emailuniq' in errStr:
                return HttpResponse('<script>alert("用户名重复");location.href="/";</script>')
            elif 'nichenguniq' in errStr:
                return HttpResponse('<script>alert("昵称重复");location.href="/";</script>')

    else:
        return HttpResponse('请正确提交')

def login(request):
    if request.method == 'POST':
        rs = Users.objects.filter(email=request.POST.get('email'),pwd=request.POST.get('pwd')).first()
        # print(rs)
        if rs != None:
            loginbean = {}
            loginbean['id']=rs.id
            loginbean['nicheng'] = rs.nicheng
            loginbean['role'] = rs.role
            request.session['loginbean']=loginbean
            # return HttpResponse('登录成功')
            if rs.role>0:
                return redirect('/home')
            else:
                return redirect('/adminhome')
        else:
            return HttpResponse('用户名/密码错误')
    else:
        dict = request.session['dict']
        if dict!=None:
            loginbean = {}
            loginbean['id'] = dict['id']
            loginbean['nicheng'] = dict['nicheng']
            loginbean['role'] = 1
            request.session['loginbean'] = loginbean
            del request.session['dict']
            # return HttpResponse('登录成功')
            return redirect('/home')
        else:
            return HttpResponse('请登录')
        # return HttpResponse(rs)

def logout(request):
    del request.session['loginbean']
    return redirect('/')