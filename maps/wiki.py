"""API MediaWiki file"""
import requests


class Wiki:
    """Uses Wikipedia's API to fetch extract and link of the page"""
    def __init__(self, question):
        self.question = question
        self.url = 'https://fr.wikipedia.org/w/api.php'
        self.params = {'action': 'query',
                       'generator': 'search',
                       'prop': 'extracts',
                       'explaintext': True,
                       'indexpageids': True,
                       'exsentences': 3,
                       'gsrlimit': 1,
                       'gsrsearch': self.question,
                       'exsectionformat': 'plain',
                       'format': 'json'
                       }

    def search(self):
        """Search page_id, Wikipedia summary extract and page's link"""
        try:
            response = requests.get(self.url, self.params)
            result = response.json()
            page_id = result['query']['pageids'][0]
            page = result['query']['pages'][page_id]['extract']
            url = 'http://fr.wikipedia.org/?curid=' + page_id
            return {'page': page, 'url': url}

        except IndexError:
            return "no result found"

        except KeyError:
            return 'no result found'
