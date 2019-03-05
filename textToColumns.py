import sys
import os.path


def text_to_columns(fname, col):
    col = int(col)
    if not os.path.isfile(fname):
        return "File does not exist !"
    if os.path.getsize(fname) == 0:
        return "File is empty !"
        
    # read the file to a list
    lines = []
    with open(fname, 'r') as f:
        for line in f:
            lines.append(line.replace('\n', ''))
    
    # separate the list in columns using col value
    columns = dict()
    for index, value in enumerate(lines):
        try:
            columns[index % col].append(value)
        except KeyError:
            columns[index % col] = [value]
    
    # rearrange the columns into a file
    output = 'c:/temp/output.csv'
    length = len(columns[0])
    with open(output, 'w') as outfile:
        for ln in range(length):
            line = []
            for cl in range(col):
                line.append(columns[cl][ln])
            outfile.write(';'.join(line) + '\n')
    return "Your file has been rearranged to %s." % output


if __name__ == '__main__':
    message = text_to_columns(sys.argv[1], sys.argv[2])
    print message
