from menu.mainMenu import design as designPrincipal
from menu.calculateTip import design as designOption1
from menu.divideAmountsMenu import design as designOption2
from menu.leaveProgram import design as designOption3

options = designPrincipal() 
if options == 1:
    designOption1()
if options == 2:
    designOption2()
if options == 3:
    designOption3()


