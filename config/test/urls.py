"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

# from django.urls import path
from schemes.views import fetchschemes, fetch_scheme_groups, schemeGroups
from members.views import fetchmember, fetchcoverbenefits, postmembers
from claims.views import storeClaim, fetchclaimstatus, fetchreimb, fetchreimbs, claims_exp, fetch_fam_exp, \
    fetch_member_statement
from preauth.views import savepreauth
from users.views import fetch_users

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^scheme/', fetchschemes),
    url(r'^member_details/(?P<memno>[\w-]+)/$', fetchmember),
    url(r'^cover_benefits/(?P<memno>[\w-]+)/$', fetchcoverbenefits),
    url(r'^claims/save', storeClaim),
    url(r'^pre_auth/save', savepreauth),
    url(r'^claims/fetch_claim_status', fetchclaimstatus),
    url(r'^reimbursement/(?P<memno>[\w-]+)/$', fetchreimb),
    url(r'^reimbursements/', fetchreimbs),
    url(r'^post_members/', postmembers),
    url(r'^users/', fetch_users),
    url(r'^scheme_groups', fetch_scheme_groups),
    url(r'^scheme_group/(?P<scheme_id>[\w-]+)/$', schemeGroups),
    url(r'^claims_experience', claims_exp),
    url(r'^family_statement/(?P<family>[\w-]+)/(?P<year>[\w-]+)/$', fetch_fam_exp),
    url(r'^member_statement/(?P<member>[\w-]+)/(?P<year>[\w-]+)/$', fetch_member_statement),

]
