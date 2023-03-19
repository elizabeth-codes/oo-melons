"""Classes for melon orders."""


class AbstractMelonOrder:

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        if self.species == "Christmas melon":
            base_price == 1.5 * base_price
            total = (1 + self.tax) * self.qty * base_price
        if self.qty > 10 and self.order_type == "international":
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    # order_type = "domestic"
    # tax = 0.08
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        # super init #belongs here
        # self.species = species
        # self.qty = qty
        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    # order_type = "international"
    # tax = 0.17

    def __init__(self, country_code, species, qty):
        """Initialize melon order attributes."""
        # super init #belongs here
        # self.species = species
        # self.qty = qty
        super().__init__(species, qty, "international", .17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


example_order = AbstractMelonOrder("melon", 5, "international", 0.17)
print(example_order)

# species, qty, order_type, tax