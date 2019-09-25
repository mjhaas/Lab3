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

def convert_bytes():
    '''
    handles byte to int conversion

    :return:
    '''

def nextLine():
    '''
    read bytes until new line reached


    read byte
    convert to ascii
    if newline
        stop
        return string of converted bytes
    :return:
    '''

