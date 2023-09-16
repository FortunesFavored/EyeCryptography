from .Messages.rawEyes1 import msg as RawMessage1
from .Messages.rawEyes2 import msg as RawMessage2
from .Messages.rawEyes3 import msg as RawMessage3
from .Messages.rawEyes4 import msg as RawMessage4
from .Messages.rawEyes5 import msg as RawMessage5
from .Messages.rawEyes7 import msg as RawMessage6
from .Messages.rawEyes7 import msg as RawMessage7
from .Messages.rawEyes8 import msg as RawMessage8
from .Messages.rawEyes9 import msg as RawMessage9


class SourceEyes(object):

    def __init__(self) -> None:
        self.East1 = RawMessage1
        self.West1 = RawMessage2
        self.East2 = RawMessage3
        self.West2 = RawMessage4
        self.East3 = RawMessage5
        self.West3 = RawMessage6
        self.East4 = RawMessage7
        self.West4 = RawMessage8
        self.East5 = RawMessage9
        pass

    def GenerateMessage(self, rawMsg: dict, direction: int = 1):
        completeMsg = []
        for pair in rawMsg.keys():
            hexString = rawMsg[pair]['b'] + rawMsg[pair]['a']
            completeMsg = completeMsg + (self.Base5FromBase7(self.Base7FromHex(hexString[::direction])))
        seperatedMsg = [[]]
        rowIndex = 0
        for value in completeMsg:
            if value != 5:
                seperatedMsg[rowIndex].append(value)
            else:
                seperatedMsg[rowIndex].append(value)
                rowIndex += 1
                seperatedMsg.append([])
        return seperatedMsg
    
    def Base7FromHex(self, hexString):
        hexValue = int(hexString, 16)
        base7 = []
        while hexValue != 0:
            # print(hexValue)
            base7 =  [hexValue % 7] + base7  
            hexValue = hexValue // 7
        return base7
    
    def Base5FromBase7(self, base7Value):
        valueList = []
        [valueList.append(int(x)-1) for x in base7Value if int(x) > 0]
        return valueList
    
    def getEyeGroups(self, generatedMsg, readingOrder: list = [0,1,2]):
        groups = []
        for i in range(0, len(generatedMsg), 2):
            tracker = 0
            if generatedMsg[i] == []: break
            while tracker < len(generatedMsg[i])-1:
                #  add first eye
                try:
                    eyeSet1 = [generatedMsg[i][tracker],generatedMsg[i][tracker+1],generatedMsg[i+1][tracker]]
                    groups.append([eyeSet1[readingOrder[0]],eyeSet1[readingOrder[1]],eyeSet1[readingOrder[2]]])
                except:
                    pass
                #  add second eye
                try:
                    eyeSet2 = [generatedMsg[i+1][tracker+2],generatedMsg[i+1][tracker+1],generatedMsg[i][tracker+2]]
                    groups.append([eyeSet2[readingOrder[0]],eyeSet2[readingOrder[1]],eyeSet2[readingOrder[2]]])
                except:
                    pass
                tracker += 3
        return groups
    
    def generateValueList(self, eyeGroup: list):
        return [int(''.join([str(i) for i in q])) for q in eyeGroup]
    
    def generateBaseNList(self, eyeValueList: list, base: int = 5):
        return [int(q, base=base) for q in eyeValueList]
    
    def generateAscii32List(self, eyeGroup: list):
        return [chr(v+32) for v in eyeGroup]
    


    