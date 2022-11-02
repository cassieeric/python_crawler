import base64
"""
var d = a("jquery")
      , e = a("support")
      , f = a("constants")
      , g = a("base64")
      , h = "substring"
      , i = "split"
      , j = "replace"
      , k = "substr";
    b.decodeMp4 = {
        getHex: function(a) {
            return {
                str: a[h](4),
                hex: a[h](0, 4)[i]("").reverse().join("")
            }
        },
        getDec: function(a) {
            var b = parseInt(a, 16).toString();
            return {
                pre: b[h](0, 2)[i](""),
                tail: b[h](2)[i]("")
            }
        },
        substr: function(a, b) {
            var c = a[h](0, b[0])
              , d = a[k](b[0], b[1]);
            return c + a[h](b[0])[j](d, "")
        },
        getPos: function(a, b) {
            return b[0] = a.length - b[0] - b[1],
            b
        },
        decode: function(a) {
            var b = this.getHex(a)
              , c = this.getDec(b.hex)
              , d = this[k](b.str, c.pre);
            return g.atob(this[k](d, this.getPos(d, c.tail)))
        }
    };
"""


def getHex(a):
    return {
        "str": a[4:],
        "hex": "".join(list(a[0:4])[::-1])
    }


def getDec(a):
    b = str(int(a, 16))  # b = 6859
    return {
        "pre": list(b[0:2]),
        "tail": list(b[2:])
    }


def substr(a, b):
    c = a[0: int(b[0])]
    d = a[int(b[0]): int(b[0])+int(b[1])]
    return c + a[int(b[0]):].replace(d, '')


def getPos(a, b):
    b[0] = len(a) - int(b[0]) - int(b[1])
    return b


def to_16(data):
    pad = 16 - len(data) % 16
    data += pad * chr(pad)
    return data


def decode(a):
    b = getHex(a)
    # print(b)
    c = getDec(b['hex'])  # {'pre': ['6', '8'], 'tail': ['5', '9']}
    # print(c)
    d = substr(b['str'], c['pre'])
    # print(d)
    origStr = substr(d, getPos(d, c['tail']))
    missing_padding = 4 - len(origStr) % 4
    if missing_padding:
        origStr += '=' * missing_padding
    print(len(origStr))
    return str(base64.b64decode(origStr).decode())


if __name__ == '__main__':
    with open('dataSrc.txt', 'r', encoding='utf-8') as f:
        for dataSrc in f.readlines():
            print(dataSrc.strip())
            try:
                print(decode(dataSrc.strip()))
                result = decode(dataSrc.strip())
                with open("decoded_dataSrc.txt", 'a', encoding='utf-8') as f:
                    f.write("http:" + result + '\n')
            except:
                pass


