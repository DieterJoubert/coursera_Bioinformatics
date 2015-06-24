def prob_3_2():
  lines = open("dataset_3_2.txt").read().splitlines()

  fout = open("out.txt", "w")
  fout.write(ReverseCompliment(lines[0]))
  fout.close()

def ReverseCompliment(string_in):
  string_out = ""
  compliment = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
  }
  length = len(string_in)
  for i in range(length):
    string_out += compliment[string_in[length-i-1]]
  return string_out

if __name__ == '__main__':
  prob_3_2()