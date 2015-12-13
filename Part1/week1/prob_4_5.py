def prob_4_5():
  """find all k-mers forming (L, t) clumps in genome"""  
  lines = open("dataset_4_5.txt").read().splitlines()

  genome = lines[0]

  klt = lines[1].split()
  k = int(klt[0])
  L = int(klt[1])
  t = int(klt[2])

  fout = open("out.txt", "w")
  fout.write( " ".join(find_clump(genome, k, L, t)) )
  fout.close() 

if __name__ == '__main__':
  prob_4_5()