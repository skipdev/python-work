print("Where do you want to look?")
place = str(input())
if place == "in my bedroom":
  print("Where in your bedroom do you want to look?")
  bedroom_answer = str(input())
  if bedroom_answer == "under the bed":
    print("Found your shoes but not your wallet.")
  else:
    print("It's a mess but found no wallet.")
elif place == "in the bathroom":
  print("Where in your bathroom?")
  bathroom_answer = str(input())
