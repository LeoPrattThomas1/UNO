
"""
    Finding the best possible strategy for a game of uno
    Copyright (C) 2024 Leo Pratt-Thomas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

#justin uncon shirt tall guy

from itertools import chain
import random
import card
import time

cards_start = 7

game_moves = False
winner = True

class UNO():
    def __init__(self,people):
        self.last_move = None
        self.stack_number = 0
        self.direction = +1 #postive 
        self.game_in_play = True
        self.winner = None
        
        
        #create a deck
        self.deck = list(
            chain.from_iterable(#flatten it to a 1d list
                [[card.Card(number,color) for color in card.COLORS] for number in card.NUMBERS]#make a 2d list of every card
                )
            )
        self.deck.extend(
            (
            chain.from_iterable(#flatten it to a 1d list
                [[card.Card(number,color) for color in card.COLORS] for number in card.NUMBERS]#make a 2d list of every card
                )
            )
        )
        
        #shuffle deck
        random.shuffle(self.deck)

        #start the first card
        self.discard = [self.draw()]
        
        
        #create players
        self.players = [Player([self.draw() for a in range(cards_start)]) for a in range(people)]
        
        if game_moves:
            print(self.top_card())
    
    #moves players can play in our game of uno

    #======== game moves =======
    def reshuffle_deck(self):
        if game_moves: 
            print("===== reshuffle ====")
        top_card = self.discard.pop(-1)
        
        #move all cards from the discard to the deck
        for a in self.discard:
            self.deck.append(self.discard.pop())
        
        #shuffle the deck
        random.shuffle(self.deck)
        
        #move the top card back to the discard
        self.discard.append(top_card)
        
        
        
    
    def draw(self):
        if game_moves:
            print(len(self.deck),"decksize")
        if len(self.deck) == 0:
                self.reshuffle_deck()  
                    
        return self.deck.pop(-1)
    def top_card(self):
        return self.discard[-1]

    #======== game logic =======
    #this does the logic connecting the player and the game in our game of uno

    #checks to see if the card can be played
    

    #sees what cards in you hand can be played
    def deck_check(self,deck):
        valid = []
        for card in deck:
            if self.top_card().card_check(card):
                valid.append(card)
        return valid
    
    
    
    #======== run game ===========
    
    def round(self, turn = 0):
        skip = 0
            
        if self.game_in_play:
            #if the turn is higer then the plays go back to 0
            if turn == len(self.players):
                turn = 0
            elif turn == -1:
                turn = len(self.players)-1
            #keep skip on a back to 0
            elif turn > len(self.players):
                turn = 1
            
            #if the game is almost over reshuffle deck  
                
                
            if game_moves: 
                print("player "+str(turn)+" turn")
                
                
            current_player = self.players[turn]
            
            #player move
            last_move = current_player.player_move(self, self.top_card())
            
            #put card in discard
            if last_move is not None:
                self.discard.append(last_move)
            
            #card actions
                if last_move.is_special_card():
                    
                    #plus
                    if last_move.number == "+":
                        self.stack_number += 2
                    
                    #skip
                    elif last_move.number == "x":
                        skip = 1
                    
                    #revurse direction
                    elif last_move.number == "&":
                        if self.direction == 1:
                            self.direction = -1
                            
                        elif self.direction == -1:
                            self.direction = 1
                    
                
            #win_uno check
            if current_player.win_check():
                self.game_in_play = False
                self.winner = turn
                #if winner:
                #    print(turn)
                return turn
            
            if game_moves: 
                print("turn over\n")
                print(str(self.top_card())+"\n")
                # str(input(""))
            
            #get next player
            self.round(turn+self.direction+skip)
        return self.winner
            
            


class Player():
    def __init__(self, deck):
        self.deck = deck
        #picking algorithm pick
    
    def win_check(self):
        if len(self.deck) == 0:
            if game_moves:
                print("game over")
            return True
        return False

    def player_move(self, game, last_card):
        self.game = game
        valid_cards = game.deck_check(self.deck)
        if game_moves: 
            print("cards",self.deck)
        
        #last player move was a +2
        if last_card.number == "+" and game.stack_number != 0:
            
            # plus_cards_TF_map = [card.number_check("+") for cards in self.deck]
            # #see if you have a +2
            # if any(plus_cards_TF_map):
            #     #play (+2)
            #     self.play(self.deck[plus_cards_TF_map.index(True)])
                
            # else:
            if True:
                for a in range(game.stack_number):
                    self.draw()
                game.stack_number = 0
                return None
                
                        #draw, skip
                
                
        else: #no
            return self.card_check(valid_cards)
                #you have a card? (create new algorithm)
                
                    
    def card_check(self,valid_cards):
        #yes 1 card
        if len(valid_cards) == 1:
            return self.play(valid_cards[0])
            #play card
            
        #no
        elif len(valid_cards) == 0:
            #draw
            self.draw()
            #recurse 
            return self.card_check(self.game.deck_check(self.deck))
            
        #yes many
        else:
            return self.play(self.run_algorithms(valid_cards))
            #run_algorithms!!!!!
    
    def run_algorithms(self,valid_cards):
        #pick algorithm
        return self.algorithm_random(valid_cards)
    
    
    
    #different algorithms to test.
    
    def algorithm_random(self,valid_cards):
        return random.choice(valid_cards)
    
    def algorithm_main_priority(self,valid_cards):
        pass
        
    def algorithm_special_priority(self,valid_cards):
        pass
    
    #draw card
    #add it to your deck
    def draw(self):
        
        draw_card = self.game.draw()#draw card
        self.deck.append(draw_card) #add it to your deck
        if game_moves: 
            print("drew card",draw_card)
        return draw_card
            
    
    #play card
    def play(self, card):
        #confirm card
        if card not in self.deck:
            raise ReferenceError("the card "+str(card)+" you dont have")
        #remove card from deck
        if game_moves: 
            print("played",card)
        return self.deck.pop(self.deck.index(card))
        
        

        
if __name__ == "__main__":
    start = time.time()
    for a in range(1000):
        game_1 = UNO(4)
        print(game_1.round())
    time_ran = time.time()-start
    print(time_ran)