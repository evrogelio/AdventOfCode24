from typing import List
import csv

def main():
  rows = parseCsv()

  # reportIsSafe(rows[23], "asc", True)
  part1(rows)
  part2(rows)

def part2(rows: List[List[int]]):
  safe, unsafe = checkSafeReports(rows, True)
  print(f"Safe reports with dampener: {safe}")
  print(f"Unsafe reports with dampener: {unsafe}")

def part1(rows: List[List[int]]):
  safe, unsafe = checkSafeReports(rows, False)
  print(f"Safe reports without dampener: {safe}")
  print(f"Unsafe reports without dampener: {unsafe}")


def checkSafeReports(rows: List[List[int]], enableDampener: bool):
  safe = 0
  unsafe = 0
  for row in rows:
    try:
      direction = getDirection(row) 
      reportIsSafe(row, direction, enableDampener)
      safe += 1
    except Exception as e:
      unsafe += 1
      pass
  
  return safe, unsafe

def parseCsv():
  filename = "Day02-input.csv"
  rows: List[List[int]] = []

  with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      intRow = row[0].split(' ')
      intRow = map(int, intRow)
      rows.append(list(intRow))

  return rows


def reportIsSafe(row: List[int], direction: str, allowError: bool):
  if row == None or len(row) == 0:
    raise Exception("Report is unsafe")
  
  safeRow = [row[0]]
  canDeleteRegister = allowError
  for i in range(1,len(row)):
    current = row[i]
    prev = safeRow[-1]
    if not areNeighborsSafe(prev, current, direction):
      if canDeleteRegister:
        canDeleteRegister = False
        next = row[i+1] if i+1 < len(row) else None
        prevprev = row[i-2] if i-2 >= 0 else None
        if areNeighborsSafe(prev, next, direction):
          pass
        elif areNeighborsSafe(prevprev, current, direction):
          safeRow.pop()
          safeRow.append(current)
          pass
        else:
          print(row)
          raise Exception("Report is not safe")
      else: 
        print(row)
        raise Exception("Report is not safe")
    else:
      safeRow.append(current)

def getDirection(row: List[int]):
  if row == None or len(row) < 2:
    return "asc"
  sum = 0
  for i in range(1,len(row)):
    if row[i] - row[i-1] > 0:
      sum += 1
    elif row[i] - row[i-1] < 0:
      sum -= 1
    else:
      pass

  return "asc" if sum > 0 else "desc"

def areNeighborsSafe(left: int, right: int, direction: str):
  if right == None or left == None:
    return True
  if direction == "desc":
    return left - right in [1,2,3]
  else:
    return left - right in [-1,-2,-3]
  

if __name__ == "__main__":
  main()