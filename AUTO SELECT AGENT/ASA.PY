import pyautogui, time
from PIL import Image, ImageGrab

class Agent:
    agentSelectBox = {"astra": (593, 931), "breach": (670, 931), "brimstone": (750, 931), "chamber": (831, 931), "cypher": (916, 931), "fade": (1005, 931), "jett": (1090, 931), "kayo": (1172, 931), "killjoy": (1257, 931), "kj": (1257, 931), "neon": (1340, 931), "omen": (586, 1011), "phoenix": (670, 1011), "raze": (750, 1011), "reyna": (831, 1011), "sage": (916, 1011), "skye": (1005, 1011), "sova": (1090, 1011), "viper": (1172, 1011), "yoru": (1257, 1011)}
    def __init__(self, agentName):
        self.agentName = agentName

    def selectAgent(self):
        time.sleep(3)
        while(True):
            agentSelectScreen = ImageGrab.grab().convert('L')
            arrayOfagentSelectScreen = agentSelectScreen.load()
            if arrayOfagentSelectScreen[0,0] == 142:
                pyautogui.click(self.agentSelectBox[self.agentName][0], self.agentSelectBox[self.agentName][1])#clicks on the agent select box
                pyautogui.click(958, 815)
                print(self.agentName)
                break     

def getScreenShot():
    agentSelectScreen = ImageGrab.grab().convert('L')
    agentSelectScreen.show()


agentObject = Agent(input("Enter the agent's name: ").lower())
agentObject.selectAgent()