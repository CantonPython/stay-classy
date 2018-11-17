
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

# Create some basic items.
book = Item('book', 'an old red book')
keys = Item('keys', 'a set of jangly keys')
lantern = Item('lantern', 'a brass lantern')
torch = Item('torch', 'an old wooden torch')
wand = Item('wand', 'a wand inscribed with the word xyzzy')

items = [book, keys, lantern, wand]
for item in items:
    item.describe()
