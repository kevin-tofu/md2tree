import re
from typing import Optional

def parse_heading(line: str) -> Optional[dict]:
    match = re.match(r'^(#+)\s+(.*)$', line)
    if match:
        level = len(match.group(1))
        text = match.group(2)
        return {'type': 'heading', 'level': level, 'text': text}
    else:
        return None


def parse_list_item(line: str) -> Optional[dict]:
    match = re.match(r'^(\s*)[*+-]\s+(.*)$', line)
    if match:
        indent = len(match.group(1))
        text = match.group(2)
        return {'type': 'list_item', 'indent': indent, 'text': text}
    else:
        return None


def parse_paragraph(lines: list[str]) -> dict:
    # print(type(lines[0]))
    text = '\n'.join(lines).strip()
    return {'type': 'paragraph', 'text': text}


def parse_table(lines: list[str]) -> Optional[dict]:
    if len(lines) < 3:
        return None

    header = [cell.strip() for cell in lines[0].strip('|').split('|')]
    divider = [cell.strip() for cell in lines[1].strip('|').split('|')]

    # Ensure that the divider contains only dashes or pipes
    if any(c not in '-| ' for cell in divider for c in cell):
        return None

    # Ensure that the number of cells in the header and divider are the same
    if len(header) != len(divider):
        return None

    # Store the table data in a dictionary
    rows = []
    for row in lines[2:]:
        cells = [cell.strip() for cell in row.strip('|').split('|')]
        # Ensure that all rows have the same number of cells as the header
        if len(cells) != len(header):
            return None
        rows.append(cells)

    return {'type': 'table', 'header': header, 'rows': rows}


