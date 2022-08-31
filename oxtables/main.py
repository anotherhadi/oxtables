####################################################################
#           ______________________________________
#  ________|               OxTables               |_______
#  \       |                                      |      /
#   \      |              @0x68616469             |     /
#   /      |______________________________________|     \
#  /__________)                                (_________\
#
# A Handy Package to Draw ASCII Tables
#
# Github repo : https://github.com/0x68616469/oxtables
#
####################################################################

class Table:

    def __init__(self, **kwargs):
        self.style = kwargs.get('style', '-')
        self.data = kwargs.get('data', [])
        self.spacer = kwargs.get('spacer', True)
        self.border_color = kwargs.get('border_color', 'black')
        self.text_color = kwargs.get('text_color', 'white')
        self.align = kwargs.get('align', 'left')
        self.max_length = kwargs.get('max_length', 50)
        self.first_row = kwargs.get('first_row', 'default')
    
    def color(self, name):    
        if name == "red": return '\033[31m'
        elif name == "green": return '\033[32m'
        elif name == "yellow": return '\033[33m'
        elif name == "blue": return '\033[34m' 
        elif name == "magenta": return '\033[35m'
        elif name == "cyan": return '\033[36m' 
        elif name == "white": return '\033[0m'
        else: return '\033[30m'  # Default : Black
    
    def add(self, data=[]):
        self.data.append(data)

    def draw(self):
        nrow = 0
        ncol = 0
        
        for row in self.data:
            nrow += 1
            if len(row) > ncol:
                ncol = len(row)
                        
        col_size = []
        for i in range(ncol):
            col_size.append(0)
            for row in self.data:
                try:
                    if len(row[i]) > col_size[i]:
                        if len(row[i]) > self.max_length:
                            row[i] = row[i][:self.max_length-2] + ".."
                        col_size[i] = len(row[i])
                except:
                    continue
        
        # Styling
        bg_color = self.color(self.border_color)
        text_color = self.color(self.text_color)   
         
        if self.style == "-":
            top_left = f"{bg_color}┌\033[0m"
            top_right = f"{bg_color}┐\033[0m"
            bottom_left = f"{bg_color}└\033[0m"
            bottom_right = f"{bg_color}┘\033[0m"
            to_left = f"{bg_color}┤\033[0m"
            to_right = f"{bg_color}├\033[0m"
            to_down = f"{bg_color}┬\033[0m"
            to_up = f"{bg_color}┴\033[0m"
            middle = f"{bg_color}┼\033[0m"
            verticaly = f"{bg_color}│\033[0m"
            horizontaly = f"{bg_color}─\033[0m"  

        elif self.style == "=":
            top_left = f"{bg_color}╔\033[0m"
            top_right = f"{bg_color}╗\033[0m"
            bottom_left = f"{bg_color}╚\033[0m"
            bottom_right = f"{bg_color}╝\033[0m"
            to_left = f"{bg_color}╣\033[0m"
            to_right = f"{bg_color}╠\033[0m"
            to_up = f"{bg_color}╩\033[0m"
            to_down = f"{bg_color}╦\033[0m"
            middle = f"{bg_color}╬\033[0m"
            verticaly = f"{bg_color}║\033[0m"
            horizontaly = f"{bg_color}═\033[0m"

        else:
            top_left = " "
            top_right = " "
            bottom_left = " "
            bottom_right = " "
            to_left = " "
            to_right = " "
            to_up = " "
            to_down = " "
            middle = " "
            verticaly = " "
            horizontaly = " "

        # Top row
        if self.first_row == "default" or self.first_row == "border":
            print(top_left,end="")
            for i in range(ncol-1):
                for j in range(col_size[i]+2):
                    print(horizontaly, end="")
                print(to_down,end="")
            if ncol > 1:
                for j in range(col_size[i+1]+2):
                    print(horizontaly, end="")
            else:
                for j in range(col_size[i]+2):
                    print(horizontaly, end="")          
            print(top_right)
        
        # Write data
        crow = 1
        for row in self.data:
            i = 0
            for col in row:
                if crow == 1 and self.first_row == "none":
                    print("  ", end="")
                else:
                    print(f"{verticaly} ", end="")
                
                print(text_color, end="")
                if self.align == "right":
                    for j in range(len(col), col_size[i]):
                        print(" ", end="")
                    print(f"{col} ", end="")
                
                elif self.align == "center":
                    for j in range(int((col_size[i]-len(col))/2)):    
                        print(" ", end="")
                    print(f"{col} ", end="")
                    if col_size[i] > 1:
                        for k in range(col_size[i]-len(col)-j-1):    
                            print(" ", end="") 
                else:
                    print(col, end="")
                    for j in range(len(str(col)), col_size[i]+1):
                        print(" ", end="")
                print('\033[0m', end="")

                i += 1
            
            for j in range(i, ncol):
                if crow == 1 and self.first_row == "none":
                    print("  ", end="")
                else:
                    print(f"{verticaly}", end="")
                for k in range(col_size[j]+1):
                    print(" ", end="")  
            
            if crow == 1 and self.first_row == "none":
                print(" ")
            else:
                print(verticaly)   

            # Spacers
            if self.spacer or (self.first_row == "border" and crow == 1):
                if crow < nrow:
                    if crow == 1 and self.first_row == "none":
                        print(top_left,end="")
                    else:
                        print(to_right,end="")
                    for i in range(ncol-1):
                        for j in range(col_size[i]+2):
                            print(horizontaly, end="")
                        if crow == 1 and self.first_row == "none":
                            print(to_down,end="")
                        else:
                            print(middle,end="")
                    if ncol > 1:
                        for j in range(col_size[i+1]+2):
                            print(horizontaly, end="")
                    else:
                         for j in range(col_size[i-1]+2):
                                print(horizontaly, end="")                       
                    if crow == 1 and self.first_row == "none":
                        print(top_right)
                    else:
                        print(to_left)            
            crow += 1  
        
        # Bottom row
        print(bottom_left,end="")
        for i in range(ncol-1):
            for j in range(col_size[i]+2):
                print(horizontaly, end="")
            print(to_up,end="")
        if ncol > 1:
            for j in range(col_size[i+1]+2):
                print(horizontaly, end="")
        else:
            for j in range(col_size[i-1]+2):
                print(horizontaly, end="")         
        print(bottom_right)