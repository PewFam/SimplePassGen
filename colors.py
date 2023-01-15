class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    ORANGE = '\033[93m'
    FAIL = '\033[91m'
    GREEN = "\033[0;32m"
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"


class style:
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    TRY = '\033[2m'
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"


def clear():
    if __import__('os').name == "nt": __import__('os').system('cls')
    else:  __import__('os').system('clear')



    
    
def oringin():
    
        
        print('\n\n')
        print(color.BROWN +"""██████╗ ███████╗██╗    ██╗███████╗ █████╗ ███╗   ███╗
██╔══██╗██╔════╝██║    ██║██╔════╝██╔══██╗████╗ ████║
██████╔╝█████╗  ██║ █╗ ██║█████╗  ███████║██╔████╔██║
██╔═══╝ ██╔══╝  ██║███╗██║██╔══╝  ██╔══██║██║╚██╔╝██║
██║     ███████╗╚███╔███╔╝██║     ██║  ██║██║ ╚═╝ ██║
╚═╝     ╚══════╝ ╚══╝╚══╝ ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  on github
                                                      """)
        print(color.PURPLE+'This multi tools library has been made to help you to make your codes better formated.')
        print(color.CYAN+'\nWrite explain(colors) in your code to show colors and styles'+ style.END)

def explain(colors):
    if colors =="colors":
        print(f"""{color.YELLOW}\ncolors:
    
    HEADER
    OKBLUE
    OKCYAN
    OKGREEN
    ORANGE
    FAIL
    GREEN
    BLACK
    RED
    GREEN
    BROWN
    BLUE
    PURPLE
    CYAN
    LIGHT_GRAY
    DARK_GRAY 
    LIGHT_RED
    LIGHT_GREEN
    YELLOW
    LIGHT_BLUE
    LIGHT_PURPLE
    LIGHT_CYAN
    LIGHT_WHITE

{color.PURPLE}styles:

    UNDERLINE 
    BOLD 
    TRY 
    BOLD 
    FAINT 
    ITALIC 
    UNDERLINE 
    BLINK 
    NEGATIVE 
    CROSSED 
    END = remove all style
    {style.END}
\n\n""")