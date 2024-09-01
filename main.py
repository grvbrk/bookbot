from collections import Counter

def charFrequency(text: str) -> dict:
  freq = Counter(text.lower())
  return {x: y for x,y in freq.items() if x.isalpha()}

def generateReport(freq: dict) -> None:
  sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
  print("BEGIN REPORT")
  for x, y in sorted_dict.items():
    print(f"The '{x}' character was found {y} times")
  print("END REPORT")

def main() -> None:
  with open("books/frankenstein.txt") as f:
    contents = f.read()
    alphabet_freq = charFrequency(contents)
    generateReport(alphabet_freq)


main()

