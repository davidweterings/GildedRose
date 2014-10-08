from item import Item


class GildedRose:
    def __init__(self):
        self.items = [
            Item('+5 Dexterity Vest', 10, 20),
            Item('Aged Brie', 2, 0),
            Item('Elixir of the Mongoose', 5, 7),
            Item('Sulfuras, Hand of Ragnaros', 0, 80),
            Item('Backstage passes to a TAFKAL80ETC concert', 15, 20),
            Item('Conjured Mana Cake', 3, 6),
        ]

    def update_quality(self):
        for i in range(0, len(self.items)):
            if ('Aged Brie' != self.items[i].name and
                'Backstage passes to a TAFKAL80ETC concert' != self.items[i].name):
                if self.items[i].quality > 0:
                    if 'Sulfuras, Hand of Ragnaros' != self.items[i].name:
                        self.items[i].quality = (self.items[i].quality - 1)
            else:
                if self.items[i].quality < 50:
                    self.items[i].quality = (self.items[i].quality + 1)
                    if 'Backstage passes to a TAFKAL80ETC concert' == self.items[i].name:
                        if self.items[i].sell_in < 11:
                            if self.items[i].quality < 50:
                                self.items[i].quality = (self.items[i].quality + 1)

                        if self.items[i].sell_in < 6:
                            if self.items[i].quality < 50:
                                self.items[i].quality = (self.items[i].quality + 1)

            if 'Sulfuras, Hand of Ragnaros' != self.items[i].name:
                self.items[i].sell_in = (self.items[i].sell_in - 1)

            if self.items[i].sell_in < 0:
                if 'Aged Brie' != self.items[i].name:
                    if 'Backstage passes to a TAFKAL80ETC concert' != self.items[i].name:
                        if self.items[i].quality > 0:
                            if 'Sulfuras, Hand of Ragnaros' != self.items[i].name:
                                self.items[i].quality = (self.items[i].quality - 1)
                    else:
                        self.items[i].quality = (self.items[i].quality - self.items[i].quality)
                else:
                    if self.items[i].quality < 50:
                        self.items[i].quality = (self.items[i].quality + 1)


def main():
    gilded_rose = GildedRose()
    gilded_rose.update_quality()


if __name__ == '__main__':
    main()
