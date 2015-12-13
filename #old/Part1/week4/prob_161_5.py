def prob_161_5():
  lines = open("dataset_161_5.txt").read().splitlines()
  kt = lines[0].split()
  k = int(kt[0])
  t = int(kt[1])

  Dna = []
  for i in range(1,len(lines)):
    Dna.append(lines[i])

  fout = open("out.txt", "w")
  for mot in RandomizedIteration(Dna, k, t):
    fout.write(mot + "\n")
  fout.close()

def RandomizedIteration(Dna, k, t):
  best_motifs = RandomizedMotifSearch(Dna, k, t)

  for i in range(10000):
    motifs_new = RandomizedMotifSearch(Dna, k, t)
    if Score(motifs_new) > Score(best_motifs):
      best_motifs = motifs_new

  """
  best = Score(motifs[0])
  best_mot = motifs[0]

  for mot in motifs:
    if Score(mot) > best:
      best = Score(mot)
      best_mot = mot
  """

  return best_motifs

def RandomizedMotifSearch(Dna, k, t):
  import random
  motifs = []

  for string in Dna:
    x = random.randint(0,len(string)-k)
    kmer = string[x:x+k]
    motifs.append(kmer)

  best_motifs = motifs

  while True:
    profile = Profile(motifs)
    motifs = MotifsFromProfile(profile, Dna, k)

    if Score(motifs) < Score(best_motifs):
      best_motifs = motifs
    else:
      return best_motifs

def MotifsFromProfile(profile, dna, k):
  return [ProfileMostProbableKmer(seq,k,profile) for seq in dna]

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


def Score(motifs):
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

  consensus = { 'A': [float(1.0) for x in range(len(motif_list[0]))], 
                'C': [float(1.0) for x in range(len(motif_list[0]))],
                'G': [float(1.0) for x in range(len(motif_list[0]))], 
                'T': [float(1.0) for x in range(len(motif_list[0]))] }

  for motif in motif_list:
    for i in range(len(motif)):
      consensus[motif[i]][i] += 1

  import copy
  profile = copy.deepcopy(consensus)

  for key, value in consensus.items():
    for i in range(len(value)):
      profile[key][i] = consensus[key][i] / motif_count

  return profile

if __name__ == '__main__':
  prob_161_5()