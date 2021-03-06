import itertools
from functional.pipeline import Sequence
from neo4j.v1 import GraphDatabase, Driver
from functional import seq
from typing import List

driver = None

def connect()->Driver:
    global driver
    uri = "bolt://127.0.0.1:7687"
    if not driver:
        driver = GraphDatabase.driver(uri, auth=("testuser", "testuser"))
    return driver

def add_node(name:str)->None:
    with connect().session() as session:
        session.run("CREATE (a:Node {name:{name}})", name=name)

def add_edge(n1:str, n2:str)->None:
    with connect().session() as session:
        session.run("MATCH (n1:Node),(n2:Node) WHERE n1.name = {n1} AND n2.name = {n2} CREATE (n1)-[r:CONNECTED]->(n2)", n1=n1, n2=n2)


def clear_nodes()->None:
    with connect().session() as session:
        session.run("MATCH (n) DETACH DELETE n")

def transpose(l:List)->List:
    return list(map(list, zip(*l)))


def fasta_read(data: str) -> Sequence:
    x = data.strip().split('>')
    x.pop(0)

    return seq(x) \
            .map(lambda s: s.split()) \
            .map(lambda s: (s.pop(0), ''.join(s)))


def overlap_graph(k: int, data: str) -> str:
    original = fasta_read(data)

    clear_nodes()
    list(original.map(lambda s: add_node(s[0][9:])))

    suffixes = original.map(lambda s: s[1][-k:])
    prefixes = list(original.map(lambda s: s[1][:k]))

    res = []
    leng = suffixes.len()
    for i in range(leng):
        p = itertools.repeat(prefixes[i], leng)
        row = list(suffixes.zip(p).map(lambda x: x[0] == x[1]))
        # clear diagonal
        row[i] = False
        res.append(row)

    edg = []
    original_list = list(original)
    res = transpose(res)
    for i in range(len(res)):
        row = res[i]
        n1 = original_list[i][0][9:]
        edges = list(filter(lambda x: x[1], zip(map(lambda x: x[0][9:], original_list), row)))
        list(map(lambda e: add_edge(n1, e[0]), edges))
        edg.extend(list(map(lambda x: 'Rosalind_' + n1 + ' Rosalind_' + x[0], edges)))

    return '\n'.join(edg)
