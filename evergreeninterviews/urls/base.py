from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(regex=  u'^$',
        view=   'django.views.generic.simple.redirect_to',
        kwargs= dict(
            url='/coupons/redeem/',
            permanent=False,
        ),
    ),
    url(regex=  u'',
        view=   include('egwproject.urls.base'),
    ),
)
