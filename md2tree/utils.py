import json
import treelib

def tree2dict(tree:treelib.Tree, root_node_name: str='root') -> dict:
    tree_id = tree.identifier
    node = tree[root_node_name]
    n_children = node.successors(tree_id)
    d = dict(
        name=node.identifier,
        data=node.data,
        children=list()
    )
    for nc_name in n_children:
        d['children'].append(
            tree2dict(tree, nc_name)
        )
    
    return d

def tree2file(
    path_export: str,
    tree:treelib.Tree,
    root_node_name: str='root',
    indent: int=2
):
    with open(path_export, 'w') as f:
        json.dump(tree2dict(tree, root_node_name), f, indent=indent)
