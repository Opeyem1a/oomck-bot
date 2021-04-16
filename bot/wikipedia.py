import string

import wikipediaapi


class Wikipedia:

    def __init__(self):
        self.wiki = wikipediaapi.Wikipedia('en')

    def get_page_summary_intro(self, page_title):
        """
        :param page_title: Page title to retrieve the summary for
        :return: The first sentence of the requested page's summary
        """
        summary = self._get_page_summary(page_title)
        return self._get_first_sentence(summary) if summary is not None else None

    def _get_page_summary(self, page_title):
        """
        :param page_title: Page title to retrieve the summary for
        :return: The summary for this page, given that it exists
        """
        page = self._get_page(page_title)
        return page.summary if page is not None else None

    def _get_page(self, page_title):
        """
        :param page_title: Page title to retrieve the page for
        :return: The requested page, if it exists in Wikipedia
        """
        page = self.wiki.page(page_title)
        return page if page.exists() else None

    def _get_first_sentence(self, text: string):
        """
        :param text: Any string to retrieve the first sentence from
        :return: The first sentence of this string
        """
        try:
            first_sentence = text.split(':')[1].split('.')[0]
        except IndexError:
            first_sentence = text.split('.')[0]
        return f"{self._strip(first_sentence)}"

    @staticmethod
    def _strip(text: string):
        """
        Removes trailing and leading new lines and replaces double spaces with single spaces
        :param text: Any text
        :return: The stripped text
        """
        return text.strip() \
            .replace('\n', '') \
            .replace('  ', ' ')
