def solution(genres, plays):
    answer = []
    playsDict = {}
    d = { }
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        playsDict[genre] = playsDict.get(genre, 0) + play
        d[genre] = d.get(genre, []) + [ (play, i) ]

    genreSort = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)
    
    for (genre, totalPlay) in genreSort:
        d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))
        answer += [ idx for (play, idx) in d[genre][:2] ]
    
    return answer
