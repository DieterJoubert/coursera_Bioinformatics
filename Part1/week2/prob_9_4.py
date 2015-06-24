def prob_9_4():
  lines = open("dataset_9_4.txt").read().splitlines()

  pattern = lines[0]
  Genome = lines[1]
  d = int(lines[2])

  fout = open("out.txt", "w")
  fout.write(" ".join(map(str,ApproximatePattern(pattern, Genome, d))))
  fout.close() 

def ApproximatePattern(pattern, text, d):
  indices = []
  for i in range(len(text)-len(pattern)+1):
    if HammingDistance(pattern, text[i:i+len(pattern)]) <= d:
      indices.append(i)
  return indices

def HammingDistance(string1, string2):
  hamm = 0
  for i in range(len(string1)):
    if string1[i] != string2[i]:
      hamm += 1
  return hamm

if __name__ == '__main__':
  prob_9_4()