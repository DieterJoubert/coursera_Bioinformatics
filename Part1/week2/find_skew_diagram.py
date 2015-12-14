def find_skew_diagram(text):
  skew = 0
  diagram = []

  for i in range(len(text)):
    diagram.append(skew)
    if text[i] == "C":
      skew -= 1
    elif text[i] == "G":
      skew += 1

  diagram.append(skew)

  return diagram