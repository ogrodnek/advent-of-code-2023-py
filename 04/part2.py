from dataclasses import dataclass

@dataclass
class Card:
    index: int
    winning: set[str]
    hand: set[str]

    @property
    def cards_won(self) -> int:
        return len(self.winning.intersection(self.hand))


def score_cards(deck: list[Card], cards: list[Card]) -> int:
    if len(cards) == 0:
        return 0
    
    card, *remaining = cards
    
    won_cards = deck[card.index + 1: card.index + card.cards_won + 1]
    return card.cards_won + score_cards(deck, won_cards) + score_cards(deck, remaining)
    

def parse_card(index: int, line: str) -> Card:
    a, b = line.split(":")[1].strip().split("|")
    return Card(index, set(a.split()), set(b.split()))


with open("input.txt") as f:
    cards = [parse_card(idx, line) for idx, line in enumerate(f.readlines())]
    print(score_cards(cards, cards) + len(cards))
