# Import Dependencies
import pandas as pd
from time import sleep
import pyautogui as bot
from playsound import playsound
import os



class LineBot:
    def __init__(self):
        self.data = pd.read_excel('database.xlsx')
    
    def get_data(self, gender=0, religion=0):
        data = self.data[['Name', 'Line ID', 'Gender', 'Religion']].dropna()
        
        # Gender Description
        # Type 0 : Male & Female
        # Type 1 : Male
        # Type 2 : Female
        male    = data[data['Gender'].str.match('Male')]
        female  = data[data['Gender'].str.match('Female')]
        
        
        # Religion Description
        # Type 0 : All
        # Type 1 : Muslim
        # Type 2 : Christian
        # Type 3 : Catholic
        # Type 4 : Hindu
        # Type 5 : Muslim + Christian + Hindu
        # Type 6 : Muslim + Catholic + Hindu
        # Type 7 : Muslim + Christian + Catholic
        Muslim      = data[data['Religion'].str.match('Islam')]
        Christian   = data[data['Religion'].str.match('Christian')]
        Catholic    = data[data['Religion'].str.match('Catholic')]
        Hindu       = data[data['Religion'].str.match('Hindu')]
        
        frames = pd.DataFrame()
        match gender:
            case 0: # Male & Female
                match religion:
                    case 0:
                        frames = [data]
                    case 1:
                        frames = [Muslim]
                    case 2:
                        frames = [Christian]
                    case 3:
                        frames = [Catholic]
                    case 4:
                        frames = [Hindu]
                    case 5:
                        frames = [Muslim, Christian, Hindu]
                    case 6:
                        frames = [Muslim, Catholic, Hindu]
                    case 7:
                        frames = [Muslim, Christian, Hindu]
                    
            case 1: # Male
                match religion:
                    case 0:
                        frames = [male]
                    case 1:
                        frames = [Muslim[male.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 2:
                        frames = [Christian[male.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 3:
                        frames = [Catholic[male.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 4:
                        frames = [Hindu[male.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 5:
                        frames = [Muslim[male.duplicated('Name', keep=False)].drop_duplicates('Name'), Christian[male.duplicated('Name', keep=False)].drop_duplicates('Name'), Hindu[male.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 6:
                        frames = [Muslim[male.duplicated('Name', keep=False)].drop_duplicates('Name'), Catholic[male.duplicated('Name', keep=False)].drop_duplicates('Name'), Hindu[male.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 7:
                        frames = [Muslim[male.duplicated('Name', keep=False)].drop_duplicates('Name'), Christian[male.duplicated('Name', keep=False)].drop_duplicates('Name'), Hindu[male.duplicated('Name', keep=False)].drop_duplicates('Name')]
                
                
            case 2: # Female
                match religion:
                    case 0:
                        frames = [female]
                    case 1:
                        frames = [Muslim[female.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 2:
                        frames = [Christian[female.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 3:
                        frames = [Catholic[female.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 4:
                        frames = [Hindu[female.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 5:
                        frames = [Muslim[female.duplicated('Name', keep=False)].drop_duplicates('Name'), Christian[female.duplicated('Name', keep=False)].drop_duplicates('Name'), Hindu[female.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 6:
                        frames = [Muslim[female.duplicated('Name', keep=False)].drop_duplicates('Name'), Catholic[female.duplicated('Name', keep=False)].drop_duplicates('Name'), Hindu[female.duplicated('Name', keep=False)].drop_duplicates('Name')]
                    case 7:
                        frames = [Muslim[female.duplicated('Name', keep=False)].drop_duplicates('Name'), Christian[female.duplicated('Name', keep=False)].drop_duplicates('Name'), Hindu[female.duplicated('Name', keep=False)].drop_duplicates('Name')]
        self.result = pd.concat(frames)


    def get_coordinates(self):
        x = []
        for category in ['Search by Id', 'Chats', 'Enter a message']:
            print(f"Please hover mouse over [{category}] \nCounting down in 5\n\n")
            sleep(3)
            for i in bot.position():
                x.append(i)
            playsound(f"{os.getcwd()}/Audio/ping.mp3")
        self.list_coordinates = x
    
    
    def iterate(self):
        for ind in self.result.index:
            bot.click(self.list_coordinates[0], self.list_coordinates[1])
            sleep(.1)
            bot.hotkey('ctrl', 'a')
            bot.press('delete')
            bot.write(self.result['Line ID'][ind])
            bot.write('\n')
            sleep(.3)
        
            bot.click(self.list_coordinates[2], self.list_coordinates[3])
            bot.click(self.list_coordinates[2]-15, self.list_coordinates[3]-15)
            bot.click(self.list_coordinates[2]+15, self.list_coordinates[3]+15)
            sleep(.1)
            
            
            bot.click(self.list_coordinates[4], self.list_coordinates[5])
            bot.hotkey('ctrl', 'v')
            bot.write('\n')
            sleep(.5)
        
        
    def main(self):
        self.get_data(gender=1, religion=0)
        self.get_coordinates()
        self.iterate()
        
        

if __name__ == '__main__':
    Program = LineBot()
    Program.main()
            