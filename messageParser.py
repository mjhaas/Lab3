'''
CS2911
Fall 2019
Lab 3
Name:
    Matt Haas
    Joe Skubal
'''

'''
read list
hasNextElement?
read element
read header length
    return length to header (maybe return sentinel for end?)
read number length # of times (send length)
    return characters as byte array? then concatenate

read in first for bytes

'''
with open('file.in') as file:
    fileText = file.read()
    file.close()
print("File Contents follow:")
print(fileText)
message = bytearray.fromhex(fileText)  # DAD\nBOD\n

list_iter = message.__iter__()


def next_byte():
    """
    draws in the next byte of the pre-made message for testing purposes.

    :return: the next byte, as a bytes object with a single byte in it
    :author: Joseph Skubal
    """
    byte = list_iter.__next__()
    return byte.to_bytes(1, 'big')


def read_message():
    '''
    Directs the program, assembling the lines of text that were read in, and sending them to export

    :author: Joseph Skubal
    '''

    lines = ''
    upper_bound = read_header()
    for line in range(0, upper_bound):  # calls next_line() upper_bound times
        lines += next_line() + "\n"  # append next line
    export_string(lines.rstrip())  # remember to strip final trailing \n


def read_header():
    '''
    reads message header bytes to get number of lines in message payload

    :return: The number of lines in the message as an integer
    :author: Joseph Skubal
    '''

    bytes = next_byte()
    for i in range(0, 3):
        bytes += next_byte()
    return int.from_bytes(bytes, "big")


def next_line():
    '''
    read bytes until new line (\n) reached

    :author: Matt Haas
    :return: the next line of text as a string
    '''

    string = ''
    byte = next_byte()
    while byte.decode('ascii') != '\n':
        string += byte.decode()
        byte = next_byte()
    return string


def export_string(string):
    """
    This method runs the exporting tasks, saving the message to a file, and displaying it to the console

    :author: Matt Haas
    :param string: the string to be exported
    """
    print("\nMessage follows:")
    print(string)

    writtenFile = 'output.txt'
    with open(writtenFile, 'w') as file:
        file.write(string)
        file.close()


# Run the program for testing purposes
read_message()
