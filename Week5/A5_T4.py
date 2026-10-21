print("Program starting.")
def askDimension(PPrompt: str) -> float:
    feed = input(f"Insert {PPrompt}: ")
    return float(feed)

width = askDimension("width")
height = askDimension("height")

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    area = PWidth * PHeight
    return area

area = calcRectangleArea(width, height)
print("")
print(f"Area is {area}²")
print("Program ending.")