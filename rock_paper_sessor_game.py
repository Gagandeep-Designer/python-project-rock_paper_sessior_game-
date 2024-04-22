import random
l=["rock","scissor","paper"]
while True:
  ccount=0
  ucount=0
  user_choice=int(input('''
Game Start.......
1.Yes
2.No|Exit
      '''))
  if user_choice==1:
   for a in range(1,6):
     user_input=int(input('''
1.Rock
2.scissor
3.paper                                                    
                      '''))
     if user_input==1:
       uchoice="rock"
     elif user_input==2:
        uchoice="scissor"
     elif user_input==3:
        uchoice="paper"
     Cchoice=random.choice(l)
     if Cchoice==uchoice:
       print("user value",uchoice)
       print("Computer value",Cchoice)
       print("Game Draw")
       ucount=ucount+1
       ccount=ccount+1
     elif (uchoice=='rock' and Cchoice=='scissor') or(uchoice=='paper' and Cchoice=='rock')or(uchoice=='scissor' and Cchoice=='paper'):
       print("user value",uchoice)
       print("Computer value",Cchoice)
       print("You Win")
       ucount=ucount+1
     else:
       print("user value",uchoice)
       print("Computer value",Cchoice)
       print("Computer Win")
       ccount=ccount+1
   if ucount==ccount:
    print("Final Game Draw.....")
    print("User Score",ucount)
    print("Computer Score",ccount)  
   elif ucount>ccount:
    print("Final You Win The Game.....")
    print("User Score",ucount)
    print("Computer Score",ccount)   
   else:
    print("Final Computer Win The Game.....")
    print("User Score",ucount)
    print("Computer Score",ccount)      
  else:
    break;