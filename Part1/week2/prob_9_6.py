from hamming_distance import *

def prob_9_6():
  lines = open("dataset_9_6.txt").read().splitlines()
  pattern = lines[0]
  text = lines[1]
  d = int(lines[2])

  fout = open("out.txt", "w")
  fout.write(str(approximate_pattern_count(text, pattern, d)))
  fout.close()  

def approximate_pattern_count(text, pattern, d):
  count = 0
  for i in range(len(text)-len(pattern)+1):
    window = text[i:i+len(pattern)]
    if hamming_distance(pattern, window) <= d:
      count += 1
  return count

if __name__ == "__main__":
  prob_9_6()