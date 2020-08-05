{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "suits = ('Hearts', 'Diamonds', 'Spades', 'Club')\n",
    "ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')\n",
    "values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,\n",
    "         'Queen':10, 'King':10, 'Ace':11}\n",
    "class Card():\n",
    "    def __init__(self,suit,rank):\n",
    "        self.rank = rank\n",
    "        self.suit = suit\n",
    "        self.value = values[rank]\n",
    "    def __str__(self):\n",
    "        return self.rank  +   \"of\"   +  self.suit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "twohearts = Card(\"Hearts\",\"Two\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TwoofHearts\n"
     ]
    }
   ],
   "source": [
    "print(twohearts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Two'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "twohearts.rank"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "twohearts.value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "twohearts.suit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Deck():\n",
    "    def __init__(self):\n",
    "        self.all_cards = []\n",
    "        for suit in suits:\n",
    "            for rank in ranks:\n",
    "                created_cards = Card(suit,rank)\n",
    "                self.all_cards.append(created_cards)\n",
    "    def shuffle(self):\n",
    "        return random.shuffle(self.all_cards)\n",
    "    def deal_one(self):\n",
    "        return self.all_cards.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "newdeck = Deck()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(newdeck.all_cards[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "newdeck.shuffle()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(newdeck.all_cards[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Player():\n",
    "    def __init__(self,name):\n",
    "        self.name = name\n",
    "        self.all_cards = []\n",
    "    def remove_one(self):\n",
    "        return self.all_cards.pop(0)\n",
    "    def add_cards(self,new_cards):\n",
    "        if type(new_cards) == type([]):\n",
    "        # if new_cards is a list of multiple cards\n",
    "            self.all_cards.extend(new_cards)\n",
    "        else:\n",
    "            self.all_cards.append(new_cards)\n",
    "    def __str__(self):\n",
    "        return f\"player {self.name} has {len(self.all_cards)} cards \""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " mycard = newdeck.deal_one()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(mycard)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "newplayer = Player(\"bob\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "abc = newplayer.add_cards(mycard)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(abc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(newplayer.all_cards[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(newdeck.all_cards)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(newplayer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "newplayer.add_cards([mycard,mycard,mycard])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(newplayer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "newplayer.remove_one()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(newplayer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "player_one = Player(\"one\")\n",
    "player_two = Player(\"two\")\n",
    "new_deck = Deck()\n",
    "new_deck.shuffle()\n",
    "\n",
    "for x in range(26):\n",
    "    player_one.add_cards(new_deck.deal_one())\n",
    "    player_two.add_cards(new_deck.deal_one())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "round 1 \n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'list' object has no attribute 'value'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-18-1bf3fa735f15>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     25\u001b[0m     \u001b[0mat_war\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     26\u001b[0m     \u001b[1;32mwhile\u001b[0m \u001b[0mat_war\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 27\u001b[1;33m         \u001b[1;32mif\u001b[0m \u001b[0mplayer_one_currentcards\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalue\u001b[0m \u001b[1;33m>\u001b[0m \u001b[0mplayer_two_currentcards\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     28\u001b[0m             \u001b[0mplayer_one\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mall_cards\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mplayer_one_currentcards\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     29\u001b[0m             \u001b[0mplayer_one\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mall_cards\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mplayer_two_currentcards\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'list' object has no attribute 'value'"
     ]
    }
   ],
   "source": [
    "round_nums = 0\n",
    "game_on = True\n",
    "\n",
    "while game_on:\n",
    "    \n",
    "    round_nums+=1\n",
    "    print(f\"round {round_nums} \")\n",
    "    \n",
    "    if len(player_one.all_cards) == 0:\n",
    "        print(\"player one out of cards! player two wins\")\n",
    "        game_one = False \n",
    "        break\n",
    "    if len(player_two.all_cards) == 0:\n",
    "        print(\"player two out of cards! player one wins\")\n",
    "        game_one = False \n",
    "        break\n",
    "        \n",
    "    player_one_currentcards = []\n",
    "    player_one_currentcards.append(player_one.remove_one())\n",
    "    \n",
    "    player_two_currentcards = []\n",
    "    player_two_currentcards.append(player_two.remove_one())\n",
    "    \n",
    "    \n",
    "    at_war = True\n",
    "    while at_war:\n",
    "        if player_one_currentcards[-1].value > player_two_currentcards[-1].value:\n",
    "            player_one.all_cards.append(player_one_currentcards)\n",
    "            player_one.all_cards.append(player_two_currentcards)\n",
    "            at_war = False\n",
    "        elif  player_one_currentcards[-1].value < player_two_currentcards[-1].value:\n",
    "            player_two.all_cards.append(player_one_currentcards)\n",
    "            player_two.all_cards.append(player_two_currentcards)\n",
    "            at_war = False\n",
    "        else:\n",
    "            print(\"WAR!\")\n",
    "            if len(player_one.all_cards) < 3:\n",
    "                print(\"player one unable to declare war! \")\n",
    "                print(\"player two wins\")\n",
    "                game_on = False\n",
    "                break\n",
    "            elif len(player_two.all_cards) < 3:\n",
    "                print(\"player two unable to declare war! \")\n",
    "                print(\"player one wins\")\n",
    "                game_on = False\n",
    "                break\n",
    "            else:\n",
    "                for i in range(3):\n",
    "                    player_one_currentcards.append(player_one.remove_one())\n",
    "                    player_two_currentcards.append(player_two.remove_one())\n",
    "                \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
