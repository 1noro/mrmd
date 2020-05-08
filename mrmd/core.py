
import mrmd
from mrmd import utils
from mrmd import log
from mrmd import web

### EDITABLE VARIABLES #########################################################
TABULAR = " "*8

### AUTOMATIC VARIABLES ########################################################
verbose = 0
# version=open("version.txt").read().replace('\n','')
version="0.0.1"

### FUNCTIONS ##################################################################
# ...

### MAIN #######################################################################
def main():
    # --- Parameters -----------------------------------------------------------
    (options, args) = utils.options_definition()
    # --- verbose
    verbose = 0
    if options.verbose :
        verbose = int(options.verbose)

    # --- CHECK CONFIG ---------------------------------------------------------
    if verbose >= 1: log.p.info("starting  v"+version)

    # --- EXECUTION ------------------------------------------------------------
    # get_html(b'', verbose)
    # get_html(b'index.php?q=twin%20peaks%20s03e01&accion=5&masdesc=&subtitulos=1&realiza_b=1', verbose)
    # https://regex101.com/r/gU7pz3/1
    log.p.info("hola")

    # --- Exit -----------------------------------------------------------------
    if verbose >= 1: log.p.exit("end of the execution")
