from core.gui import setup
from core.licenceManager import LicenceManager



if __name__ == "__main__":

    try:
        from PyQt5.uic import loadUi
        import pyqtgraph as pg
        setup(LicenceManager(),debug=True)
    except ImportError:
        import os
        input("Appuyez sur entrée pour tenter une installation des modules nécésaires")
        os.system("py -m pip install PyQt5 pyqtgraph")
        os.system("python -m pip install PyQt5 pyqtgraph")
