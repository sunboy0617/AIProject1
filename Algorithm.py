import copy
import random
import time
class Node():
    def __init__(self, state, father, zero_pos, depth):

        self.state = state
        self.father = father
        self.zero_pos = zero_pos
        self.depth = depth
        self.score = 0

    def update_score(self, new_score):
        self.score = new_score



def calc_manhattan_dist(temp_state, goal, height, width):
    dist = 0
    for i in range(height * width):
        if temp_state[i] == 0:
            continue
        for j in range(height * width):
            if temp_state[i] == goal[j]:
                dist = dist + abs(i%width-j%width) + abs(i//width-j//width)
    return dist

def calc_unpos(temp_state, goal, height, width):
    count = 0
    for i in range(height * width):
        if temp_state[i] == 0:
            continue
        if temp_state[i] != goal[i]:
            count = count + 1
    return count

def develop_children(temp_node, height, width):
    output = []
    zero_pos_list = []
    state = copy.deepcopy(temp_node.state)
    zero_pos = temp_node.zero_pos

    if zero_pos// width > 0: #up
        state[zero_pos], state[zero_pos-width] = state[zero_pos-width], state[zero_pos]
        output.append(state)
        zero_pos_list.append(zero_pos-width)
        state = copy.deepcopy(temp_node.state)
    if zero_pos// width < height - 1: #down
        state[zero_pos], state[zero_pos+width] = state[zero_pos+width], state[zero_pos]
        output.append(state)
        zero_pos_list.append(zero_pos+width)
        state = copy.deepcopy(temp_node.state)
    if zero_pos % width > 0: #left
        state[zero_pos], state[zero_pos-1] = state[zero_pos-1], state[zero_pos]
        output.append(state)
        zero_pos_list.append(zero_pos-1)
        state = copy.deepcopy(temp_node.state)
    if zero_pos % width < width - 1: #right
        state[zero_pos], state[zero_pos+1] = state[zero_pos+1], state[zero_pos]
        output.append(state)
        zero_pos_list.append(zero_pos+1)
    
    return output, zero_pos_list

def is_trans_successful(temp, goal, height, width):
    lst = copy.deepcopy(temp)
    goal_lst = copy.deepcopy(goal)
    for i in range(height*width):
        if (i//width) % 2 == 1:
            lst[i] = temp[((i//width)+1)*width - (i-(i//width)*width) - 1]
            goal_lst[i] = goal[((i//width)+1)*width - (i-(i//width)*width) - 1]

    
    def inverse_num(list):
        num = 0
        for i in range(len(list)):
            for j in range(i):
                if list[j] > list[i] and list[i] != 0 and list[j] != 0:
                    num += 1
        return num

    if inverse_num(lst)%2 == inverse_num(goal_lst)%2:
        return True
    else:
        return False

def is_node_exist(child,lst):
    for i in range(len(lst)):
        if(lst[i].state==child):
            return i
    return -1



def return_father(node):
    fatherlist = []
    while True:
        if node.father == None:
            fatherlist.append(node.state)
            return fatherlist
            break
        else:
            fatherlist.append(node.state)
            node = node.father

def Astar(start, goal, height ,width, k):
    
    maxdepth = 0
    for i in range(len(start)):
        if start[i] == 0:
            zero_pos = i
            break

    root = Node(start, None, zero_pos, 0)
    root.update_score(k*calc_manhattan_dist(start, goal, height, width))

    openlist = [root]
    closelist = []
    count = 1

    while len(openlist)!=0:
        temp_node = openlist[0]
        openlist.remove(temp_node)

        if temp_node.state == goal:
            print("success")
            return (return_father(temp_node))
            
            break

        children, c_zeropos = develop_children(temp_node,height,width)
        if(len(children)==0): 
            continue

        for i in range(len(children)):
            if is_node_exist(children[i],openlist)==-1 and is_node_exist(children[i],closelist)==-1:
                score = k*calc_manhattan_dist(children[i], goal, height, width) + temp_node.depth + 1
                new_node = Node(children[i], temp_node, c_zeropos[i], temp_node.depth + 1)
                if(temp_node.depth + 1 >maxdepth):
                    maxdepth = temp_node.depth + 1
                new_node.update_score(score)
                count = count + 1
                openlist.append(new_node)

            elif is_node_exist(children[i],closelist)==-1:
                idx = is_node_exist(children[i],openlist)
                temp_score = k*calc_manhattan_dist(children[i], goal, height, width) + temp_node.depth + 1
                if temp_score < openlist[idx].score:
                    count = count + 1
                    openlist[idx].update_score(temp_score)
                    openlist[idx].father = temp_node
                    openlist[idx].depth = temp_node.depth + 1

            else:
                idx = is_node_exist(children[i],closelist)
                temp_score = k*calc_manhattan_dist(children[i], goal, height, width) + temp_node.depth + 1
                if temp_score < closelist[idx].score:
                    count = count + 1
                    this_node = closelist[idx]
                    closelist.remove(this_node)
                    this_node.depth = temp_node.depth + 1
                    this_node.father = temp_node
                    this_node.update_score(temp_score)
                    openlist.append(this_node)
                    if(temp_node.depth + 1 >maxdepth):
                        maxdepth = temp_node.depth + 1

        closelist.append(temp_node)
        openlist.sort(key=lambda x:x.score,reverse=False)


def Astar_DC(start, goal, height ,width, k):
    
    maxdepth = 0
    for i in range(len(start)):
        if start[i] == 0:
            zero_pos = i
            break

    root = Node(start, None, zero_pos, 0)
    root.update_score(k*calc_manhattan_dist(start, goal, height, width))

    openlist = [root]
    closelist = []
    count = 1

    while len(openlist)!=0:
        temp_node = openlist[0]
        openlist.remove(temp_node)

        if temp_node.state == goal:
            print("success")
            return (return_father(temp_node))
            
            break

        children, c_zeropos = develop_children(temp_node,height,width)
        if(len(children)==0): 
            continue

        for i in range(len(children)):
            if is_node_exist(children[i],openlist)==-1 and is_node_exist(children[i],closelist)==-1:
                score = k*calc_manhattan_dist(children[i], goal, height, width)
                new_node = Node(children[i], temp_node, c_zeropos[i], temp_node.depth + 1)
                if(temp_node.depth + 1 >maxdepth):
                    maxdepth = temp_node.depth + 1
                new_node.update_score(score)
                count = count + 1
                openlist.append(new_node)

            elif is_node_exist(children[i],closelist)==-1:
                idx = is_node_exist(children[i],openlist)
                temp_score = k*calc_manhattan_dist(children[i], goal, height, width)
                if temp_score < openlist[idx].score:
                    count = count + 1
                    openlist[idx].update_score(temp_score)
                    openlist[idx].father = temp_node
                    openlist[idx].depth = temp_node.depth + 1

            else:
                idx = is_node_exist(children[i],closelist)
                temp_score = k*calc_manhattan_dist(children[i], goal, height, width)
                if temp_score < closelist[idx].score:
                    count = count + 1
                    this_node = closelist[idx]
                    closelist.remove(this_node)
                    this_node.depth = temp_node.depth + 1
                    this_node.father = temp_node
                    this_node.update_score(temp_score)
                    openlist.append(this_node)
                    if(temp_node.depth + 1 >maxdepth):
                        maxdepth = temp_node.depth + 1

            maxidx = 0
            maxf = openlist[0].score
            for ii in range(len(openlist)):
                if openlist[ii].score > maxf:
                    maxf = openlist[ii].score
                    maxidx = ii
            if len(openlist) > 25:
                openlist.remove(openlist[maxidx])


        minidx = 0
        minf = openlist[0].score
        for i in range(len(openlist)):
            if openlist[i].score < minf:
                minf = openlist[i].score
                minidx = i
        closelist.append(temp_node)
        openlist[0],openlist[minidx] = openlist[minidx], openlist[0]


def Faster_Astar(start, goal, height ,width, k):
    
    maxdepth = 0
    for i in range(len(start)):
        if start[i] == 0:
            zero_pos = i
            break

    root = Node(start, None, zero_pos, 0)
    root.update_score(k*calc_manhattan_dist(start, goal, height, width))

    openlist = [root]
    closelist = []
    count = 1

    while len(openlist)!=0:
        temp_node = openlist[0]
        openlist.remove(temp_node)

        if temp_node.state == goal:
            print("success")
            return (return_father(temp_node))
            
            break

        children, c_zeropos = develop_children(temp_node,height,width)
        if(len(children)==0): 
            continue

        

            
        for i in range(len(children)):
            if is_node_exist(children[i],openlist)==-1 and is_node_exist(children[i],closelist)==-1:
                score = k*calc_manhattan_dist(children[i], goal, height, width) + temp_node.depth + 1
                new_node = Node(children[i], temp_node, c_zeropos[i], temp_node.depth + 1)
                if(temp_node.depth + 1 >maxdepth):
                    maxdepth = temp_node.depth + 1
                new_node.update_score(score)
                count = count + 1
                openlist.append(new_node)

            elif is_node_exist(children[i],closelist)==-1:
                idx = is_node_exist(children[i],openlist)
                temp_score = k*calc_manhattan_dist(children[i], goal, height, width) + temp_node.depth + 1
                if temp_score < openlist[idx].score:
                    count = count + 1
                    openlist[idx].update_score(temp_score)
                    openlist[idx].father = temp_node
                    openlist[idx].depth = temp_node.depth + 1

            else:
                idx = is_node_exist(children[i],closelist)
                temp_score = k*calc_manhattan_dist(children[i], goal, height, width) + temp_node.depth + 1
                if temp_score < closelist[idx].score:
                    count = count + 1
                    this_node = closelist[idx]
                    closelist.remove(this_node)
                    this_node.depth = temp_node.depth + 1
                    this_node.father = temp_node
                    this_node.update_score(temp_score)
                    openlist.append(this_node)
                    if(temp_node.depth + 1 >maxdepth):
                        maxdepth = temp_node.depth + 1

            maxidx = 0
            maxf = openlist[0].score
            for ii in range(len(openlist)):
                if openlist[ii].score > maxf:
                    maxf = openlist[ii].score
                    maxidx = ii
            if len(openlist) > 25:
                openlist.remove(openlist[maxidx])


        minidx = 0
        minf = openlist[0].score
        for i in range(len(openlist)):
            if openlist[i].score < minf:
                minf = openlist[i].score
                minidx = i
        closelist.append(temp_node)
        openlist[0],openlist[minidx] = openlist[minidx], openlist[0]


    
    
