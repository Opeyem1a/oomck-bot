import string

from es import ElasticSearch
from nlp.cleaner import Cleaner
from nlp.translate import Translate

DEFAULT = [
    "Sorry, I don't get what you're saying, can you try again?",
    "I don't quite follow, could you try repeating that in a different way?",
    "I'm not sure if I remember that happening in the Fast & Furious movies...",
    "Are you describing a specific scene? Which characters were involved?",
    "You're interesting...Out of curiosity, what is your favourite Fast & Furious movie?",
    "I don't understand, but I'm interested, what do you think Dom would say if you said that to him?",
    "Well...I'm not sure how to respond. Let's change the topic - What do you think about Tyrese?",
    "I don't know how to follow that up haha. To change the topic - What do you think about Dom?",
    "Intriguing, but let's get back on topic - What do you think about Paul Walker?"
]

ENDING = [
    ", but why are we talking about this instead of the Fast and Furious movie franchise?",
    ". I'm not sure how to respond to that. Let's change the topic - What do you think about Tyrese?",
    ". Intriguing, but let's get back on topic - What is your favourite Fast and Furious movie?",
    ", I don't quite follow, could you try repeating that in a different way?",
]


class Bot:
    """
    The main bot class
    """

    def __init__(self):
        self.cleaner = Cleaner
        self.es = ElasticSearch
        self.translate = Translate

    def ask(self, raw_input_string):
        """
        :param raw_input_string: Users question as raw string
        :return: Bots response as string
        """
        translated_input_string, lang = self.translate.translate_to_english(raw_input_string)
        query = self.cleaner.clean(translated_input_string)
        results = self.es.search(query)

        if len(results) > 0:
            response = results[0]["_source"]['response']
            response, src_lang = self.translate.translate_to_lang(response, lang)
            return response

        return self._get_default_response(query, lang)

    def _get_default_response(self, cleaned_query: string, lang: string):
        from random import randint
        response = self._get_wikipedia_summary(cleaned_query)

        if response is None:
            response = DEFAULT[randint(0, len(DEFAULT) - 1)]
        else:
            response += ENDING[randint(0, len(ENDING) - 1)]

        return self.translate.translate_to_lang(response, lang)[0]

    @staticmethod
    def _get_wikipedia_summary(query):
        from nlp.tokenizer import Tokenizer
        from nlp.pos_tagger import POSTagger

        tokenized = Tokenizer.tokenize(query)
        tagged_tokens = POSTagger.tag(tokenized)
        page_title = next((noun[0] for noun in tagged_tokens if noun[1] == 'NN'), None)

        if page_title is None:
            return None

        from .wikipedia import Wikipedia
        wikipedia = Wikipedia()
        return wikipedia.get_page_summary_intro(page_title)
