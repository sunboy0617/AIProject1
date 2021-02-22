from Algorithm import Astar, Faster_Astar, is_trans_successful
from Algorithm_DC import Astar_algo_DC
import time
import random

height = 7
width = 7
k = 6*height*width
start = list(range(height*width))
random.shuffle(start)
goal = [i for i in range(1, height*width)]
goal.append(0)
valid_count = 0
time_a = 0.0

for times in range(20):
    random.shuffle(start)

    if is_trans_successful(start, goal, height, width) == False:
        print(str(times)+" fail")
    else:
        print(str(times)+ " ok")
        time1=time.time()
        result = Astar_algo_DC(start, goal, height, width)
        time2=time.time()
        for ii in range(len(result)):
            print(result[i])
        valid_count = valid_count + 1
        time_a = time_a + time2 -time1

time_a = time_a / valid_count
print("average time:",time_a)