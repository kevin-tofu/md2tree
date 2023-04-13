import pathlib
from parse import *
import treelib
import utils

def create_tree(
    node_list: list[dict],
    text_list: list[list[str]],
    text2node: bool = True
) -> treelib.Tree:

    mytree = treelib.Tree()
    mytree.create_node('root', 'root')
    idx_prev = 'root'
    index_list = range(len(node_list))
    # print(node_list)
    depth_prev = node_list[0]['depth']
    _node_list = node_list[1::]

    for i, node, text in zip(index_list[1::], node_list[1::], text_list[1::]):
        idx = str(i)
        # print('node-title:', node)
        # print('text:', text)
        if text2node:
            data = dict(
                title=node['title'],
                objects=str2dict(text)
            )
        else:
            data = dict(
                title=node['title'],
                texts=text
            )
        if depth_prev + 1 <= node['depth']:
            idx_parent = idx_prev

        elif depth_prev >= node['depth']:
            _idx = None
            for j in range(len(_node_list[0:i])-1, -1, -1):
                if _node_list[j]['depth'] < node['depth']:
                    _idx = j+1  #
                    break
            idx_parent = str(_idx) if _idx is not None else 'root'

        else:
            raise ValueError('err')

        mytree.create_node(
            idx,
            idx,
            parent=idx_parent,
            data=data
        )
        depth_prev = node['depth']
        idx_prev = idx

    return mytree


def lines2tree(
    lines: str,
    text2node: bool = True
) -> treelib.Tree:
    
    current_lines = list()
    node_list = list()
    text_list = list()
    
    depth_prev = dict(
        type='heading',
        depth=0,
        text=''   
    )
    node_list.append(depth_prev)

    for i, line in enumerate(lines):

        idx = str(i)
        if node := parse_heading(line):
            # print(node)
            node_list.append(node)
            text_list.append(current_lines)
            current_lines = list()

        else:
            current_lines.append(line)
    
    text_list.append(current_lines)
    mytree = create_tree(
        node_list,
        text_list,
        text2node=text2node
    )
    
    return mytree


def file2tree(
    file_path: pathlib.Path,
    text2node: bool = True
) -> treelib.Tree:
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # print(type(lines), type(lines[0]))
    # for i, line in enumerate(lines):
        # print(i, line)

    return lines2tree(lines, text2node=text2node)


if __name__ == '__main__':
    
    import json
    import pathlib

    path = './README.md'
    mytree1 = file2tree(
        pathlib.Path(path),
        text2node=False
    )
    # mytree1.to_graphviz('./vis')
    # mytree1.save2file('./test.txt')
    parent_id = mytree1.identifier
    for i, n in enumerate(mytree1.all_nodes_itr()):
        print(i, n, n.predecessor(parent_id), n.successors(parent_id))
    
    with open('./test1.json', 'w') as f:
        json.dump(mytree1.to_dict(), f, indent=2)
    with open('./test2.json', 'w') as f:
        json.dump(utils.tree2dict(mytree1, 'root'), f, indent=2)

    print(mytree1)

    depth_list = [0, 1, 1, 2, 2, 3, 3, 2, 2, 1, 3, 3, 1, 2, 2]
    node_list = [ dict(depth=d, title='') for d in depth_list]
    index_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    text_list = [ [''] for _ in range(len(node_list))]
    mytree2 = create_tree(node_list, text_list)
    print(mytree2)

    mytree1_dict = utils.tree2dict(mytree2, 'root')
    with open('./test3.json', 'w') as f:
        json.dump(mytree1_dict, f, indent=2)