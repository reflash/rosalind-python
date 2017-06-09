from functional import seq

nucl_order = ['A','C','G','T']

def transpose(x):
    return list(map(list, zip(*x)))

def profile_consensus(data):
    x = data.split('>')
    x.pop(0)
    x = ( seq(x)
            .map(lambda s: s.split())
            .map(lambda s: s[1])
            .map(lambda s: list(s))
            )
    y = seq(transpose(x))
    y = y.map(lambda col: [col.count(k) for k in nucl_order])
    common_ancestor = ''.join(y.map(lambda col: nucl_order[col.index(max(col))]))
    y = transpose(y)
    profile = '\n'.join([ nucl_order[y.index(r)] + ': ' + ' '.join(seq(r).map(str)) for r in y ] )
    return common_ancestor + '\n' + profile
