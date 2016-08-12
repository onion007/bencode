import logging,sys

def bencode_error():
    print 'Error: Invalid data'
    exit(1)

def int_decode(source):
    logging.debug('Function: {}'.format(sys._getframe().f_code.co_name))
    data = source['data']
    source['p'] += 1
    start = source['p']
    while data[source['p']] != 'e':
        source['p'] += 1
    source['p'] += 1
    return int(data[start:source['p']-1])

def int_encode(source):
    pass

def str_decode(source):
    logging.debug('Function: {}'.format(sys._getframe().f_code.co_name))
    data = source['data']
    istart = source['p']
    while data[source['p']] != ':':
        source['p'] += 1
    slen = int(data[istart:source['p']])
    source['p'] += 1
    sstart = source['p']
    source['p'] += slen
    return data[sstart:source['p']]

def str_encode(source):
    pass

def list_decode(source):
    logging.debug('Function: {}'.format(sys._getframe().f_code.co_name))
    ret = list()
    data = source['data']
    source['p'] += 1
    while data[source['p']] != 'e':
        op = data[p]
        try:
            v = decode_func[op](source)
            ret.append[v]
        except KeyError:
            bencode_error()
    source['p'] += 1
    return ret

def dict_decode(source):
    logging.debug('Function: {}'.format(sys._getframe().f_code.co_name))
    ret = dict()
    data = source['data']
    source['p'] += 1
    while data[source['p']] != 'e':
        try:
            op = data[source['p']]
            k = decode_func[op](source)
            op = data[source['p']]
            v = decode_func[op](source)
            ret[k] = v
        except KeyError:
            bencode_error()
    source['p'] += 1
    return ret

def dict_encode(source):
    pass

def bencode(source):
    'bencode encode fucntion'
    logging.debug('bencode function.')

def bdecode(source):
    'bencode decode fucntion'
    logging.debug('bdecode function.')
    logging.debug('data:>>>\n[{}]'.format(source))
    data = {
            'data': source,
            'p'   : 0
            }
    return dict_decode(data) if source[0] == 'd' else bencode_error()

decode_func = {
        'i': int_decode,
        'l': list_decode,
        'd': dict_decode
        }
decode_func.update({str(x):str_decode for x in range(10)})
