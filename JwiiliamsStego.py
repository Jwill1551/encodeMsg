#Joshua Williams
#A Program that encodes a secret message
#12/8/19

alphaArray = (['a','b','c','d','e','f','g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M',
               'N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!'])

def ClearLSBPic(aPicture):
  for px in getPixels(aPicture):
    setRed(px,getRed(px) & 252)
    setGreen(px,getGreen(px) & 252)
    setBlue(px,getBlue(px) & 252)
  return aPicture
  
def encodeMsg():
  for counter in range(0,len(msg)):
    charIndex = alphaArray.index(msg[counter])
    charIndex = charIndex + key.index(key[counter % len(key)])
    leftBits = charIndex & 48
    leftBits = leftBits >> 4 
    middleBits = charIndex & 12
    middleBits = middleBits >> 2 
    rightBits = charIndex & 3
    setRed(allPixels[counter],getRed(allPixels[counter]) | leftBits)
    setBlue(allPixels[counter],getBlue(allPixels[counter]) | middleBits)
    setGreen(allPixels[counter],getGreen(allPixels[counter]) | rightBits)
    

def decodeMsg():
  decodedMsg = ""
  for counter in range(0,len(msg)):
    redBits = getRed(allPixels[counter]) & 3
    blueBits = getBlue(allPixels[counter]) & 3
    greenBits = getGreen(allPixels[counter]) & 3
    charIndex = ((0 | greenBits) | (blueBits << 2)) | (redBits << 4)
    charIndex = charIndex - key.index(key[counter % len(key)])
    decodedMsg = decodedMsg + alphaArray[charIndex]
  return decodedMsg
  
key = "LopesUp!"
setMediaPath("")
orginPic = makePicture(getMediaPath("/finalCanvas.jpg"))
explore(orginPic)
clearLSB = ClearLSBPic(orginPic)
explore(clearLSB)

doc = pickAFile()
file = open(doc, "r")
msg = file.read()
allPixels = getPixels(clearLSB)

encodeMsg()
decodedMessage = decodeMsg()
print decodedMessage