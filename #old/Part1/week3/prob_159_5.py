def prob_159_5():
  lines = open("dataset_159_5.txt").read().splitlines()
  kt = lines[0].split()
  k = int(kt[0])
  t = int(kt[1])

  Dna = []
  for i in range(1,len(lines)):
    Dna.append(lines[i])

  motifs = GreedyMotifSearch(k, t, Dna)
  fout = open("out.txt", "w")
  for mot in motifs:
    fout.write(mot + "\n")
  fout.close()

def GreedyMotifSearch(k, t, Dna):
  best_motifs = []
  for string in Dna:
    best_motifs.append(string[0:0+k])

  for i in range(len(Dna[0])-k+1):
    kmer = Dna[0][i:i+k]
    motifs = [kmer]
    for index in range(1,len(Dna)):
      profile = Profile(motifs)
      motifs.append( ProfileMostProbableKmer(Dna[index], k, profile) )
    if Score(motifs) < Score(best_motifs):
      best_motifs = motifs

  return best_motifs

def Score(motifs):
  print motifs
  score = 0
  for i in range(len(motifs[0])):
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for mot in motifs:
      count[mot[i]] += 1
    (best_found, best_count) = (None, 0)
    for key, value in count.items():
      if value > best_count:
        (best_found, best_count) = (key, value)
    for key, value in count.items():
      if key != best_found:
        score += value

  return score

def Profile(motif_list):
  motif_count = len(motif_list)

  consensus = { 'A': [float(0.0) for x in range(len(motif_list[0]))], 
                'C': [float(0.0) for x in range(len(motif_list[0]))],
                'G': [float(0.0) for x in range(len(motif_list[0]))], 
                'T': [float(0.0) for x in range(len(motif_list[0]))] }

  for motif in motif_list:
    for i in range(len(motif)):
      consensus[motif[i]][i] += 1

  import copy
  profile = copy.deepcopy(consensus)

  for key, value in consensus.items():
    for i in range(len(value)):
      profile[key][i] = consensus[key][i] / motif_count

  return profile

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

  if best_kmer == None:
    return text[0:0+k]
  return best_kmer

if __name__ == '__main__':
  prob_159_5()