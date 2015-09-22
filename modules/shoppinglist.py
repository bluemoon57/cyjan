import os

def run(**args):
    print "[+] Entered shoppinglist module"
    files = os.listdir('.')
    return str(files)
