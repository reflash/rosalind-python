def probability(k,m,n):
    sum = k + m + n

    p1 = ( k / sum ) * ( (k - 1) / (sum - 1) )
    p2 = ( k / sum ) * ( m / (sum - 1) )
    p3 = ( k / sum ) * ( n / (sum - 1) )

    p4 = ( m / sum ) * ( k / (sum - 1) )
    p5 = 0.75 * ( m / sum ) * ( (m - 1) / (sum - 1) )
    p6 = 0.5 * ( m / sum ) * ( n / (sum - 1) )

    p7 = ( n / sum ) * ( k / (sum - 1) )
    p8 = 0.5 * ( n / sum ) * ( m / (sum - 1) )
    p9 = 0 # n n always homozygous recessive

    return round( p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9, 5 )
