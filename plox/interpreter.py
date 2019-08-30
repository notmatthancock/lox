import sys
from scanner import Scanner


REPL_EXIT = 'exit'


class PLox:

    def run_source(self, source_string):
        scanner = Scanner(source_string)
        scanner.scan()

    def run_file(self, lox_file):
        with open(lox_file, 'r') as f:
            script_contents = f.read()
        self.run_source(script_contents)

    def run_repl(self):
        while True:
            try:
                line = input('> ')
            except KeyboardInterrupt:
                line = REPL_EXIT

            if line == REPL_EXIT:
                print('Exiting...')
                break
            else:
                self.run_source(line)

    def main(self):
        if len(sys.argv) > 2:
            print("Usage: plox [script]")
        elif len(sys.argv) == 2:
            self.run_file(sys.argv[1])
        else:
            self.run_repl()


if __name__ == '__main__':
    plox = PLox()
    plox.main()
