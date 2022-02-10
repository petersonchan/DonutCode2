import ASCII as ascii


def main(asciiCharts=[], bodyPath="ascii_image.txt", backgroundPath="ascii_image_background.txt"):
    b = open("ascii_image.txt", "r")
    bodyText = b.read()
    #print(bodyText)

    c = open("ascii_image_background.txt", "r")
    backgroundText = c.read()
    #print(backgroundText)

    combinedText = []
    for i in range(len(bodyText)):
        combinedText.append(None)
    #print("length of combinedText: ", len(combinedText))
    #print("length of bodyText: ", len(bodyText))
    #print("length of backgroundText: ", len(backgroundText))

    for i in range(len(bodyText)):
        try:
            if backgroundText[i] == '@':
                combinedText[i] = bodyText[i]
            elif backgroundText[i] == 'Z':
                if bodyText[i] == asciiCharts[0]:
                    combinedText[i] = 'Z'
                elif bodyText[i] != asciiCharts[0]:
                    combinedText[i] = bodyText[i]
        except:
            combinedText[i] = bodyText[i]
    #print(combinedText)
    #print(len(combinedText))
    characters = [char for char in combinedText if char != None]
    characters2 = [char for char in characters if char != '\n']
    char2 = "".join(characters2)
    #char3 =  "\n".join(char2[index:(index + 50)] for index in range(0, len(char2), 50))
    char3 = "\n".join(char2[index:(index + 100)] for index in range(0, len(char2), 100))

    #print(characters)
    #print(char2)
    #print(char3)

    with open("ascii_image_combined.txt", "w") as f:
        f.write(char3)

if __name__ == '__main__':
    main(asciiCharts=[],bodyPath="ascii_image.txt", backgroundPath="ascii_image_background.txt")