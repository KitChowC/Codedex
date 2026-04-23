# Write code below 💖

import random

Magic = [
  "Yes - definitely.",
  "It is decidedly so.",
  "Without a doubt.",
  "Reply hazy, try again.",
  "Ask again later.",
  "Better not tell you now.",
  "My sources say no.",
  "Outlook not so good.",
  "Very doubtful."
]

Question = input("Question: ")
Answer = random.randint(0,8)
print(Magic[Answer])
