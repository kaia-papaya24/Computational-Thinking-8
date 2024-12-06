###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background ("winter")
q1 = codesters.Square (100, 100, 200, 'blue')
q2 = codesters.Square (-100, 100, 200, 'yellow') 
q3 = codesters.Square (-100, -100, 200, 'red')
q4 = codesters.Square (100, -100, 200, 'green')                       
s1 = codesters.Sprite ("dad", 100, 100)
s2 = codesters.Sprite ("cardinal", -100, -100)
