import unittest

from bot.wikipedia import Wikipedia


class TestWikipedia(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestWikipedia, self).__init__(*args, **kwargs)
        self.wiki = Wikipedia()

    def test_get_page_summary_intro(self):
        self.assertEqual(self.wiki.get_page_summary_intro('message'),
                         "A message is a discrete unit of communication intended by the source for consumption by some"
                         " recipient or group of recipients")
