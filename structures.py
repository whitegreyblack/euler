# data structures
# cli to access different data structure properties

import textwrap
import click
from collections import namedtuple

ds = namedtuple("DataStructure", "name description properties characteristics")
"""
class DataStructure(object):
    def __init__(self, name, alts, description):
        self.name = name
        self.alt_names = alts
        self.desc = description
"""
def build_structs():
    yield ds("B-tree", 
"""
A B-tree is a self-balancing tree data structure that maintains sorted data
and allows searches, sequential access, insertions and deletions in
logarithmic time. The B-tree is a generalization of a binary search tree in
that a node can have more than two children. Unlike other self-balancing
binary search trees, the B-tree is well suited for storage systems that read
and write relatively large blocks of data, such as discs. It is commonly used
in databases and filesystems."""[1:], None, None)
    yield ds("B+tree", 
"""
A B +tree is an N-ary tree with a variable but often large number of children
per node. A B+tree consists of a root, internal nodes, and leaves. The root
may be iether a leaf or a node with two or more children. A B+tree can be
viewed as a B-tree in which each node contains only keys (not key-value
pairs), and to which an additional level is added at the bottom with linked
leaves. The primary value of a B+tree is in storing data for efficient
retrieval in a block-oriented storage context - in particular, filesystems.
This is primarily because unlike binary search trees, B+tree have a very
high fanout (number of pointers to child nodes in a node, typically on the
order of 100 or more), which reduces the number of I/O operations required
to find an element in the tree."""[1:], 
"""
The order, or branching factor, 'b' of a B+tree measures the capacity of nodes
(i.e., the number of children nodes) for internal nodes in the tree. The actual
number of children for a node, referred to here as m, is constrained for
internal nodes so that [b/2] <= m <= b. The root is an exception: it is allowed
to have as few as two children. For example, if the order of a B+tree is 7,
each internal node (except for the root) may have between 4-7 children; The
root may have between 2 and 7. Leaf nodes have no children, but are constrained
so that the number of keys must be at least ['b'/2] and at most 'b'. In the
situation where a B+tree is nearly empty, it only constains one node, which is
a leaf node. (The root is also the single leaf, in this case.) This node is
permitted to have as little as one key if necessary and at most 'b'-1."""[1:],
"""
For a 'b'-order B+tree with 'h' levels of index:
    n = number of records:
        max(n) = b^h - b^(h-1)
        min(n) = 2 * ceil(b/2)^(h-1) - 2 * ceil(b/2)^(h-2)
    k = number of keys:
        max(k) = b^h - 1
        min(k) = 2 * ceil(b/2)^(h-1) - 1
    Space Complexity:
        O(n)
    Insert:
        O(log_b(n))
    Search:
        O(log_b(n))
    Delete (previously located):
        O(log_b(n))
    Range query:
        O(log_b(n) + k)"""[1:])

def replace(string, pattern='\n', replace=' '):
   return string.replace(pattern, replace)

def wrap(string, width):
    wrapped_lines = textwrap.wrap(string, width=width)
    return '\n'.join(wrapped_lines)

def indent(string, dent):
    # only used for printing available data structures for quering
    dent_str = ' ' * dent
    return '\n' + '\n'.join(dent_str + s for s in string.split(','))

@click.command()
@click.argument('struct')
@click.option('--maxlen', 'maxlen', help="Width of a single line of text", default=80)
def main(struct, maxlen=80):
    structs = { s.name.lower(): s for s in list(build_structs()) }
    message = None
    if struct.lower() in structs.keys():
        s = structs[struct]
        # format long strings. Remove newlines to create a continuous string
        desc = ''
        if s.description:
            d = replace(s.description)
            desc = '\n' + 'Description:' + '\n' + wrap(d, maxlen)
        prop = ''
        if s.properties:
            p = replace(s.properties)
            prop = '\n' + 'Properties:' + '\n' + wrap(p, maxlen)
        chars = ''
        if s.characteristics:
            chars = '\n' + 'Characteristics:' + '\n' + s.characteristics
        message = s.name + desc + prop + chars
    else:
        available = indent(','.join(structs.keys()), dent=2)
        message = f"Data structure {struct} not found. Available queries: {available}"
    print(message)

if __name__ == "__main__":
    main()
