def prob_158_9():
  lines = open("dataset_158_9.txt").read().splitlines()
  k = int(lines[0])

  Dna = []
  for i in range(1,len(lines)):
    Dna.append(lines[i].strip())

  fout = open("out.txt", "w")
  fout.write(MedianString(Dna, k))
  fout.close()

def MedianString(Dna, k):
  distance = float("inf")
  perms = Perms(k)
  for kmer in perms:
    if distance > d(kmer, Dna):
      distance = d(kmer, Dna)
      median = kmer

  return median

def d(Pattern, Dna):
  d_total = 0
  for string in Dna:
    min_d = float("inf")
    for i in range(len(string)-len(Pattern)+1):
      min_d = min(min_d, HammingDistance(Pattern, string[i:i+len(Pattern)]))
      if min_d == 0:
        break
    d_total += min_d
  return d_total

def HammingDistance(string1, string2):
  hamm = 0
  for i in range(len(string1)):
    if string1[i] != string2[i]:
      hamm += 1
  return hamm

def Perms(length):
  DNA = ['A', 'C', 'G', 'T']
  perms = []
  from itertools import product
  for i in product(DNA, repeat=length):
    perms.append("".join(i))
  return perms

if __name__ == '__main__':
  prob_158_9()