from egwproject.settings.base import *


ROOT_URLCONF = 'evergreeninterviews.urls.base'

AUTHENTICATION_BACKENDS += (
    # Coupons
    'evergreeninterviews.backends.CouponRedemptionBackend',
)

INSTALLED_APPS = (
    # Include egwproject as an app so we can access templates, media, admin.
    'evergreeninterviews',
) + INSTALLED_APPS
