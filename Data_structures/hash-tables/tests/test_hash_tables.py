from hash_tables.hashtables import HashTable
import pytest

def test_hash_method():
    hash_table = HashTable()
    assert 899 == hash_table.hash("hi")
    assert 683 == hash_table.hash("dream")
    assert 683 == hash_table.hash("derma")
    assert 892 == hash_table.hash("heart")
    assert 320 == hash_table.hash("true")



def test_set_method():
    hash_table = HashTable()
    test = hash_table.set("welcome", "home")
    for i in enumerate(hash_table.map):
        if i == ["welcome","home"]:
            return True
        else:
            return False
    assert True == hash_table.map



def test_get_method():
    hash_table = HashTable()
    hash_table.set("hello", "world")
    hash_table.set("new", "york")
    assert "world" == hash_table.get("hello")
    assert "york" == hash_table.get("new")



def test_contains_method():
    hash_table = HashTable()
    hash_table.set("hello", "world")
    hash_table.set("new", "york") 

    with pytest.raises(Exception):
        hash_table.contains("happy")




