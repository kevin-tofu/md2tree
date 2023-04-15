

if __name__ == '__main__':
    
    import json
    import pathlib
    import md2tree


    path = './README.md'
    mytree1 = md2tree.file2tree(
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
        json.dump(md2tree.tree2dict(mytree1, 'root'), f, indent=2)

    print(mytree1)

    depth_list = [0, 1, 1, 2, 2, 3, 3, 2, 2, 1, 3, 3, 1, 2, 2]
    node_list = [ dict(depth=d, title='') for d in depth_list]
    index_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    text_list = [ [''] for _ in range(len(node_list))]
    mytree2 = md2tree.create_tree(node_list, text_list)
    print(mytree2)

    mytree1_dict = md2tree.tree2dict(mytree2, 'root')
    with open('./test3.json', 'w') as f:
        json.dump(mytree1_dict, f, indent=2)