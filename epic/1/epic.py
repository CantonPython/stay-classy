
class Item:
    def __init__(self, desc, big=False):
        self.desc = desc
        self.big = big

    def __repr__(self):
        return 'Item(desc="{self.desc}", '\
               'big={self.big})'.format(self=self)

    def describe(self):
        print(self.desc)

# Create some basic items.
book = Item('an old red book')
keys = Item('a set of jangly keys')
lantern.off()
lantern = Item('a brass lantern')
torch = Item('an old wooden torch')
wand = Item('a wand inscribed with the word xyzzy')

items = [book, keys, lantern, wand]
for item in items:
    item.describe()
