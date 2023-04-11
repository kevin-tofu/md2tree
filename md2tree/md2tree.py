import pathlib
from parse import *


def parse_liststr(
    lines: str
) -> list[dict]:
    nodes = list()
    current_node = None
    current_lines = list()

    for line in lines:
        if node := parse_heading(line):
            if current_node:
                current_node['children'] = parse_paragraph(current_lines)
                nodes.append(current_node)
            current_node = node
            current_node['children'] = []
            current_lines = []
        
        elif node := parse_list_item(line):
            if current_node and current_node['type'] != 'list':
                current_node['children'] = parse_paragraph(current_lines)
                nodes.append(current_node)
            if not current_node or current_node['type'] != 'list' or current_node['indent'] != node['indent']:
                current_node = {'type': 'list', 'indent': node['indent'], 'children': []}
                nodes.append(current_node)
            current_node['children'].append(node)
            current_lines = []
        
        # elif node := parse_table(current_lines + [line]):
        #     if current_node:
        #         current_node['children'] = parse_paragraph(current_lines)
        #         nodes.append(current_node)
        #     current_node = node
        #     current_node['children'] = []
        #     current_lines = []

        else:
            current_lines.append(line)

    if current_node:
        current_node['children'] = parse_paragraph(current_lines)
        nodes.append(current_node)

    return nodes


def path2str(file_path: pathlib.Path):
    pass


def parse_file(
    file_path: pathlib.Path
) -> list[str]:
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # print(type(lines), type(lines[0]))
    # for i, line in enumerate(lines):
        # print(i, line)

    return parse_liststr(lines)



if __name__ == '__main__':
    
    import pathlib

    path = './README.md'
    data = parse_file(
        pathlib.Path(path)
    )

    print(data)