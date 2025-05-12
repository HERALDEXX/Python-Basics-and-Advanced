senior_scores = [10, 20, 30, 40, 50]
junior_scores = [5, 10, 15, 20, 25]

score = 50
category = 'senior'

senior_high = max(senior_scores)
junior_high = max(junior_scores)

if (score == senior_high) and (category == 'senior'):
    print('You are the winner for the senior category!')

elif (score == junior_high) and (category == 'junior'):
    print('You are the winner for the junior category!')
else:
    print('You did not win the competition.')    