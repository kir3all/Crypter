from email import message
from RC4 import RC4
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-stdin", help="get data from stdin", action='store_true') # TODO description
parser.add_argument("-k", "--key", help="key for algorithm", type=str, required=True)
parser.add_argument("-o", "--output", help="output file", type=argparse.FileType('wb'))
parser.add_argument('-f', '--file', help="input file", type=argparse.FileType('rb'))
parser.add_argument('-m', '--message', help='message for crypt', type=str)

if __name__ == "__main__":
    args = parser.parse_args()
    dcod = RC4(args.key)
    dcod.keySetup()
    result = ''
    if (args.message):
        result = dcod.crypt(args.message)
    elif args.stdin:
        message = sys.stdin.buffer.read().decode("utf-8")
        result = dcod.crypt(message)
    elif args.file:
        message = args.file.read().decode("utf-8")
        result = dcod.crypt(message)
    if args.output:
        args.output.write(result.encode('utf-8'))
    else:
        sys.stdout.buffer.write(result.encode('utf-8'))
