from functions import *

def prob_197_3():
  lines = open("data/dataset_197_3.txt").read().splitlines()
  k = int(lines[0])
  text = lines[1]

  fout = open("out/out_197_3.txt", "w")
  for i in composition_k(k,text):
    fout.write(i + '\n')
  fout.close()

if __name__ == "__main__":
  prob_197_3()