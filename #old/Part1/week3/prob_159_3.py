def prob_159_3():
  lines = open("dataset_159_3.txt").read().splitlines()
  string = lines[0]
  k = int(lines[1])

  profile = {}
  profile['A'] = map(float, lines[2].split())
  profile['C'] = map(float, lines[3].split())
  profile['G'] = map(float, lines[4].split())
  profile['T'] = map(float, lines[5].split())      

  fout = open("out.txt", "w")
  fout.write(" ".join(ProfileMostProbableKmer(string, k, profile)))
  fout.close()

def ProfileMostProbableKmer(text, k, profile):
  best_kmer = None
  best_prob = float(0)

  for i in range(len(text)-k+1):
    kmer = text[i:i+k]
    kmer_prob = float(1)
    for i_kmer in range(len(kmer)):
      kmer_prob = kmer_prob * profile[kmer[i_kmer]][i_kmer]
    if kmer_prob > best_prob:
      best_prob = kmer_prob
      best_kmer = kmer

  return best_kmer

if __name__ == '__main__':
  prob_159_3()