from django.db import models

# Create your models here.
class Token(models.Model):
    VERB = 'V'
    NOUN = 'N'
    ADVERB = 'ADV'
    ADJECTIVE = 'ADJ'
    PHRASAL_VERB = 'PHV'
    OTHER = 'OTH'
    WORD_TYPE_CHOICES = [
        (VERB, 'Verb'),
        (NOUN, 'Noun'),
        (ADVERB, 'Adverb'),
        (ADJECTIVE, 'Adjective'),
        (PHRASAL_VERB, 'Phrasal verb'),
        (OTHER, 'Other')
    ]
    word = models.CharField(max_length=50)
    pronunciation = models.CharField(max_length=50)
    type = models.CharField(
        max_length=50,
        choices=WORD_TYPE_CHOICES,
        default= NOUN
    )

    def __str__(self):
        return self.word

    def has_no_meaning(self):
        return len(self.meaning_set.all()) == 0

    def has_one_meaning(self):
        return 0 < len(self.meaning_set.all()) < 2 

    def has_many_meanings(self):
        return len(self.meaning_set.all()) > 1


class Meaning(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    order = models.IntegerField(unique=True)
    meaning_text = models.CharField(max_length=200)

    def __str__(self):
        return self.meaning_text
