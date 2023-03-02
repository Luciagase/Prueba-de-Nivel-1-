#El script principal que lo pondrá todo en marcha
import sys
import menu

if __name__ == "__main__":
    len(sys.argv) > 1 and sys.argv[1] == "-t"
    menu.iniciar()
    
