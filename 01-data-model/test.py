from frenchdeck import FrenchDeck, Card




if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()
    print(deck._cards)
    print(deck.ranks)
    print(deck.suits)