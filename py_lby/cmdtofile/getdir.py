#! python3

def getdir():
    try:
        dirname = open('d:\\directoryfile.txt').read()
    except IOError:
        print('No such filename.')
        dirname = input('Please input the directory name:')
        f = open('d:\\directoryfile.txt', 'w')
        f.write(dirname)
        f.close()
        print('Directory name has been written in d:\\directoryfile.txt.')
        pass
    else:
        print('We have got directory name', dirname, 'in d:\\directoryfile.txt.')
        pass
    return dirname

def test():
    getdir()

if __name__ == '__main__':
    test()
