import frequent_words_with_mismatches as fwwm

def prob_9_7():
  lines = open("data/dataset_9_7.txt").read().splitlines()
  text = lines[0]
  k = int(lines[1].split()[0])
  d = int(lines[1].split()[1])

  fout = open("out.txt", "w")
  fout.write(" ".join(fwwm.frequent_words_with_mismatches(text,k,d)))
  fout.close()  

if __name__ == "__main__":
  prob_9_7()