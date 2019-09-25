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


'''


def next_byte():
    """
    Read the next byte from the sender, received over the network.
    If the byte has not yet arrived, this method blocks (waits)
      until the byte arrives.
    If the sender is done sending and is waiting for your response, this method blocks indefinitely.

    :return: the next byte, as a bytes object with a single byte in it
    """

