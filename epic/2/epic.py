
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
