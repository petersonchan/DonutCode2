import random

colourList = \
[
    ["#43FF21", "#323232", "#FA4EAB", "#FE83C6", "#FFF2F9", "#B4FFFA"],
    ["#FF7B21", "#072227", "#35858B", "#4FBDBA", "#AEFEFF", "#6CFF92"],
    ["#468C7A", "#D9D7F1", "#FFFDDE", "#E7FBBE", "#FFCBCB", "#3E4153"],
    ["#FFEB54", "#FF008E", "#D22779", "#612897", "#0C1E7F", "#FEE8D9"],
    ["#29FFD4", "#000000", "#5800FF", "#E900FF", "#FFC600", "#FFA497"],
    ["#138F76",	"#171717", "#444444", "#DA0037", "#EDEDED", "#FADB5A"],
    ["#FF8280",	"#F2F9F1", "#388E3C", "#8BC34A", "#DDEEDF", "#FFFDDE"],
    ["#8F3F13",	"#212121", "#323232", "#0D7377", "#14FFEC", "#05FA98"],
    ["#B9E937",	"#FDEBF7", "#FBCAFF", "#FFADF0", "#FC28FB", "#212121"],
    ["#8F3F83",	"#51EAEA", "#FFFDE1", "#FF9D76", "#FB3569", "#F2F9F1"],
    ["#23EB69",	"#F90716", "#F90716", "#FFCA03", "#FFF323", "#8A94FF"],
    ["#E838FA", "#F5F5F5", "#B9E937", "#57D131", "#406661", "#FFD292"],
    ["#9CC0EB", "#876445", "#CA965C", "#EEC373", "#F4DFBA", "#F2F9F1"],
    ["#8BC34A", "#1A1A40", "#270082", "#7A0BC0", "#FA58B6", "#E4E4E4"],
    ["#ACE9A9", "#FF00E4", "#ED50F1", "#FDB9FC", "#FFEDED", "#87D8FF"],
    ["#0A8F67", "#FEFF89", "#FF9F68", "#F85959", "#AC005D", "#000000"],
    ["#FFB460", "#7900FF", "#548CFF", "#93FFD8", "#CFFFDC", "#F480FF"],
    ["#FFA919", "#23374D", "#1089FF", "#E5E5E5", "#EEEEEE", "#D3ECFA"],
    ["#F5DD53", "#22577E", "#5584AC", "#95D1CC", "#F6F2D4", "#FC8BC4"],
    ["#6ED1FB", "#F76E11", "#FF9F45", "#FFBC80", "#FC4F4F", "#000000"]
]

def main():
    return random.choice(colourList)


if __name__ == '__main__':
    main()