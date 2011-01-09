from django.conf.urls.defaults import *


urlpatterns = patterns('',
    # Direct the user to the coupon redeem page for now.
    url(regex=  u'^$',
        view=   'django.views.generic.simple.redirect_to',
        kwargs= dict(
            url='/coupons/redeem/',
            permanent=False,
        ),
    ),
    # Also, direct individual redemptions to the list of
    # redemptions, to clean up the URL.
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
