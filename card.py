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

# this takes every number and every card color so i can make a complete deck
COLORS = {
        'r':"red",
        'y':"yellow",
        'g':"green",
        'b':"blue"
    }

NUMBERS = {
        '0':['0',False],
        '1':['1',False],
        '2':['2',False],
        '3':['3',False],
        '4':['4',False],
        '5':['5',False],
        '6':['6',False],
        '7':['7',False],
        '8':['8',False],
        '9':['9',False],
        '+':['+2',True],
        '&':['reverse',True],
        'x':["skip",True], 
    }

# This is a class that stores a singer card
# it requires a number and a color and checks to make sure its valid.
class Card():
    def __init__(self, number, color):
        
        #base validation to remove possible errors down the line 
        if number not in NUMBERS:
            raise ValueError(number+" is not a recognized number")
        
        elif color not in COLORS:
            raise ValueError(color+" is not a recognized color")
        
        self.number = number
        self.color = color
    
    #      built in functions
    
    #if printing out the card its 'user' friendly
    def __str__(self):
        return NUMBERS[self.number][0]+" : "+COLORS[self.color]
    def __repr__(self): # do the same in lists
        return str(self)
    
    def is_special_card(self): #is a +2, +4, reverse ECT
        return NUMBERS[self.number][1]
    
    # get the number value of the card
    def number_check(self,number): 
        return number == self.number
    
    # compare to cards to see if they are the same
    def card_check(self,card):

        if self.color == card.color: #color check
            return True
        elif self.number == card.number: #number check
            return True
        else:
            return False

if __name__ == "__main__":
    None
    card1 = Card("1",'r')
    print(card1)