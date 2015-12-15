def prob_9_3():
  lines = open("data/dataset_9_3.txt").read().splitlines()
  str_1 = lines[0]
  str_2 = lines[1]

  from hamming_distance import *
  print(str(hamming_distance(str_1, str_2)))

if __name__ == "__main__":
  prob_9_3()