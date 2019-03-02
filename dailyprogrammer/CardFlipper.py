def solution(prob):
    list_prob = list(prob)
    print(list_prob)
    if face_up_even(list_prob) == False:
        return "No solution possible"
    i = 0
    while i < len(list_prob):
        if list_prob[i] == "1":
            flip_adjacent(list_prob, i)
            list_prob[i] = "." 
            print list_prob, "(%d)"%i
            i = 0
        else:
            i += 1
    if list_prob == ["." for j in range(len(list_prob))]:
        return "Solution found!"
    else:
        return "No solution found"
          
flip_map = {"0": "1",
            "1": "0",
            ".": "."
            }
def face_up_even(list_prob):
    face_up_count = 0
    for i in list_prob:
        if i == "1":
            face_up_count += 1
    if face_up_count % 2 == 0:
        return True
    return False


def flip_adjacent(list_prob, ind):
    if ind - 1 >= 0:
        list_prob[ind - 1] = flip_map.get(list_prob[ind - 1])
    if ind + 1 < len(list_prob):
        list_prob[ind + 1] = flip_map.get(list_prob[ind + 1])
    return list_prob

print(solution("1111"))