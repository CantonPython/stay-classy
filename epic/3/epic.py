
class Item:
    def __init__(self, name, desc, big=False):
        self.name = name
        self.desc = desc
        self.big = big

    def __repr__(self):
        return 'Item(name={self.name}, '\
               'desc="{self.desc}", '\
               'big={self.big})'.format(self=self)

    def describe(self):
        print(self.desc)

class LightSource(Item):
    def __init__(self, name, desc):
        super().__init__(name, desc)
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
        desc = self.desc
        if self.lit:
            desc = desc + ', lit'
        print(desc)


class Location:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = dict()
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

    def place(self, item):
        name = item.name
        self.items[name] = item

    def remove(self, name):
        item = self.items[name]
        del self.items[name]
        return item

    def describe(self):
        print(self.desc)
        if self.items:
            print('You see')
            for item in self.items.values():
                item.describe()
        print('')

    def on_enter(self):
        self.describe()

    def on_exit(self):
        pass

#------------------------------------------------------------------------------------
# Items

# Create some basic items.
book = Item('book', 'an old red book')
keys = Item('keys', 'a set of jangly keys')
lantern = LightSource('lantern', 'a brass lantern')
torch = LightSource('torch', 'an old wooden torch')
wand = Item('wand', 'a wand inscribed with the word xyzzy')

items = [book, keys, lantern, wand]
for item in items:
    item.describe()

# Demo light source class.
print('Turn lantern on and off')
lantern.describe()
lantern.on()
lantern.describe()
lantern.off()
lantern.describe()
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
wellhouse.place(lantern)
wellhouse.place(keys)
chamber.place(book)

locations = [road, wellhouse, chamber]
for location in locations:
    location.describe()

