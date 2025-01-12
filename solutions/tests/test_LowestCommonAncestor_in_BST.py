#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for Lowest Common Ancestor in Binary Search Tree function.
Author: Safia Gibril
Created on: 2.1.2025
"""

import unittest

from solutions.LowestCommonAncestor_in_BST import lowestCommonAncestor


class TreeNode:
    """Define class for TreeNode"""

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TestLowestCommonAncestor(unittest.TestCase):
    """Test the Lowest Common Ancestor in Binary Search Tree function.

    Binary Search Tree structure:

            5
          /   \\
         3     8
        / \   / \\
       1   4 7   9
        \\
         2
    """

    def setUp(self):
        """Construct Binary Search Tree from the example."""
        self.root = TreeNode(5)
        self.root.left = TreeNode(3)
        self.root.right = TreeNode(8)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(4)
        self.root.right.left = TreeNode(7)
        self.root.right.right = TreeNode(9)
        self.root.left.left.right = TreeNode(2)

    # Basic cases
    def test_level_1(self):
        """Test LCA of node 3 and node 8 on the same level"""
        p = self.root.left
        q = self.root.right
        candidate = lowestCommonAncestor(self.root, p, q)
        self.assertEqual(candidate.value, 5)

    def test_different_levels_case_1(self):
        """Test LCA for node 2 and node 9 on different levels"""
        p = self.root.left.left.right
        q = self.root.right.right
        candidate = lowestCommonAncestor(self.root, p, q)
        self.assertEqual(candidate.value, 5)

    def test_different_levels_case_2(self):
        """Test LCA for node 1 and node 2 on different levels"""
        p = self.root.left.left.right
        q = self.root.left.left
        candidate = lowestCommonAncestor(self.root, p, q)
        self.assertEqual(candidate.value, 1)

    def test_different_levels_case_3(self):
        """Test LCA for node 3 and node 7 on different levels"""
        p = self.root.left.left
        q = self.root.right.left
        candidate = lowestCommonAncestor(self.root, p, q)
        self.assertEqual(candidate.value, 5)

    def test_different_levels_case_4(self):
        """Test LCA for node 7 and node 9 on different levels"""
        p = self.root.right.left
        q = self.root.right.right
        candidate = lowestCommonAncestor(self.root, p, q)
        self.assertEqual(candidate.value, 8)

    def test_different_levels_root_2(self):
        """Test LCA for root 5 and node 7 on different levels"""
        p = self.root
        q = self.root.right.left
        candidate = lowestCommonAncestor(self.root, p, q)
        self.assertEqual(candidate.value, 5)

    # Edge cases
    def test_ancestor_is_the_node_itself(self):
        """Test LCA where the ancestor is one of the nodes itself (3, 4)"""
        p = self.root.left
        q = self.root.left.right
        candidate = lowestCommonAncestor(self.root, p, q)
        self.assertEqual(candidate.value, 3)

    # AssertionError test cases
    def test_assertion_error_root_none(self):
        """Test when root is None"""
        with self.assertRaises(ValueError):
            lowestCommonAncestor(None, self.root.left, self.root.right)

    def test_assertion_error_p_none(self):
        """Test when p is None"""
        with self.assertRaises(ValueError):
            lowestCommonAncestor(self.root, None, self.root.right)

    def test_assertion_error_q_none(self):
        """Test when q is None"""
        with self.assertRaises(ValueError):
            lowestCommonAncestor(self.root, self.root.left, None)
