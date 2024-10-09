# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)

    # Test +5 Dexterity Vest decreases in quality and sell_in over time
    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [
            Item(vest, 1, 2),
            Item(vest, 9, 19),
            Item(vest, 4, 6)
        ]
        gr = GildedRose(items)
        gr.update_quality()

        # self.assertEqual(items[0].sell_in, 1)  # Deliberately incorrect: should be 0
        # self.assertEqual(items[0].quality, 2)  # Deliberately incorrect: should be 1
        #
        # self.assertEqual(items[1].sell_in, 10)  # Deliberately incorrect: should be 8
        # self.assertEqual(items[1].quality, 20)  # Deliberately incorrect: should be 18
        #
        # self.assertEqual(items[2].sell_in, 5)  # Deliberately incorrect: should be 3
        # self.assertEqual(items[2].quality, 7)  # Deliberately incorrect: should be 5
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 1)

        self.assertEqual(items[1].sell_in, 8)
        self.assertEqual(items[1].quality, 18)

        self.assertEqual(items[2].sell_in, 3)
        self.assertEqual(items[2].quality, 5)

    # Test Aged Brie increases in quality over time
    def test_aged_brie_increases_in_quality(self):
        items = [
            Item("Aged Brie", 2, 0),  # Normal case
            Item("Aged Brie", 0, 10),  # After sell-by date has passed
            Item("Aged Brie", 5, 50)  # Quality at maximum value
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Deliberately set wrong expected values to ensure the test fails
        # self.assertEqual(items[0].quality, 2)  # Deliberately incorrect: expected value should be 1
        # self.assertEqual(items[1].quality, 12)  # Deliberately incorrect: expected value should be 12
        # self.assertEqual(items[2].quality, 49)  # Deliberately incorrect: quality should remain 50
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[1].quality, 12)
        self.assertEqual(items[2].quality, 50)

    # Test Backstage passes increase in quality as the event approaches
    def test_backstage_passes_increases_in_quality(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),  # 15 days left
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 30),  # 5 days left
            Item("Backstage passes to a TAFKAL80ETC concert", 1, 45)  # 1 day left
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # # Deliberately set wrong expected values to ensure the test fails
        # self.assertEqual(items[0].quality, 22)  # Deliberately incorrect: expected value should be 21
        # self.assertEqual(items[1].quality, 35)  # Deliberately incorrect: expected value should be 33
        # self.assertEqual(items[2].quality, 50)  # Deliberately incorrect: expected value should be 48
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[1].quality, 33)
        self.assertEqual(items[2].quality, 48)

    # Test Conjured Mana Cake quality decreases faster
    def test_conjured_mana_cake_decreases_in_quality(self):
        items = [
            Item("Conjured Mana Cake", 3, 6),  # 3 days left
            Item("Conjured Mana Cake", 0, 6),  # After sell-by date has passed
            Item("Conjured Mana Cake", 1, 1)  # Quality close to 0
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # # Deliberately set wrong expected values to ensure the test fails
        # self.assertEqual(items[0].quality, 5)  # Deliberately incorrect: expected value should be 4
        # self.assertEqual(items[1].quality, 3)  # Deliberately incorrect: expected value should be 2
        # self.assertEqual(items[2].quality, -1)  # Deliberately incorrect: quality should not be negative, expected value should be 0
        self.assertEqual(items[0].quality, 4)
        self.assertEqual(items[1].quality, 2)
        self.assertEqual(items[2].quality, 0)

if __name__ == '__main__':
    unittest.main()
