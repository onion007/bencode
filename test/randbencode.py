import random, logging

string = "abcdefghijklmnopqrstuvwxyz"

rand = lambda x:random.randint(1,x)

randint = lambda :random.randint(-255,256)
randstr = lambda :string[0:rand(20)]
def randlist(ilen):
    pass

def randdict():
    pass

func_map = dict()
func_map[1] = randint
func_map[2] = randstr
func_map[3] = randlist
func_map[4] = randdict

logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    total = rand(20)
    logging.debug('total={}\n------------------'.format(total))
    result = []
    p = 0
    while total > 0:
        itype = rand(2)
        ret = func_map[itype]()
        logging.debug('type={} {}'.format(itype, ret))
        result.append(ret)
        total -= 1
        p += 1

    print result
