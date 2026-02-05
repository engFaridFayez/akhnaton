"""
URL configuration for akhnaton project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from projects import views
from users import views as usersviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('',views.index,name='index'),
    path('projects/',views.project_list,name='projects'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
    path('add/', views.add_project, name='add_project'),
    path('projects/<int:id>/edit/', views.edit_project, name='edit_project'),
    path('projects/image/<int:image_id>/delete/', views.delete_project_image, name='delete_project_image'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('tools/',views.tools,name='tools'),
    path('consultants/',views.consultants,name='consultants'),
    path('sub-contractors/',views.subContractors,name='sub-contractors'),
    path('certificates-of-appreciation/',views.certificates_of_appreciation,name='certificates_of_appreciation'),
    path('services/',views.services,name='services'),
    path('employment/',views.employment_message_view,name='employment'),
    path('employment/success/', views.employment_success, name='employment_success'),
    path('company-profile/',views.download_company_profile,name='company-profile'),
    path('forbidden/', usersviews.forbidden, name='forbidden'),
    path('not-found/', usersviews.notFound, name='notFound'),
    
] 


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^.*$', usersviews.notFound),  # أي حاجة غير موجودة
]


handler404 = 'users.views.notFound'