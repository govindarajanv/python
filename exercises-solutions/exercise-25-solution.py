import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stderr.write('This is stdout text\n')

#This is how we execute custom script
print ("sys.argv =",sys.argv)

#command line arguments,arg 1 is the first argument
if len(sys.argv) > 1:
    print (sys.argv[1])

def main(arg):
    print ("inside main function",arg)


main(sys.argv[0])
    
