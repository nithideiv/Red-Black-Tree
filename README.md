# Red-Black Tree Implementation

## Overview

In this lab, the focus is on implementing a red-black tree based on the given rules:
- Nodes are either red or black.
- Every leaf counts as black.
- If a node is red, then both of its children are black.
- Every simple path from a node to a descendant leaf contains the same number of black nodes.
- The root node is always black.

The project requires extending the functionality of a provided skeleton code `rb_tree.py`, implementing methods for balanced insertions and deletions while adhering to red-black tree rules.

## Data Structures

### Red-Black Tree Methods

#### `print_with_colors(self, curr_node)`

Prints the tree with color codes (‘B’ for black, ‘R’ for red) alongside the nodes in preorder traversal format. Aids in debugging.

#### `left_rotate(self, curr_node)`

Performs a left rotation on the current node according to the specified algorithm.

#### `right_rotate(self, curr_node)`

Performs a right rotation on the current node according to the specified algorithm.

#### `insert(self, data)`

Inserts a node into the red-black tree, maintaining the tree's balance by performing necessary rotations and recolorings.

#### `delete(self, data)`

Deletes a node from the red-black tree, ensuring the tree remains balanced by performing required rotations.

