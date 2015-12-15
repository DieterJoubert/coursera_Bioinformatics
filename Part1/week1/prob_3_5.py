def prob_3_5():
  lines = open("data/dataset_3_5.txt").read().splitlines()

  pattern = lines[0]
  genome = lines[1]

  fout = open("out.txt", "w")
  fout.write(" ".join(map(str,pattern_matching(pattern, genome))))
  fout.close() 

def pattern_matching(pattern, genome):
  indices = []
  for i in range(len(genome)):
    if genome[i:i+len(pattern)] == pattern:
      indices.append(i)
  return indices

if __name__ == '__main__':
  prob_3_5()