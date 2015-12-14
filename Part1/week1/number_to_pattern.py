def number_to_pattern(number,k):      
  num_to_symbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
  if k == 1:
    return num_to_symbol[number]
  quotient = number / 4
  remainder = number % 4
  symbol = num_to_symbol[remainder]
  prefix_pattern = number_to_pattern(quotient,k-1)
  return prefix_pattern + symbol
