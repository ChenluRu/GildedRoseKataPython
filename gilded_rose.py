# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

from abc import ABC, abstractmethod
class ItemStrategy(ABC):
    @abstractmethod
    def update(self, item):
        pass

class RegularItemStrategy(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class AgedBrieStrategy(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class BackstagePassStrategy(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(item.quality + 3, 50)
        elif item.sell_in < 10:
            item.quality = min(item.quality + 2, 50)
        else:
            item.quality += 1


class ConjuredItemStrategy(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality = max(0, item.quality - 2)
        if item.sell_in < 0 and item.quality > 0:
            item.quality = max(0, item.quality - 2)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = self.get_strategy(item)
            strategy.update(item)

    def get_strategy(self, item):
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassStrategy()
        elif item.name.startswith("Conjured"):
            return ConjuredItemStrategy()
        else:
            return RegularItemStrategy()

#     def update_quality(self):
#         for item in self.items:
#             if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
#                 if item.quality > 0:
#                     if item.name != "Sulfuras, Hand of Ragnaros":
#                         item.quality = item.quality - 1
#             else:
#                 if item.quality < 50:
#                     item.quality = item.quality + 1
#                     if item.name == "Backstage passes to a TAFKAL80ETC concert":
#                         if item.sell_in < 11:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#                         if item.sell_in < 6:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#             if item.name != "Sulfuras, Hand of Ragnaros":
#                 item.sell_in = item.sell_in - 1
#             if item.sell_in < 0:
#                 if item.name != "Aged Brie":
#                     if item.name != "Backstage passes to a TAFKAL80ETC concert":
#                         if item.quality > 0:
#                             if item.name != "Sulfuras, Hand of Ragnaros":
#                                 item.quality = item.quality - 1
#                     else:
#                         item.quality = item.quality - item.quality
#                 else:
#                     if item.quality < 50:
#                         item.quality = item.quality + 1
