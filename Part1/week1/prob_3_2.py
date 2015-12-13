def prob_3_2():
  lines = open("dataset_3_2.txt").read().splitlines()

  dna_input = lines[0]

  fout = open("out.txt", "w")
  fout.write(reverse_complement_dna(dna_input))
  fout.close() 

def reverse_complement_dna(pattern):
  complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
  reverse_complement = ""
  for i in range(len(pattern)):
    reverse_complement += complement_dict[pattern[len(pattern)-1-i]]
  return reverse_complement

if __name__ == '__main__':
  prob_3_2()