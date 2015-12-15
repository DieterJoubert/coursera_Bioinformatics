from pattern_to_number import *

def prob_3010_2():
  lines = open("data/dataset_3010_2.txt").read().splitlines()
  pattern = lines[0]

  fout = open("out.txt", "w")
  fout.write(str(pattern_to_number(pattern)))
  fout.close() 

if __name__ == '__main__':
  prob_3010_2()