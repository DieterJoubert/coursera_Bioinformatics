def prob_9_6():
  lines = open("dataset_9_6.txt").read().splitlines()

  text = lines[0]
  pattern = lines[1]
  d = int(lines[2])

  print(ApproximatePatternCount(text, pattern, d))

def ApproximatePatternCount(text, pattern, d):
  count = 0
  for i in range(len(text)-len(pattern)+1):
    if HammingDistance(pattern,text[i:i+len(pattern)]) <= d:
      count += 1
  return count

def HammingDistance(string1, string2):
  hamm = 0
  for i in range(len(string1)):
    if string1[i] != string2[i]:
      hamm += 1
  return hamm

if __name__ == '__main__':
  prob_9_6()