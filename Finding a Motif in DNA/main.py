from functional import seq

def positions(code,s_code):
    n = len(s_code)
    pos = (seq([(i+1) if code[i:i+n] == s_code else None
                        for i in range(len(code))])
                    .filter(lambda x: x is not None)
                    .map(str)
                    )
    return ' '.join(pos)
