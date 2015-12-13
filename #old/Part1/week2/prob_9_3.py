def prob_9_3():
  lines = open("dataset_9_3.txt").read().splitlines()

  string1 = lines[0]
  string2 = lines[1]

  print(HammingDistance(string1, string2))

def HammingDistance(string1, string2):
  hamm = 0
  for i in range(len(string1)):
    if string1[i] != string2[i]:
      hamm += 1
  return hamm

if __name__ == '__main__':
  prob_9_3()