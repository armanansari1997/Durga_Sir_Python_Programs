players = ['Sachin', 'Sehwag', 'Gambhir', 'Raina']
scores = [100, 80, 50, 40]
for pl,sc in zip(players, scores):
    print('player : %s    Score : %d' % (pl, sc))
    