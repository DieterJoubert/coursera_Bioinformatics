from functions import *

def prob_198_3():
  lines = open("data/dataset_198_3.txt").read().splitlines()
  genome_path = []
  for line in lines[0:]:
    if line == "":
      break
    genome_path.append(line.strip())

  fout = open("out/out_198_3.txt", "w")
  fout.write(construct_string_from_path(genome_path))
  fout.close()  

def construct_string_from_path(genome_path):
  string = genome_path[0]
  for next in genome_path[1:]:
    string += next[-1]
  return string

if __name__ == "__main__":
  prob_198_3()