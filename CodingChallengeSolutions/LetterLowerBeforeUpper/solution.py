def solution(letters):
  first_lower = {}
  first_upper = {}
  last_lower = {}

  for i, ch in enumerate(letters):
    if ch.islower():
      if ch not in first_lower.keys():
        first_lower[ch] = i
      last_lower[ch] = i
    else:
      low = ch.lower()
      if low not in first_upper:
        first_upper[low] = i

  count = 0
  for ch in first_lower:
    if ch in first_upper:
      if last_lower[ch] < first_upper[ch]:
        count += 1
        
  return count