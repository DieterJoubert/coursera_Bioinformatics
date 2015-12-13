from computing_frequencies import *

def prob_2994_5():
  lines = open("dataset_2994_5.txt").read().splitlines()

  text = lines[0]
  k = int(lines[1])

  fout = open("out.txt", "w")
  fout.write(" ".join(map(str,computing_frequencies(text,k))))
  fout.close() 

if __name__ == '__main__':
  prob_2994_5()