class MaxTotalCouponRedemptionsBackend(object):
    """Provides authorization rules for coupon redemption."""

    supports_object_permissions = True
    supports_anonymous_user = True

    def authenticate(self, username, password):
        return None

    def has_perm(self, user, perm, obj=None):
        # Users can redeem a maximum of one coupon code.
        if perm == 'coupons.redeem':
            if user.is_authenticated():
                if user.coupon_redemptions.count() == 0:
                    return True
                else:
                    return False
