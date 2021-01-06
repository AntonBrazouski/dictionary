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
x
    def __str__(self):
        return self.word


class Meaning(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    order = models.IntegerField(unique=True)
    meaning_text = models.CharField(max_length=200)

    def __str__(self):
        return self.meaning_text
