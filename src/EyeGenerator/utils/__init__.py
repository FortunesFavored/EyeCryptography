def generateValueList(eyeGroup: list):
    '''Goes through the eye message group and combines the number representation into a single value. Leading zeros are dropped.'''
    return [str(''.join([str(i) for i in q])) for q in eyeGroup]

def generateBaseNList(eyeValueList: list, base: int = 5):
    '''Takes an array of numbers (representing eye groups) and converts them to a specific base value (defaults to 5).'''
    return [int(q, base=base) for q in eyeValueList]

def generateAscii32List(eyeValueList: list, offset: int = 32):
    '''Takes array of numbers (representing eye groups) and for each value adds an offset (default 32) and then converts them to ascii.'''
    return [chr(v+offset) for v in eyeValueList]

def fastAsciiGen( eyeGroup: list):
    return generateAscii32List(generateBaseNList(generateValueList(eyeGroup)))

