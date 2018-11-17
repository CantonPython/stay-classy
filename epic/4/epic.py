
class Item:
    def __init__(self, desc, big=False):
        self.desc = desc
        self.big = big

    def __repr__(self):
        return 'Item(desc="{self.desc}", '\
               'big={self.big})'.format(self=self)

    def describe(self):
        print(self.desc)

class LightSource(Item):
    def __init__(self, desc):
        super().__init__(desc)
        self.lit = False

    def __repr__(self):
        return 'LightSource(lit={0}, '\
               'super={1})'.format(self.lit, super().__repr__())

    def on(self):
        if self.lit:
            print('already on')
        else:
            self.lit = True;

    def off(self):
        if self.lit:
            self.lit = False
        else:
            print('already off')

    def describe(self):
        if self.lit:
            print('lit', end=' ')
        else:
            print('unlit', end=' ')
        super().describe()


class Location:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = []
        self.exits = dict(
            north=None,
            south=None,
            east=None,
            west=None,
            up=None,
            down=None,
        )

    def __repr__(self):
        return 'Location(name="{self.name}", '\
               'desc="{self.desc}", '\
               'items={self.items}, '\
               'exits={self.exits})'\
               .format(self=self)

    def describe(self):
        print(self.desc)
        if self.items:
            print('You see')
            for item in self.items:
                item.describe()
        print()

    def on_enter(self):
        self.describe()

    def on_exit(self):
        pass

class Player:

    def __init__(self, name, location=None):
        self.name = name
        self.health = 100
        self.items = []
        self.location = location

    def __repr__(self):
        return 'Player(name="{self.name}", '\
               'health={self.health}, '\
               'items={self.items}, '\
               'location={self.location})'\
               .format(self=self)

    def move(self, direction):
        _from = self.location
        _to = _from.exits.get(direction)
        if not _to:
            print("You can't go that way.")
        else:
            _from.on_exit()
            _to.on_enter()
            self.location = _to

#------------------------------------------------------------------------------------
# Items

# Create some basic items.
book = Item('old red book')
keys = Item('set of jangly keys')
lantern = LightSource('brass lantern')
torch = LightSource('old wooden torch')
wand = Item('wand inscribed with the word xyzzy')

items = [book, keys, lantern, wand]
for item in items:
    item.describe()

print('Demo light source class')
lantern.describe()
lantern.on()
lantern.describe()
lantern.off()
lantern.off()

# ------------------------------------------------------------------------------------
# Locations

road = Location('road',
    'You are standing on a dirt road. You see a small '\
    'wellhouse to the north.');
wellhouse = Location('wellhouse',
    'You are in a small wellhouse. Stairs lead '\
    'down to passage in the dark.')
chamber = Location('chamber',
    'This small chamber has stairs leading up, '\
    'and doors on the east and west walls.')

# Map
road.exits['north'] = wellhouse
wellhouse.exits['south'] = road
wellhouse.exits['down'] = chamber
chamber.exits['up'] = wellhouse

# Populate items
wellhouse.items.append(lantern)
wellhouse.items.append(keys)
chamber.items.append(book)

locations = [road, wellhouse, chamber]
for location in locations:
    location.describe()


# ------------------------------------------------------------------------------------
# Player

player = Player('Mongo', location=road)
print(player)

player.move('north')
player.move('down')
player.move('up')
player.move('south')
player.move('south')
