# Musical Instrument Inventory

# The class which defines the structure and behavior of musical instruments
class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name # instance variable for the name of the instrument
        self.instrument_type = instrument_type # instance variable for the type of the instrument

    def play(self):
        print(f'The {self.name} is fun to play!')

    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.' # prints output anywhere the method is called

# Objects created from the MusicalInstrument class
instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

# Calling methods on the instrument objects to demonstrate their functionality. Since get_fact() returns a string instead of printing it directly, you need to use print() to display the returned string.
instrument_1.play()
print(instrument_1.get_fact())
instrument_2.play()
print(instrument_2.get_fact())