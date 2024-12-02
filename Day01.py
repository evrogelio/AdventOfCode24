from typing import List
import csv



def main():
  left, right = parseAndSortCsv()
  difference = part1(left, right)
  print(f'The difference between left and right is: {difference}')

  similarity = part2(left, right)
  print(f'Similarity between left and right is: {similarity}')


# Calculate the difference between ith elements of left and right arrays
def part1(left: List[int], right: List[int]):
  sum = 0
  for i in range(len(left)):
    sum = sum + abs(left[i]-right[i])
  
  return sum

def part2(left: List[int], right: List[int]):
  ri = 0
  li = 0
  similarity = 0

  while(li<len(left) and ri < len(right)):
    if left[li] < right[ri]:
      li += 1
    else:
      if left[li] == right[ri]:
        similarity += left[li]
      ri += 1

  return similarity


def parseAndSortCsv():
  filename = "Day01-input.csv"

  left: List[int] = []
  right: List[int] = []
  
  with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      split = row[0].split("   ")
      left.append(int(split[0]))
      right.append(int(split[1]))

  left.sort()
  right.sort()

  return left, right

if __name__ == "__main__":
  main()