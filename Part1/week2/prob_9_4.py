from hamming_distance import *
from approx_pattern_match_indices import *

def prob_9_4():
  lines = open("data/dataset_9_4.txt").read().splitlines()
  pattern = lines[0]
  text = lines[1]
  d = int(lines[2])

  fout = open("out.txt", "w")
  fout.write(" ".join(map(str,approx_pattern_match_indices(pattern,text,d))))
  fout.close()

if __name__ == "__main__":
  prob_9_4()