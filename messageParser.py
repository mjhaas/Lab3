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
print(fileText)

#message = bytearray.fromhex('00 00 00 02 44 41 44 0A 42 4F 44 0A')  # DAD\nBOD\n
message = bytearray.fromhex(fileText)  # DAD\nBOD\n

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
    # print(upper_bound)  # fixme remove after testing
    while len(lines) < upper_bound:
        lines.append(next_line())

    combined = ''
    for element in lines:
        combined += str(element) + "\n"
    export_string(combined.rstrip())  # fixme a bit sloppy to put the whitespace on, then stip it. Revise


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

    string = ''
    byte = next_byte()
    while byte.decode('ascii') != '\n':
    #while byte.decode('ascii') != b'0x0A':
        string += byte.decode()
        byte = next_byte()
    return string


def export_string(string):
    """
    fixme Prints the string to the console
    This method may end up writing the string to a file, or doing
    something so totally tubular, we can't even conceive of it right now.
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
main_controller()
