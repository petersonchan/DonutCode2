import random

fontList = ["8bitOperatorPlus-Regular.ttf",
            "Arcade.ttf",
            "Bullpen3D.ttf",
            "chinese.simyou.ttf",
            "NeoTechItalic.ttf",
            "SuperMario256.ttf",
            "CHERL___.ttf",
            "Tintenfische.otf",
            "Bypass.ttf",
            "CubicCoreMono.ttf",
            "Panic.ttf"]

def main():
    return ( "fonts\\" + random.choice(fontList))
    #return ("fonts\\" + "Panic.ttf")

if __name__ == '__main__':
    main()