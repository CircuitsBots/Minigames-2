class SpecialType:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"<Special Type {self.name}>"


MISSING = SpecialType("missing")
