from django.conf.urls.defaults import *


urlpatterns = patterns('',
    # Direct the user to the coupons page.
    url(regex=  u'^$',
        view=   'django.views.generic.simple.redirect_to',
        kwargs= dict(
            url='/coupons/',
            permanent=False,
        ),
    ),
    # When conversion is done, direct back to the root URL.
    url(name=   'lazysignup_convert_done',
        regex=  u'^accounts/convert/done/$',
        view=   'django.views.generic.simple.redirect_to',
        kwargs= dict(
            url='/',
            permanent=False,
        ),
    ),
    # Direct individual redemptions to the list of redemptions, to clean up the URL.
    url(regex=  u'^coupons/redeemed/\d+/$',
        view=   'django.views.generic.simple.redirect_to',
        kwargs= dict(
            url='/coupons/redeemed/',
            permanent=False,
        ),
    ),
    url(regex=  u'',
        view=   include('egwproject.urls.base'),
    ),
)
