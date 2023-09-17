My first python module for use with the noita eyes

## Example script to getting the common ascii characters and printing them to the console.

```
from EyeGenerator import eyeSource

source = eyeSource.EyeSource()

messages = source.getFastAsciiChars()

print(messages['East1'])
print(messages['West1'])
print(messages['East2'])
print(messages['West2'])
print(messages['East3'])
print(messages['West3'])
print(messages['East4'])
print(messages['West4'])
print(messages['East5'])

```

## Example script to generate the sequence of interleaved eye values

```
from EyeGenerator import eyeSource

source = eyeSource.EyeSource()

interleaved = source.GenerateMessageSD(source.East1)

print(interleaved)
```


## Example script for generating the eye trigrams using conventional reading order

```
from EyeGenerator import eyeSource

source = eyeSource.EyeSource()

interleaved = source.GenerateMessageSD(source.East1)

trigramGroups = source.getEyeGroups(interleaved)

print(trigramGroups)
```