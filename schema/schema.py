from graphene_django import DjangoObjectType
import graphene
from users.models import User as UserModel
from decks.models import Deck as DeckModel
from cards.models import Card as CardModel

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Deck(DjangoObjectType):
    class Meta:
        model = DeckModel

class Card(DjangoObjectType):
    class Meta:
        model = CardModel
        #fields = "__all__"


class Query(graphene.ObjectType):
    users = graphene.List(User)
    decks = graphene.List(Deck)
    cards = graphene.List(Card)

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_decks(self, info):
        return DeckModel.objects.all()
    def resolve_cards(self, info):
        return CardModel.objects.all()

schema = graphene.Schema(query=Query)