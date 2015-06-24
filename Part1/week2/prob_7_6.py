def prob_7_6():
  lines = open("dataset_7_6.txt").read().splitlines()

  Genome = lines[0]

  fout = open("out.txt", "w")
  fout.write(" ".join(map(str,MinSkewIndex(Genome))))
  fout.close() 

def MinSkewIndex(Genome):
  skew_table = []
  curr_skew = 0
  skew_table.append(curr_skew)
  for char in Genome:
    if char == 'G':
      curr_skew += 1
    elif char == 'C':
      curr_skew -= 1
    skew_table.append(curr_skew)

  min_skew = 0
  min_indices = []

  for skew in skew_table:
    min_skew = min(min_skew, skew)

  for i in range(len(skew_table)):
    if skew_table[i] == min_skew:
      min_indices.append(i)

  return min_indices

if __name__ == '__main__':
  prob_7_6()