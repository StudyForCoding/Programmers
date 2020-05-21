def solution(genres, plays):
    answer = []
    
    genre = dict()
    for g in genres:
        genre[g] = 0
        
    PlayLength = len(plays)
    play = [0 for _ in range(PlayLength)]
    i = 0
    for p, g in zip(plays,genres) :
        play[i] = {g:p}
        i += 1
    
    
    for p in play:
        genre[list(p.keys())[0]] += list(p.values())[0]
    
    genre = sorted(genre.items(), key=lambda t: t[1], reverse=True)

    for g in genre:
        result_dict = dict()
        i = 0
        for p in play:
            key = list(p.keys())[0]
            if g[0] == key:
                value = list(p.values())[0]
                result_dict[i] = value
            i += 1
        
        result_dict = sorted(result_dict.items(), key=lambda kv: (-kv[1], kv[0]))
        count = 0
        for result in result_dict:
            answer.append(result[0])
            count += 1
            if count == 2:
                break
        
    return answer