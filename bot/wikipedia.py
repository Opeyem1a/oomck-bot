import string

import wikipediaapi


class Wikipedia:

    def __init__(self):
        self.wiki = wikipediaapi.Wikipedia('en')

    def get_page_summary(self, page_title):
        page = self._get_page(page_title)
        return self._get_first_sentence(page.summary) if page is not None else None

    def _get_page(self, page_title):
        page = self.wiki.page(page_title)
        return page if page.exists() else None

    def _get_first_sentence(self, text: string):
        try:
            first_sentence = text.split(':')[1].split('.')[0]
        except IndexError:
            first_sentence = text.split('.')[0]
        return f"{self._strip(first_sentence)}"

    @staticmethod
    def _strip(text: string):
        # remove trailing and leading new lines
        # replace double spaces with single spaces
        return text.strip() \
            .replace('\n', '') \
            .replace('  ', ' ')
