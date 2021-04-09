class Shape:
    _name = "default"
    _type = "default"
    points = []

    def __init__(self, a_name, a_type,*args):
        self._name = a_name
        self._type = a_type
        self.points = args
shape1 = Shape("R1","rectangle",(4),(5),(6),(7))

print(shape1._name)
