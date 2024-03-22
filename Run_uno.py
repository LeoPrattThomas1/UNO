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

#run with the amount of players in the code

from UNO import *
from csv import writer
import sys


def run_rounds():
    # this is the part that can be modified for different games of uno
    wins = [] 
    game_round = 0
    tot_rounds  = 10_000
    loading_per_rate = 5
    
    while True:
        game_round += 1
        
        #run until 10_000 games
        if game_round >= tot_rounds:
            break
        
        if ((game_round / (tot_rounds//loading_per_rate)) == #calculate the (game round / percentage round number)
            (game_round // (tot_rounds//loading_per_rate))): # see if the result is a round number
            
            print(f"{round((game_round / tot_rounds)*100)}% done")
    
        #set up game
        game_cur = UNO(int(sys.argv[1]))
        
        #run game, if the game has a error, just ignore that game
        try:
            winner = game_cur.round()
            # print(winner)
            wins.append(winner)
        except:
            print("error")
        
        
    return wins

def save_to_files(data):
    with open('/Users/leopratt-thomas/Desktop/GitHub2/UNO/game.csv', 'a') as f_object:
        
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)
        
            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(data)
        
            # Close the file object
            f_object.close()

if __name__ == "__main__":
    wins = [f"{sys.argv[1]} players"]
    wins.extend(run_rounds())
    # print(wins)
    # save_to_files(wins)