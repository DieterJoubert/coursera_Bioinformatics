def prob_2_6():
  lines = open("dataset_2_6.txt").read().splitlines()

  Text = lines[0]
  Pattern = lines[1]

  print(PatternCount(Text,Pattern))

def PatternCount(Text, Pattern):
  count = 0
  for i in range(0,len(Text)):
    if Text[i:i+len(Pattern)] == Pattern:
      count += 1
  return count

if __name__ == '__main__':
  prob_2_6()