import os
import imp

class LiveModule(object):
    def __init__(self, fileName):
        self._cached_stamp = 0
        self.filename = fileName
        self.modulename = self.filename.split('.')[0]
        print fileName
        print self.filename
        self.file, self.pathname, self.description = imp.find_module(self.modulename)
        self.mod = imp.load_module(self.modulename, self.file, self.pathname, self.description)
        self.file.close()
        
    def checkAndReload(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            print "Loading module, as it changed"
            self.file, self.pathname, self.description = imp.find_module(self.modulename)
            self.mod = imp.load_module(self.modulename, self.file, self.pathname, self.description)
            self.file.close()
        return self.mod

if __name__ == "__main__":
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(prog='PythonLive', description='Point file to watch')
    parser.add_argument('--watch', help='Python file to watch')

    args = parser.parse_args()

    print 'Observing {}'.format(args.watch)
    mod = LiveModule(args.watch)
    exit = False
    while not exit:
        input = raw_input('Next command: ')
        commandModule = mod.checkAndReload()
        print commandModule.process(input)
        if input == 'exit':
            exit = True
    sys.exit(0)        