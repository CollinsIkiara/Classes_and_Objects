# Planet Class

# This code defines a Planet class with attributes for name, planet type, and star. It includes methods for orbiting and string representation.
class Planet:
    def __init__(self, name, planet_type, star):
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')
        if name == '' or planet_type == '' or star == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

# We create objects from the Planet class.
planet_1 = Planet('Earth', 'terrestrial', 'Sun')
planet_2 = Planet('Venus', 'terrestrial', 'Sun')
planet_3 = Planet('Jupiter', 'gas', 'Sun')

# We print the string representation of each planet.
print(planet_1)
print(planet_2)
print(planet_3)

# We call the orbit method for each planet and print the result.
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())