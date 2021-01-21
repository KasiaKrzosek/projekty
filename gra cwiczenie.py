import random
import time
from collections import Counter

def find_box():
    box_or_not = ['True', 'False']
    return random.choices(box_or_not,[60, 40])

def color_box():
    draw_color_box = ['green', 'orange', 'purple', 'gold']
    return random.choices(draw_color_box,[75, 20, 4, 1])

def reward_value(color):
    reward_value = {'green': 1000, 'orange': 4000, 'purple': 9000, 'gold': 160000}
    return reward_value[color]
"""
czysty kod
samoopisujace
english
"""

game_lenght = 0
total_reward = 0
counter_find = 0
draw_color_box = []
time0 = 1

while game_lenght < 5:
    time0 += 0.5    
    gamer_Answer = input("\nDo You want go forward?")
    find_box()
    find = find_box()[0]

    if gamer_Answer == "yes":
        print('\nGo...')
        time.sleep(time0)
        game_lenght += 1
        
        if find == 'True':
            print('\nYou find something!')
            time.sleep(time0)
            counter_find += 1
            draw_color = color_box()[0]
            print("color of box is",draw_color,"\nopening...")
            time.sleep(time0)
            draw_color_box.append(draw_color)
            reward = reward_value(draw_color)
            total_reward += reward
            print("\nYour reward is:",reward,"gold")       
        else:
            time.sleep(time0)
            print('nothing')
            continue
    else:
        print("sorry, just possibility go foreward")
        
    

print("\nYou find",counter_find,"boxes")
print("color of boxes is", draw_color_box)
print("total reward is",total_reward,"gold")



