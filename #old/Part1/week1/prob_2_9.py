def prob_2_9():
  lines = open("dataset_2_9.txt").read().splitlines()

  Text = lines[0]
  k = int(lines[1])

  print(FrequentWords(Text,k))

def FrequentWords(Text, k):
  kmers_count = {}
  for i in range(0,len(Text)-k):
    kmer = Text[i:i+k]
    if kmer in kmers_count:
      kmers_count[kmer] += 1
    else:
      kmers_count[kmer] = 1

  max_value = 0
  for key, value in kmers_count.items():
    max_value = max(value, max_value)

  max_kmers = []
  for key, value in kmers_count.items():
    if value == max_value:
      max_kmers.append(key)

  return " ".join(max_kmers)

if __name__ == '__main__':
  prob_2_9()