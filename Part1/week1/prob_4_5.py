def prob_4_5():
  """find all k-mers forming (L, t) clumps in genome"""  
  lines = open("data/dataset_4_5.txt").read().splitlines()

  genome = lines[0]

  klt = lines[1].split()
  k = int(klt[0])
  L = int(klt[1])
  t = int(klt[2])

  import better_clump_finding as bcf

  fout = open("out.txt", "w")
  fout.write(" ".join(bcf.better_clump_finding(genome, k, t, L)))
  fout.close() 

if __name__ == '__main__':
  prob_4_5()