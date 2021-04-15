import unittest

from bot import Bot, DEFAULT


class TestBot(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBot, self).__init__(*args, **kwargs)
        self.bot = Bot()

    def test_bot(self):
        self.assertEqual(self.bot.ask("hi"), "Hey.")

    def test_bot_unknown_string(self):
        from nlp.translate import Translate
        test = "sadfkljdfkjlhfd"
        detected_lang = Translate.translate_to_english(test)[1]
        translated_default = [Translate.translate_to_lang(i, detected_lang)[0] for i in DEFAULT]
        self.assertIn(self.bot.ask(test), translated_default)
