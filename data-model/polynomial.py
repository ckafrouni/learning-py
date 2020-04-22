class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs
    
    # --------------------------- #
    def __add__(self, other):
        return Polynomial(
            *(x+y for x, y in zip(self.coeffs, other.coeffs)), 
            *self.coeffs[len(other)::],
            *other.coeffs[len(self)::],
        )
    
    def __sub__(self, other):
        return Polynomial(
            *(x-y for x, y in zip(self.coeffs, other.coeffs)),
            *self.coeffs[len(other)::],
            *other.coeffs[len(self)::],
        )
    # --------------------------- #
    def __eq__(self, other):
        return self.coeffs == other.coeffs

    def __lt__(self, other):
        return len(self) - len(other) < 0
    
    def __le__(self, other):
        return len(self) - len(other) <= 0
    
    def __gt__(self, other):
        return len(self) - len(other) > 0
    
    def __ge__(self, other):
        return len(self) - len(other) >= 0
    # --------------------------- #
    def __neg__(self):
        return Polynomial(*(-x for x in self.coeffs))
    
    def __abs__(self):
        return Polynomial(*(-x if x < 0 else x for x in self.coeffs))
    
    def __reversed__(self):
        return Polynomial(*reversed(self.coeffs))
    
    def __complex__(self):
        return Polynomial(*(complex(f'{x}j') for x in self.coeffs))
    # --------------------------- #
    def __lshift__(self, other):
        return Polynomial(*self.coeffs, *[0 for _ in range(other)])

    def __rshift__(self, other):
        return Polynomial(*self.coeffs[:len(self)-other])

    def __rlshift__(self, other):
        self <<= other

    def __rrshift__(self, other):
        self >>= other
    # --------------------------- #
    def __getitem__(self, key):
        if (type(key) != int):
            raise TypeError(f'type({key}) != int')
        elif (key > len(self)-1 ):
            raise IndexError(f"index {key} is out of bound. ( --> max index = {len(self)-1})")
        return self.coeffs[len(self) - key - 1]
    
    def __setitem__(self, key, value):
        coeffs = list(self.coeffs)
        if key >= len(self):
            coeffs += [0 for _ in range(-len(self)+1+key)]
        coeffs[key] = value
        self.coeffs = tuple(reversed(coeffs))
    # --------------------------- #
    def __len__(self):
        return len(self.coeffs)
    
    def __iter__(self):
        return iter(self.coeffs)
    # --------------------------- #
    def __repr__(self):
        return f'Polynomial{self.coeffs}'
    
    def __str__(self):
        tmp = [f'{coeff}x^{i} + ' if i>1 else f'{coeff}{"x + "*i}'\
            for i, coeff in reversed(list(enumerate(reversed(self))))]
        return ''.join(tmp)
    
    def __format__(self, format_spec='Ò'):
        return str(self)
    


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(1, 2, 3, 4, 5, 6)

