def prob_2_9():
  lines = open("dataset_2_9.txt").read().splitlines()

  text = lines[0]
  k = int(lines[1])

  fout = open("out.txt", "w")
  fout.write(" ".join(frequent_words(text,k)))
  fout.close() 

def frequent_words(text, k):
  frequent_patterns = []
  count = []
  for i in range(len(text)-k):
    pattern = text[i:i+k]
    count.append(pattern_count(text,pattern))
  max_count = max(count)
  for i in range(0,len(text)-k):
    if count[i] == max_count:
      frequent_patterns.append(text[i:i+k])
  frequent_patterns = list(set(frequent_patterns))
  return frequent_patterns

def pattern_count(text, pattern):
  count = 0
  for i in range(len(text)-len(pattern)):
    if text[i:i+len(pattern)] == pattern:
      count = count + 1
  return count  

if __name__ == '__main__':
  prob_2_9()