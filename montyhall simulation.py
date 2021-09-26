#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 12:22:11 2021

@author: younessubhi

Simulation af monty hall i python
"""

import numpy as np
import matplotlib.pyplot as plt
import random

plt.style.use('fivethirtyeight')

#værten kender til hvad der er bag døren
#værten afslører en ged efter spilleren har lavet et initielt valg

def get_non_prize_door(host, num_doors, player_choice):
    i = 1
    while ( i == host or i == player_choice):
        i = (i+1) % (num_doors)
        
    return i

#spilleren skifter til den anden dør
    
def switch_function(shown_door, num_doors, player_choice):
    i = 1
    while (i == shown_door or i == player_choice):
        i = (i+1) % (num_doors)
        
    return i

#opret spillet
def monty_hall_game(switch, num_tests):
  win_switch_cnt = 0
  win_no_switch_cnt = 0
  lose_switch_cnt = 0
  lose_no_switch_cnt = 0
  doors = [0,1,2] ###definerer dørerne
  num_doors = len(doors) ###antal dører
  
  
  for i in range(0,num_tests):
    door_with_prize = random.randint(0, num_doors-1) #definer dør med pris *random*
    host = door_with_prize #afslør vinder dør til vært
    
    #spiller vælger dør *random
    player_choice = random.randint(0, num_doors-1) 
    original_player_choice = player_choice
    shown_door = get_non_prize_door(host, num_doors, player_choice)
    if switch == True:
      player_choice = switch_function(shown_door,num_doors, player_choice)
    
    #DATAOPSAMLING
    if player_choice == host and switch == False:
      #vind ved stædighed (skifter ikke dør)
      print('Player Wins (No switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice ,', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      win_no_switch_cnt = win_no_switch_cnt + 1
    elif player_choice == host and switch == True:
      #vind ved skift
      print('Player Wins (switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      win_switch_cnt = win_switch_cnt +1
    elif player_choice != host and switch == False:
      #tab ved stædighed (skifter ikke dør)
      print('Player Lost (No switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      lose_no_switch_cnt = lose_no_switch_cnt + 1
    elif player_choice != host and switch == True:
      #tab ved skift
      print('Player Lost (switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      lose_switch_cnt = lose_switch_cnt + 1
    else:
      print('ERROR')

  return win_no_switch_cnt,win_switch_cnt,lose_no_switch_cnt,lose_switch_cnt, num_tests

#SPIL OG GENERER STATISTIK

#spil spillet 
x = monty_hall_game(True, 1000)
print('Win switch %: ', x[1]/ x[4])
print('Lose switch %: ', x[3]/ x[4])
print('Win No switch %: ', x[0]/ x[4])
print('Lose No switch %: ', x[2]/ x[4])