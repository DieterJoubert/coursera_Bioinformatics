def Vibrio_cholerae():
  lines = open("data/Vibrio_cholerae.txt").read().splitlines()

  pattern = "CTTGATCAT"
  genome = lines[0]

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
  Vibrio_cholerae()