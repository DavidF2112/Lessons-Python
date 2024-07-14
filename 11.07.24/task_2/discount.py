class Discount:
    def discount(self):
        return 0


class DiscountSilver(Discount):
    def discount(self):
        return 0.1


class DiscountGold(Discount):
    def discount(self):
        return 0.2


class DiscountPlatinum(Discount):

    def discount(self):
        return 0.3