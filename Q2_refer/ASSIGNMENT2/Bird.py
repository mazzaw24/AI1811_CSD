class Bird:
    def __init__(self, xType, xRate, xWing):
        self.type = xType
        self.rate = xRate
        self.wing = xWing
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.type},{self.rate},{self.wing})"