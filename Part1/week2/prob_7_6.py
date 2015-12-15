from find_skew_diagram import *

def prob_7_6():
  lines = open("data/dataset_7_6.txt").read().splitlines()
  genome = lines[0]

  fout = open("out.txt", "w")
  fout.write(" ".join(map(str, min_skew_indices(genome))))
  fout.close() 

def min_skew_indices(text):
  skew_diagram = find_skew_diagram(text)
  min_skew = min(skew_diagram)

  min_indices = []

  for i in range(len(skew_diagram)):
    if skew_diagram[i] == min_skew:
      min_indices.append(i)

  return min_indices

if __name__ == '__main__':
  prob_7_6()