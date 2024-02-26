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

from UNO import *
from csv import writer
import sys

# this is the part that can be modified for different games of uno
wins = [] 
a = 0
while True:
    a=a+1
    if a >= 10000:
        break
    game_1 = UNO(int(sys.argv[1]))
    try:
        winner = game_1.round()
    except:
        None
    print(winner)
    wins.append(winner)


with open('/Users/leopratt-thomas/Desktop/GitHub2/UNO/game.csv', 'a') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(wins)
    
        # Close the file object
        f_object.close()