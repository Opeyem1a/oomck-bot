import string

import six

from google.cloud import translate_v2 as translate


class Translate:

    @staticmethod
    def translate_to_english(text):
        return Translate.translate_text(text, 'en')

    @staticmethod
    def translate_to_lang(text, lang):
        return Translate.translate_text(text, lang)

    @staticmethod
    def translate_text(text: string, target_lang: string):
        """Translates text into the target language. From Google Developer Quickstart Guide

        Target must be an ISO 639-1 language code.
        See https://g.co/cloud/translate/v2/translate-reference#supported_languages
        """
        translate_client = translate.Client()

        if isinstance(text, six.binary_type):
            text = text.decode("utf-8")

        result = translate_client.translate(text, target_language=target_lang)
        result = dict(result)

        Translate.log_translation(result)

        # if the original language is the same as the target language then return the original string
        # (to avoid modifying strings we already understand)
        if result.get('detectedSourceLanguage') == target_lang:
            return text, target_lang

        # otherwise return the translated string
        return result.get('translatedText', None), result.get('detectedSourceLanguage', None)

    @staticmethod
    def log_translation(result: dict):
        print(f"Translation | {result.get('input')} -> "
              f"{result.get('translatedText')} | "
              f"Source Lang: {result.get('detectedSourceLanguage')}")
