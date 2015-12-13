import computing_frequencies as cf

def faster_frequent_words(text, k):
  frequent_patterns = []
  frequency_array = cf.computing_frequencies(text,k)
  max_count = max(frequency_array)
  for i in range(0,4**k):
    if frequency_array[i] == max_count:
      pattern = cf.number_to_pattern(i,k)
      if pattern not in frequent_patterns:
        frequent_patterns.append(pattern)
  return frequent_patterns