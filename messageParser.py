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


def next_byte():
    """
    Read the next byte from the sender, received over the network.
    If the byte has not yet arrived, this method blocks (waits)
      until the byte arrives.
    If the sender is done sending and is waiting for your response, this method blocks indefinitely.

    :return: the next byte, as a bytes object with a single byte in it
    """


def main_controller():
    '''
    handles calls to next byte
    :return:
    '''
    '''
    string = []
    upper bound = read_header()
    while lineIndex < upper bound:
        string += nextLine()
        increment lineIndex
        
    print(string)
    '''

def read_header():
    '''
    reads header line to get number of lines
    :return: int
    '''

    bytes = next_byte()
    for i in range (1,3):
        bytes += next_byte()
    return int.fromBytes(bytes, "big")

def next_line():
    '''
    read bytes until new line reached

    read byte
    convert to ascii
    if newline
        stop
        converted bytes containing ascii characters from file
        return string of converted bytes
    :return:
    '''
    string = []
    byte = next_byte()
    while byte.decode('ascii') != '\n':
    #while byte.decode('ascii') != b'0x0A':
        string += byte.decode()
        byte = next_byte()
    return string + '\n'
