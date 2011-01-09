from coupons.backends import DefaultCouponRedemptionBackend


class CouponRedemptionBackend(DefaultCouponRedemptionBackend):
    """Provides authorization rules for coupon redemption."""

    supports_object_permissions = True
    supports_anonymous_user = True

    def authenticate(self, username, password):
        return None

    def has_perm(self, user, perm, obj=None):
        if perm == 'coupons.redeem':
            authorized = super(CouponRedemptionBackend, self).has_perm(user, perm, obj)
            if authorized:
                # Users can redeem a maximum of one coupon code.
                if user.coupon_redemptions.count() > 0:
                    return False
                return True
            else:
                return False
