
def bdecode(seq):
    p = 0
    v = seq[p]
    assert v in do_map, E_INVSEQ
    p, part = do_map[v](seq, p)
    return part

def decode_str(seq, p):
    i_colon = seq.find(':', p)
    str_len = int(seq[p:i_colon])
    p = i_colon + str_len + 1
    part = seq[i_colon+1:p]
    return p, part

def decode_int(seq, p):
    p += 1
    part = ''
    while seq[p] != 'e':
        part += seq[p]
        p += 1
    p += 1
    return p, int(part)

def decode_list(seq, p):
    part = list()
    p += 1 
    while seq[p] != 'e':
        v = seq[p]
        assert v in do_map, E_INVSEQ
        p, element = do_map[v](seq, p)
        part.append(element)
    p += 1
    return p, part

def decode_dict(seq, p):
    part = dict()
    p += 1
    while seq[p] != 'e':
        v = seq[p]
        assert v.isdigit(), E_INVSEQ
        p, key = decode_str(seq, p)
        v = seq[p]
        assert v in do_map, E_INVSEQ
        p, value = do_map[v](seq, p)
        part[key] = value
    p += 1
    return p, part

# decode_x(seq, p) -> p, x
do_map = dict()
for x in range(10):
    do_map[str(x)] = decode_str
do_map['i'] = decode_int
do_map['l'] = decode_list
do_map['d'] = decode_dict

E_INVSEQ = 'Invalid sequence.'

