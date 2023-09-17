from .Messages.rawDataBulk import sourceData
from .utils import *

class EyeSource(object):

    def __init__(self) -> None:
        self.SD = sourceData
        self.East1 = sourceData[0]
        self.West1 = sourceData[1]
        self.East2 = sourceData[2]
        self.West2 = sourceData[3]
        self.East3 = sourceData[4]
        self.West3 = sourceData[5]
        self.West4 = sourceData[6]
        self.East4 = sourceData[7]
        self.East5 = sourceData[8]
        pass

    def GenerateMessageSD(self, rawMsg: list, direction: int = 1):
        completeMsg = []
        for pair in rawMsg:
            hexString = pair[1]+pair[0]
            # print(hexString)
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
    
    def getEyeGroups(self, generatedMsg, readingOrder1: list = [0,1,2], readingOrder2: list = None):
        if readingOrder2 is None: readingOrder2 = readingOrder1
        groups = []
        for i in range(0, len(generatedMsg), 2):
            tracker = 0
            if generatedMsg[i] == []: break
            while tracker < len(generatedMsg[i])-1:
                #  add first eye
                try:
                    eyeSet1 = [generatedMsg[i][tracker],generatedMsg[i][tracker+1],generatedMsg[i+1][tracker]]
                    groups.append([eyeSet1[readingOrder1[0]],eyeSet1[readingOrder1[1]],eyeSet1[readingOrder1[2]]])
                except:
                    pass
                #  add second eye
                try:
                    eyeSet2 = [generatedMsg[i+1][tracker+2],generatedMsg[i+1][tracker+1],generatedMsg[i][tracker+2]]
                    groups.append([eyeSet2[readingOrder2[0]],eyeSet2[readingOrder2[1]],eyeSet2[readingOrder2[2]]])
                except:
                    pass
                tracker += 3
        return groups
       
    def getFastAsciiChars(self):
        return {
            'East1': ''.join(fastAsciiGen(self.getEyeGroups(self.GenerateMessageSD(self.East1)))),
            'West1': ''.join(fastAsciiGen(self.getEyeGroups(self.GenerateMessageSD(self.West1)))),
            'East2': ''.join(fastAsciiGen(self.getEyeGroups(self.GenerateMessageSD(self.East2)))),
            'West2': ''.join(fastAsciiGen(self.getEyeGroups(self.GenerateMessageSD(self.West2)))),
            'East3': ''.join(fastAsciiGen(self.getEyeGroups(self.GenerateMessageSD(self.East3)))),
            'West3': ''.join(fastAsciiGen(self.getEyeGroups(self.GenerateMessageSD(self.West3)))),
            'East4': ''.join(fastAsciiGen(self.getEyeGroups(self.GenerateMessageSD(self.East4)))),
            'West4': ''.join(fastAsciiGen(self.getEyeGroups(self.GenerateMessageSD(self.West4)))),
            'East5': ''.join(fastAsciiGen(self.getEyeGroups(self.GenerateMessageSD(self.East5)))),
        }

    