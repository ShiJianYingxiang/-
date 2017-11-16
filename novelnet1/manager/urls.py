from django.conf.urls import url
from django.conf.urls import include
from . import views
from .home import myhome
from .home import adminHome
from . import common

urlpatterns = [
    url(r'^$', views.index, name='index'),  # 首页
    url(r'^userRegister', views.zhuce, name='zhuce'),
    url(r'^userLogin', views.login, name='login'),
    url(r'^loginpanel', views.loginPanel),
    url(r'^zhucepanel', views.zhucePanel),
    url(r'^home$', myhome.index),
    url(r'^writerApply$', myhome.writerApply),
    url(r'^showImg$',common.showImg),
    url(r'^logout$',views.logout),
    url(r'^adminhome$',adminHome.index),
    url(r'^writerapplylist$',adminHome.writerApplyList),
    url(r'^applyInfo',adminHome.applyInfo),
    url(r'^applyPass',adminHome.applyPass)
]
