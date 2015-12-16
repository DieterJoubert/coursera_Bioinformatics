from functions import *

def prob_159_3():
  lines = open("data/dataset_159_3.txt").read().splitlines()
  text = lines[0]
  k = int(lines[1])
  profile = []
  for i in range(2,6):
    profile.append(map(float,lines[i].split()))
  print profile

  fout = open("out/out_159_3.txt", "w")
  fout.write(profile_most_probable_kmer(text,k,profile))
  fout.close()  

if __name__ == "__main__":
  prob_159_3()