"""
Create a Python file named lab_2-8.py
A team needs to score 15 points to win a gold medal, between 12-14 points to win a silver medal, 
and between 9-11 point to win a bronze medal. A team does not earn a medal if they earn 8 or fewer points.
Write a program using nested if else statements where a user can input the number of points a team scored and the medal that they earned is displayed.

"""
a = input('how many point a team scored')
a= int(a)
if a>=15: print('earned gold medal')
else :
    if 12<=a<14:
        print ('earned silver medal')
    else: 
        if (9<=a<=11):
         print('earned bronze medal')

         if a<=8: print (' no meadal earned')