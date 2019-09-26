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

message = bytearray.fromhex('00 00 00 02 44 41 44 0A 42 4F 44 0A')  # DAD\nBOD\n
list_iter = message.__iter__()


def next_byte():
    """
    Read the next byte from the sender, received over the network.
    If the byte has not yet arrived, this method blocks (waits)
      until the byte arrives.
    If the sender is done sending and is waiting for your response, this method blocks indefinitely.

    :return: the next byte, as a bytes object with a single byte in it
    :author: Joseph Skubal
    """
    byte = list_iter.__next__()
    print(byte)
    return byte.to_bytes(1, 'big')


def main_controller():
    '''
    Directs the program, assembling the lines of text that were read in.

    :author: Joseph Skubal
    '''

    # Joseph Skubal wuz here
    lines = list()
    upper_bound = read_header()
    print(upper_bound)  # fixme remove after testing
    while len(lines) < upper_bound:
        lines.append(next_line())
    export_string(str(lines))


def read_header():
    '''
    reads message header line to get number of lines in file

    :return: Then number of lines in the rest of the file as an integer
    :author: Joseph Skubal
    '''

    # Jospeh Skubal wuz here
    bytes = next_byte()
    for i in range(0, 3):
        bytes += next_byte()
    print(bytes)  # fixme remove after testing
    return int.from_bytes(bytes, "big")


def convert_bytes():
    '''
    handles byte to string conversion

    :return:
    '''


def next_line():
    '''
    read bytes until new line reached


    read byte
    convert to ascii
    if newline
        stop
        return string of converted bytes
    :return:
    '''


def export_string(string):
    """
    fixme Prints the string to the console
    This method may end up writing the string to a file, or doing
    something so totally tubular, we can't even conceive of it right now.

    :param string: the string to be exported
    """
    print(string)



#Run the program for testing purposes
main_controller()
