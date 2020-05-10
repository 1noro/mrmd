# core.logsprint
### CLASSES ###################################################################
class bcolor:
    NONE = ''
    INFO = ''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class p:
    def info(txt):      print(bcolor.INFO       + "[INFO] " + txt + bcolor.ENDC)
    def sinfo(txt):     print(bcolor.HEADER     + "[INFO] " + txt + bcolor.ENDC)
    def ok(txt):        print(bcolor.OKGREEN    + "[ OK ] " + txt + bcolor.ENDC)
    def warning(txt):   print(bcolor.WARNING    + "[WARN] " + txt + bcolor.ENDC)
    def fail(txt):      print(bcolor.FAIL       + "[FAIL] " + txt + bcolor.ENDC)
    def exit(txt):      print(bcolor.OKBLUE     + "[EXIT] " + txt + bcolor.ENDC)
    def loop(txt):      print(bcolor.OKBLUE     + "[LOOP] " + txt + bcolor.ENDC)
    def cin(txt):       print(bcolor.INFO       + "[ <--] " + txt + bcolor.ENDC)
    def cout(txt):      print(bcolor.INFO       + "[--> ] " + txt + bcolor.ENDC)
    def sslcin(txt):    print(bcolor.INFO       + "[ <~~] " + txt + bcolor.ENDC)
    def sslcout(txt):   print(bcolor.INFO       + "[~~> ] " + txt + bcolor.ENDC)

class pt:
    def info(txt, name = 'main'):      print(bcolor.INFO       + "[INFO] " + name + ": " + txt + bcolor.ENDC)
    def sinfo(txt, name = 'main'):     print(bcolor.HEADER     + "[INFO] " + name + ": " + txt + bcolor.ENDC)
    def ok(txt, name = 'main'):        print(bcolor.OKGREEN    + "[ OK ] " + name + ": " + txt + bcolor.ENDC)
    def warning(txt, name = 'main'):   print(bcolor.WARNING    + "[WARN] " + name + ": " + txt + bcolor.ENDC)
    def fail(txt, name = 'main'):      print(bcolor.FAIL       + "[FAIL] " + name + ": " + txt + bcolor.ENDC)
    def exit(txt, name = 'main'):      print(bcolor.OKBLUE     + "[EXIT] " + name + ": " + txt + bcolor.ENDC)
    def loop(txt, name = 'main'):      print(bcolor.OKBLUE     + "[LOOP] " + name + ": " + txt + bcolor.ENDC)
    def cin(txt, name = 'main'):       print(bcolor.INFO       + "[ <--] " + name + ": " + txt + bcolor.ENDC)
    def cout(txt, name = 'main'):      print(bcolor.INFO       + "[--> ] " + name + ": " + txt + bcolor.ENDC)
    def sslcin(txt, name = 'main'):    print(bcolor.INFO       + "[ <~~] " + name + ": " + txt + bcolor.ENDC)
    def sslcout(txt, name = 'main'):   print(bcolor.INFO       + "[~~> ] " + name + ": " + txt + bcolor.ENDC)
