from itertools import permutations

def check(user, banned_id) :
    for i in range (len(banned_id)) :
        if len(user[i]) != len(banned_id[i]):
            return False

        for j in range(len(user[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != user[i][j]:
                return False # 현재 튜플 불일치
    return True

def solution(user_id, banned_id):
    answer = 0
    
    user_set = list(permutations(user_id, len(banned_id)))
    banned = []
    
    for user in user_set :
        if not check(user, banned_id) :
            continue
        else :
            user = set(user)
            if user not in banned :
                banned.append(user)
    
    return len(banned)