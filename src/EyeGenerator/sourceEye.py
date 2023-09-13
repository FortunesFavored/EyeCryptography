from .Messages.rawEyes1 import msg as RawMessage1
from .Messages.rawEyes2 import msg as RawMessage2
from .Messages.rawEyes3 import msg as RawMessage3
from .Messages.rawEyes4 import msg as RawMessage4
from .Messages.rawEyes5 import msg as RawMessage5
from .Messages.rawEyes7 import msg as RawMessage6
from .Messages.rawEyes7 import msg as RawMessage7
from .Messages.rawEyes8 import msg as RawMessage8
from .Messages.rawEyes9 import msg as RawMessage9


class SourceEyes:
    RawMessage1 = RawMessage1
    RawMessage2 = RawMessage2
    RawMessage3 = RawMessage3
    RawMessage4 = RawMessage4
    RawMessage5 = RawMessage5
    RawMessage6 = RawMessage6
    RawMessage7 = RawMessage7
    RawMessage8 = RawMessage8
    RawMessage9 = RawMessage9

    def __init__(self) -> None:
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
    
    def reverseHexPairs(self, hexString: str):
        pointer = 0
        revHexString = ''
        while pointer < len(hexString):
            revHexString = hexString[pointer:pointer+2:] + revHexString
            pointer += 2
        return revHexString
    
    def reverseMsgHex(self, rawMsg: dict):
        reversedMessageDict = {}
        for pair in rawMsg.keys():
            reversedMessageDict[pair] = {
                'a': self.reverseHexPairs(rawMsg[pair]['a']),
                'b': self.reverseHexPairs(rawMsg[pair]['b']),
            }
        return reversedMessageDict