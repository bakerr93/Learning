import random

def Get_ToF_statements():
  statements = []
  statements.append(["The tallest mountain is Everest", "true", "True"])
  statements.append(["The largest forest is the Amazon", "true", "True"])
  statements.append(["USA is the most populous country", "false", "False"])
  statements.append(["Brown eyes are a dominant gene", "true", "True"])
  statements.append(["Cheese is made of trees", "false", "False"])

  return statements


print("type 'stop' to end the game")

def Ask_questions():
  stop = False
  ToF_statements = Get_ToF_statements()
  random.shuffle(ToF_statements)
  score = 0
  while stop is False:
    for s in ToF_statements:
      print(s[0] + ": True or false?")
      user_answer = input(">")
      if user_answer == s[1] or user_answer == s[2]:
        print("Congrats!")
        score = score + 1
      elif user_answer == "stop":
        stop = True
        score = str(score)
        print("your score is " + score)
      else:
        print("better luck next time")

Ask_questions()