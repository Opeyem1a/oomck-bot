import unittest

from .translate import Translate


class TestTranslate(unittest.TestCase):
    def test_translate_to_english(self):
        self.assertEqual(
            Translate.translate_to_english("Dette er en test"),
            ("This is a test", "no")
        )

    def test_transate_to_lang(self):
        self.assertEqual(
            Translate.translate_to_lang("This is a test", 'no'),
            ("Dette er en test", "en")
        )

    def test_transate_text(self):
        self.assertEqual(
            Translate.translate_to_lang("This is a test", 'no'),
            ("Dette er en test", "en")
        )
