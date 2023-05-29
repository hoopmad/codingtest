players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

def solution(players, callings):
    answer = []
    player_dict = {player : index for index, player in enumerate(players)}
    print(player_dict)
    
    for i in range(len(callings)):
        c_idx = players.index(callings[i])

        players[c_idx-1], players[c_idx] = players[c_idx], players[c_idx-1]
    
            
    
    print(players)
    return answer

solution(players, callings)