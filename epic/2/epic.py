
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
