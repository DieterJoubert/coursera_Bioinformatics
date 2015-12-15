from hamming_distance import *
from approximate_pattern_count import *

def prob_9_6():
  lines = open("data/dataset_9_6.txt").read().splitlines()
  pattern = lines[0]
  text = lines[1]
  d = int(lines[2])

  fout = open("out.txt", "w")
  fout.write(str(approximate_pattern_count(text, pattern, d)))
  fout.close()  

if __name__ == "__main__":
  prob_9_6()