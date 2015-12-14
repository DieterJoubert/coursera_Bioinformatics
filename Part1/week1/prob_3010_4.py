from number_to_pattern import *

def prob_3010_4():
  lines = open("dataset_3010_4.txt").read().splitlines()
  number = int(lines[0])
  k = int(lines[1])

  fout = open("out.txt", "w")
  fout.write(str(number_to_pattern(number,k)))
  fout.close() 

if __name__ == '__main__':
  prob_3010_4()