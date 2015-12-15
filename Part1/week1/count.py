def count(text, pattern):
  count = 0
  for i in range(len(text)-len(pattern)):
    if text[i:i+len(pattern)] == pattern:
      count = count + 1
  return count  