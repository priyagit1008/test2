"""drf_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


# project level import
from exicutive import views
from client import views as c
from candidate import views as ca

# Third Party Imports
from rest_framework.routers import SimpleRouter

# intialize DefaultRouter
router = SimpleRouter()
# register accounts app urls with router
router.register(r'user', views.managerlist, base_name='manager')
router.register(r'client',c.addclient,base_name='client')
router.register(r'candidate',ca.addcandidate,base_name='candidate')
# router.register(r'client', views.managerlist2, base_name='manager2')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('greet/',views.GreetingView.as_view()),
    # # path('greet1/',views. MorningGreetingView.as_view()),
    # path('greet2/',views.MyView.as_view()),
    # path('reg/',views.manager2.as_view()),
    # path('login/',views.login.as_view()),
    # path('manager/',views.managerlist.as_view()),
    path('api/', include((router.urls, 'api'), namespace='v1')),

]
