
def bencode(obj):
    t = type(obj)
    assert t in do_map, E_INVOBJ
    return do_map[t](obj)

encode_str = lambda obj: '{}:{}'.format(len(obj), obj)
encode_int = lambda obj: 'i{}e'.format(obj)
def encode_list(obj):
    es = ''
    for e in obj:
        t = type(e)
        assert t in do_map, E_INVOBJ
        es += do_map[t](e)
    return 'l{}e'.format(es)

def encode_dict(obj):
    pairs = ''
    seq = obj.items()
    seq.sort(key=lambda x: x[0])
    for k,v in seq:
        assert type(k) == str, E_INVOBJ
        pairs += encode_str(k)
        assert type(v) in BEN_TYPE, E_INVOBJ
        t = type(v)
        assert t in do_map, E_INVOBJ
        pairs += do_map[t](v)
    return 'd{}e'.format(pairs)

do_map = dict()
do_map[str] = encode_str
do_map[int] = encode_int
do_map[list] = encode_list
do_map[dict] = encode_dict

E_INVOBJ = 'Invalid object.'
BEN_TYPE = (str, int, list, dict)

