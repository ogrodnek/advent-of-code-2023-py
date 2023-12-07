from dataclasses import dataclass
from enum import Enum
from collections import Counter
from functools import cmp_to_key


class HandType(Enum):
    FiveOfAKind = 7
    FourOfAKind = 6
    FullHouse = 5
    ThreeOfAKind = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1


def card_rank(card: str) -> int:
  rank = { "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10 }
  return rank.get(card, int(card) if card.isdigit() else 0)

def hand_type(cards: list[str]) -> HandType:
    match [v[1] for v in Counter(cards).most_common(2)]:
        case [5]:
            return HandType.FiveOfAKind
        case [4, 1]:
            return HandType.FourOfAKind
        case [3, 2]:
            return HandType.FullHouse
        case [3, 1]:
            return HandType.ThreeOfAKind
        case [2, 2]:
            return HandType.TwoPair
        case [2, 1]:
            return HandType.OnePair
        case _ :
            return HandType.HighCard

@dataclass
class Hand:
    cards: list[str]
    bid: int

    @property
    def hand_type(self) -> HandType:
        return hand_type(self.cards)

    def __repr__(self):
        return f"Hand({self.cards}, {self.bid})"

def compare_hands(hand1: Hand, hand2: Hand) -> int:    
    comp = hand1.hand_type.value - hand2.hand_type.value
    if comp != 0:
        return comp
    for card1, card2 in zip(hand1.cards, hand2.cards):
        comp = card_rank(card1) - card_rank(card2)
        if comp != 0:
            return comp
    return 0


def parse_hand(line: str) -> Hand:
    cards, bid = line.split(" ")
    return Hand(list(cards), int(bid))


with open("input.txt") as f:
    hands = [parse_hand(line) for line in f.readlines()]
    sorted = sorted(hands, key=cmp_to_key(compare_hands))

    total = sum([hand.bid * (index+1) for index, hand in enumerate(sorted)])
    print(total)
