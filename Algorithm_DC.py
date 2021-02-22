import copy
import random
import time
from Algorithm import Astar_DC, is_trans_successful

def move_zero_pos(zero_pos, step, direction, height, width, result):
    temp_zero_pos = zero_pos
    if step == 0:
        return temp_zero_pos
    
    for i in range(int(abs(step))):
        state = copy.deepcopy(result[-1])
        if direction == 'up_down': #down step>0;  up step<0
            state[temp_zero_pos], state[temp_zero_pos+ int(step/abs(step))*width] = state[temp_zero_pos+int(step/abs(step))*width], state[temp_zero_pos]
            temp_zero_pos = temp_zero_pos+int(step/abs(step))*width
            result.append(state)
        elif direction == 'left_right': #right step>0; left step<0
            state[temp_zero_pos], state[temp_zero_pos+ int(step/abs(step))] = state[temp_zero_pos+int(step/abs(step))], state[temp_zero_pos]
            temp_zero_pos = temp_zero_pos+int(step/abs(step))
            result.append(state)
    return temp_zero_pos


def move_to_dest(temp_pos, init_zero_pos, zero_dest, h, w, result):
    temp_num = result[-1][temp_pos]
    if init_zero_pos == zero_dest:
        return init_zero_pos
    zero_pos = init_zero_pos
    if abs(zero_dest - temp_pos) == 1:#左右位置
        if temp_pos%w != zero_pos%w:
            if temp_pos // w != h-1:
                zero_pos = move_zero_pos(zero_pos, (temp_pos//w+1-zero_pos//w),'up_down',h,w,result)
                zero_pos = move_zero_pos(zero_pos, (zero_dest%w-zero_pos%w),'left_right',h,w,result)
                zero_pos = move_zero_pos(zero_pos, (zero_dest//w-zero_pos//w),'up_down',h,w,result)
            else:
                zero_pos = move_zero_pos(zero_pos, (h-2-zero_pos//w),'up_down',h,w,result)
                zero_pos = move_zero_pos(zero_pos, (zero_dest%w-zero_pos%w),'left_right',h,w,result)
                zero_pos = move_zero_pos(zero_pos, (zero_dest//w-zero_pos//w),'up_down',h,w,result)

        else:
            if temp_pos % w != w-1:
                if zero_dest == temp_pos+1:
                    zero_pos = move_zero_pos(zero_pos, 1,'left_right',h,w,result)
                    zero_pos = move_zero_pos(zero_pos, (zero_dest//w-zero_pos//w),'up_down',h,w,result)
                else:
                    zero_pos = move_zero_pos(zero_pos, 1,'left_right',h,w,result)
                    if temp_pos // w != h-1:
                        zero_pos = move_zero_pos(zero_pos, (temp_pos // w+1-zero_pos//w),'up_down',h,w,result)
                        zero_pos = move_zero_pos(zero_pos, (zero_dest%w-zero_pos%w),'left_right',h,w,result)
                        zero_pos = move_zero_pos(zero_pos, (zero_dest//w-zero_pos//w),'up_down',h,w,result)
                    else:
                        zero_pos = move_zero_pos(zero_pos, (h-2-zero_pos//w),'up_down',h,w,result)
                        zero_pos = move_zero_pos(zero_pos, (zero_dest%w-zero_pos%w),'left_right',h,w,result)
                        zero_pos = move_zero_pos(zero_pos, (zero_dest//w-zero_pos//w),'up_down',h,w,result)
            else:
                zero_pos = move_zero_pos(zero_pos, -1,'left_right',h,w,result)
                zero_pos = move_zero_pos(zero_pos, (zero_dest//w-zero_pos//w),'up_down',h,w,result)

    else:  #左右位置已经对好，只需要上
        if temp_pos // w != h-1 and temp_pos % w != w-1:
            if zero_pos %w == zero_dest%w:
                zero_pos = move_zero_pos(zero_pos, 1,'left_right',h,w,result)
            zero_pos = move_zero_pos(zero_pos, (temp_pos // w+1-zero_pos//w),'up_down',h,w,result)
            zero_pos = move_zero_pos(zero_pos, (zero_dest%w + 1 -zero_pos%w),'left_right',h,w,result)

            zero_pos = move_zero_pos(zero_pos, (zero_dest//w -zero_pos//w),'up_down',h,w,result)
            zero_pos = move_zero_pos(zero_pos, -1,'left_right',h,w,result)
        elif temp_pos // w != h-1 and temp_pos % w == w-1:#不沉底贴右边
            zero_pos = move_zero_pos(zero_pos, (w-2 -zero_pos%w),'left_right',h,w,result)
            zero_pos = move_zero_pos(zero_pos, (zero_dest//w -zero_pos//w),'up_down',h,w,result)
            zero_pos = move_zero_pos(zero_pos, 1,'left_right',h,w,result)
        else:
            zero_pos = move_zero_pos(zero_pos, (h-2-zero_pos//w),'up_down',h,w,result)
            zero_pos = move_zero_pos(zero_pos, (zero_dest%w-zero_pos%w),'left_right',h,w,result)

    if zero_pos == zero_dest and result[-1][temp_pos] == temp_num:
        return zero_pos
    else:
        return -1




def rowarrange(goal, height ,width, rownum, result):
    destlist= []

    

    for i in range(width):
        destlist.append(goal[width*rownum + i])

    for i in range(width):
        state = copy.deepcopy(result[-1])
        if i < width-1:
            dest_height = rownum
        else:
            dest_height = rownum+1
        if i < width-2 or i == width-1:
            dest_width = i
        else:
            dest_width = width-1

        for j in range(height*width):
            if state[j] == destlist[i]:
                temp_pos = j
            elif state[j] == 0:
                zero_pos = j

        if temp_pos%width == dest_width and temp_pos //width == dest_height:
            if i == width-2:
                zero_pos = move_zero_pos(zero_pos, (width-2 -zero_pos%width),'left_right',height,width,result)
                zero_pos = move_zero_pos(zero_pos, (temp_pos // width-zero_pos//width),'up_down',height,width,result)
                if result[-1][zero_pos + width] == destlist[i+1]:
                    zero_pos = move_zero_pos(zero_pos, 1,'left_right',height,width,result)
                    zero_pos = move_zero_pos(zero_pos, 1,'up_down',height,width,result)
                    zero_pos = move_zero_pos(zero_pos, -1,'left_right',height,width,result)
                    zero_pos = move_zero_pos(zero_pos, 1,'up_down',height,width,result)
                    zero_pos = move_zero_pos(zero_pos, 1,'left_right',height,width,result)
                    zero_pos = move_zero_pos(zero_pos, -2,'up_down',height,width,result)
                    zero_pos = move_zero_pos(zero_pos,-1,'left_right',height,width,result)
                zero_pos = move_zero_pos(zero_pos, 1,'up_down',height,width,result)
            continue

        while temp_pos%width != dest_width:
            if temp_pos%width > dest_width:
                zero_dest = temp_pos - 1
                zero_pos = move_to_dest(temp_pos, zero_pos, zero_dest, height, width, result)
                if zero_pos == -1:
                    print("error!")
                zero_pos = move_zero_pos(zero_pos, 1, 'left_right', height, width, result)
                temp_pos = zero_dest
            
            else:
                zero_dest = temp_pos + 1
                zero_pos = move_to_dest(temp_pos, zero_pos, zero_dest, height, width, result)
                if zero_pos == -1:
                    print("error!")
                zero_pos = move_zero_pos(zero_pos, -1, 'left_right', height, width, result)
                temp_pos = zero_dest

        while temp_pos// width != dest_height:
            zero_dest = temp_pos - width
            zero_pos = move_to_dest(temp_pos, zero_pos, zero_dest, height, width, result)
            if zero_pos == -1:
                print("error!")
            zero_pos = move_zero_pos(zero_pos, 1, 'up_down', height, width, result)
            temp_pos = zero_dest

        if i == width-2:
            zero_pos = move_zero_pos(zero_pos, (width-2 -zero_pos%width),'left_right',height,width,result)
            zero_pos = move_zero_pos(zero_pos, (temp_pos // width-zero_pos//width),'up_down',height,width,result)
            if result[-1][zero_pos + width] == destlist[i+1]:
                zero_pos = move_zero_pos(zero_pos, 1,'left_right',height,width,result)
                zero_pos = move_zero_pos(zero_pos, 1,'up_down',height,width,result)
                zero_pos = move_zero_pos(zero_pos, -1,'left_right',height,width,result)
                zero_pos = move_zero_pos(zero_pos, 1,'up_down',height,width,result)
                zero_pos = move_zero_pos(zero_pos, 1,'left_right',height,width,result)
                zero_pos = move_zero_pos(zero_pos, -2,'up_down',height,width,result)
                zero_pos = move_zero_pos(zero_pos,-1,'left_right',height,width,result)
            zero_pos = move_zero_pos(zero_pos, 1,'up_down',height,width,result)


    zero_pos = move_zero_pos(zero_pos,(width-2 -zero_pos%width),'left_right',height,width,result)
    zero_pos = move_zero_pos(zero_pos,(rownum -zero_pos//width),'up_down',height,width,result)
    zero_pos = move_zero_pos(zero_pos,1,'left_right',height,width,result)
    zero_pos = move_zero_pos(zero_pos,1,'up_down',height,width,result)


def Astar_algo_DC(start, goal, height ,width):
    result = []
    result.append(start)
    for i in range(height - 2):
        rowarrange(goal, height, width, i, result)

    
    new_start = result[-1][width*(height - 2):height*width]
    new_goal = goal[width*(height - 2):height*width]
    print(new_start)
    print(new_goal)
    new_list = Astar_DC(new_start, new_goal, 2, width, 100)
    for i in range(len(new_list)):
        new_list[i] = result[-1][0:width*(height - 2)] + new_list[i]
    result.reverse()
    result.remove(result[0])
    
    final = new_list + result

    return final

# height = 4
# width = 5
# start = list(range(height*width))
# random.shuffle(start)
# print(start)
# goal = [i for i in range(1, height*width)]
# goal.append(0)
# result = []
# result.append(start)
# if is_trans_successful(start, goal, height, width) == False:
#     print("False to trans")
# else:
#     for i in range(height - 2):
#         rowarrange(goal, height, width, i, result)
#         print('rowok')

#     new_start = result[-1][width*(height - 2):height*width]
#     new_goal = goal[width*(height - 2):height*width]
#     print(new_start)
#     print(new_goal)
#     new_list = Astar_DC(new_start, new_goal, 2, width, 100)
#     for i in range(len(result)-1):
#         print(result[i])

#     for i in range(len(new_list)-1,-1,-1):
#         print(result[-1][0:width*(height - 2)] + new_list[i])

#     print("total_step: " + str(len(result)+len(new_list)-1))
