import os, sys
_path = os.path.abspath('../../')
sys.path.append(_path)
from bencode import bencode, bdecode

def bdecode_test(fname):
    with open(fname) as f:
        torrent_dict = bdecode(f.read())
    return torrent_dict

def bencode_test(torrdict):
    return bencode(torrdict)

if __name__ == '__main__':
    fname = 'test.torrent'
    torrdict = bdecode_test(fname)
    assert bencode_test(torrdict) == open(fname).read()
