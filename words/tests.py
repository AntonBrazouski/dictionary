from django.test import TestCase
from django.urls import reverse

from .models import Token, Meaning

class TokenModelTest(TestCase):
    def test_has_no_meaning(self):
        no_meaning_token = Token()
        self.assertIs(no_meaning_token.has_no_meaning(), True)

    # def test_has_no_meaning_negative(self):
    #     token_with_meaning = Token()
    #     token_with_meaning.meaning_set.create()
    #     meaning = Meaning()
    #     meaning.token = token_with_meaning
    #
    #     self.assertIs(0, len(token_with_meaning.meaning_set.all()))
        # self.assertIs(token_with_meaning.has_no_meaning(), False)


def create_token(word='rat', pronunciation='rat', type='Noun'):
    return Token.objects.create(
        word=word, pronunciation=pronunciation,
        type=type)


class TokenIndexViewTests(TestCase):
    def test_no_token(self):
        response = self.client.get(reverse('words:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No words are available")
        self.assertQuerysetEqual(response.context['query'], [])

    def test_empty_token(self):
        create_token(word='rat', pronunciation='rat', type='Noun')
        response = self.client.get(reverse('words:index'))
        self.assertQuerysetEqual(
            response.context['query'],
            ['<Token: rat>']
        )

class TokenDetailViewTests(TestCase):
    def test_101_token(self):
        token = create_token()
        url = reverse('words:detail', args=(token.id +100,)) # no such token
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_good_token(self):
        token = create_token()
        url = reverse('words:detail', args=(token.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class TokenSearchViewTests(TestCase):
    def test_search(self):
        token = create_token()
        url = reverse('words:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_form(self):
        token = create_token()
        url = reverse('words:search')
        # query = request.GET['search'] # NameError
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
