def prob_3_5():
  lines = open("dataset_3_5.txt").read().splitlines()

  fout = open("out.txt", "w")
  fout.write(SubstringIndices(lines[0],lines[1]))
  fout.close() 

def SubstringIndices(Pattern, Genome):
  indices = []
  for i in range(len(Genome)-len(Pattern)):
    if Genome[i:i+len(Pattern)] == Pattern:
      indices.append(i)
  return " ".join( map(str, indices))

if __name__ == '__main__':
  prob_3_5()