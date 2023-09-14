import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice=int(input(print("what do you want to choose? enter 0 for rock, 1 for paper and 2 for scissors.")))
if choice == 0:
  print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

elif choice==1:
  print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif choice==2:
  print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
print("computer chose")
c=random.randint(0,2)
if c==0:
  print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
  if c==choice:
    print("It's draw!")
  elif choice==1:
    print("You win!")
  elif choice==2:
    print("You lose!")

elif c==1:
  print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
  if c==choice:
    print("It's draw!")
  elif choice==2:
    print("You win!")
  elif choice==0:
    print("You lose!")
elif c==2:
  print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
if c==choice:
    print("It's draw!")
elif choice==0:
    print("You win!")
elif choice==1:
    print("You lose!")
