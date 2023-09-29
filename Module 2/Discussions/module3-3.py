def get_score():
  score = -1
  
  try:
    print('Enter score: ')
    score = input()
    if score == '':
      is_stop = input('Stop? (y/n): ')
      is_stop = is_stop.lower()
      if is_stop == 'y':
        return
    score = int(score)
    if score < 0 or score > 100:
      raise ValueError
  except ValueError:
    print('Invalid score entered')
    score = 0
  return score

def get_average(scores):
  if len(scores) == 0:
    return 0
  return sum(scores) / len(scores)

def get_scores():
  scores = []
  while True:
    score = get_score()
    if score is None:
      break
    scores.append(score)
  return scores

average_score = get_average(get_scores())
print(f'Average score: {average_score}')