#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module for Lowest_Common_Ancestor_in Binary Search Tree function.
Author: Safia Gibril
Created on: 2.1.2025
"""


class TreeNode:
    """Define class for TreeNode"""

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lowestCommonAncestor(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    r"""
    Finds the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree.

    In a Binary Search Tree, the Lowest Common Ancestor between two nodes p and q is the lowest node
    such that both p and q are descendants of this node (a node can be a descendant of itself).

    Args:
        root (TreeNode): The root node of the Binary Search Tree.
        p (TreeNode): The first node in the tree.
        q (TreeNode): The second node in the tree.

    Returns:
        TreeNode: The Lowest Common Ancestor of nodes p and q.

    Raises:
        ValueError: If any of the inputs (root, p, or q) is None.

    Notes:
        - If both p and q are smaller than the current node, the LCA is in the left subtree.
        - If both p and q are larger than the current node, the LCA is in the right subtree.
        - Otherwise, the current node is the LCA.

    Examples:
        Example 1:
            Input: root = [5,3,8,1,4,7,9,null,2], p = TreeNode(3), q = TreeNode(8)
            Output: TreeNode(5)

        Example 2:
            Input: root = [5,3,8,1,4,7,9,null,2], p = TreeNode(3), q = TreeNode(4)
            Output: TreeNode(3)
    
    Example:
    Tree Structure:
            5
          /   \\
         3     8
        / \   / \\
       1   4 7   9
        \\
         2

        Example 1:
        Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
        Output: 5
        
        Example 2:
        Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
        Output: 3
    """

    # Check if root, p, or q are None and raise ValueError if so
    if root is None or p is None or q is None:
        raise ValueError("None of the inputs (root, p, q) can be None.")

    candidate = root
    # this tree satisfies BST properties
    while candidate:
        if p.value > candidate.value and q.value > candidate.value:
            candidate = candidate.right
        elif p.value < candidate.value and q.value < candidate.value:
            candidate = candidate.left
        else:
            return candidate
