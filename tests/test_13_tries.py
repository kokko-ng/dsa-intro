"""
Tests for Topic 13: Tries
"""
import pytest
from conftest import get_solution


class TestImplementTrie:
    def test_trie_basic(self):
        f = get_solution("implement_trie")
        Trie = f()
        trie = Trie()
        trie.insert("apple")
        assert trie.search("apple") == True
        assert trie.search("app") == False
        assert trie.startsWith("app") == True
        trie.insert("app")
        assert trie.search("app") == True


class TestWordSearchII:
    def test_word_search_basic(self):
        f = get_solution("word_search_ii")
        board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        words = ["oath", "pea", "eat", "rain"]
        result = set(f(board, words))
        assert result == {"eat", "oath"}

    def test_word_search_single(self):
        f = get_solution("word_search_ii")
        board = [["a"]]
        assert f(board, ["a"]) == ["a"]


class TestAddAndSearchWord:
    def test_search_basic(self):
        f = get_solution("add_and_search_word")
        WordDictionary = f()
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")
        assert wd.search("pad") == False
        assert wd.search("bad") == True
        assert wd.search(".ad") == True
        assert wd.search("b..") == True


class TestReplaceWords:
    def test_replace_basic(self):
        f = get_solution("replace_words")
        assert f(["cat", "bat", "rat"], "the cattle was rattled by the battery") == "the cat was rat by the bat"


class TestLongestWord:
    def test_longest_basic(self):
        f = get_solution("longest_word")
        assert f(["w", "wo", "wor", "worl", "world"]) == "world"

    def test_longest_multiple(self):
        f = get_solution("longest_word")
        result = f(["a", "banana", "app", "appl", "ap", "apply", "apple"])
        assert result in ["apple", "apply"]


class TestMapSum:
    def test_mapsum_basic(self):
        f = get_solution("map_sum")
        MapSum = f()
        ms = MapSum()
        ms.insert("apple", 3)
        assert ms.sum("ap") == 3
        ms.insert("app", 2)
        assert ms.sum("ap") == 5
