from hamming_distance import *

def prob_9_4():
  lines = open("dataset_9_4.txt").read().splitlines()
  pattern = lines[0]
  text = lines[1]
  d = int(lines[2])

  fout = open("out.txt", "w")
  fout.write(" ".join(map(str,approx_pattern_match_indices(pattern,text,d))))
  fout.close()

def approx_pattern_match_indices(pattern, text, d):
  indices = []
  for i in range(len(text)-len(pattern)+1):
    window = text[i:i+len(pattern)]
    if hamming_distance(pattern, window) <= d:
      indices.append(i)
  return indices

if __name__ == "__main__":
  prob_9_4()