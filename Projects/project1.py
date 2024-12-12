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
s1 = codesters.Sprite ("cutecat", 100,-100)
s1.set_size(0.5)
s2 = codesters.Sprite ("cardinal", -100, -100)
s3 = codesters.Sprite ("birthday", 100, 100)
s3.set_size(0.5)
s4 = codesters.Sprite ("cookie", -100,100)
message1 = codesters.Text ("so um guys....", 0,-220,"black")