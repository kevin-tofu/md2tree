
# Convert Markdown to Tree (Dictonary)

 This module is going to convert markdown(.md) file into tree-structure-object.

## Set Up

```bash

poetry add git+https://github.com/kevin-tofu/md2tree.git

```

## Usage

```bash

import md2tree

readme = md2tree.parse_file('README.md')
print(readme)

```

### Functions

| Functions | Description |
| --- | --- |
| parse_file |  |
| parse_liststr |  |
| parse_str |  |
