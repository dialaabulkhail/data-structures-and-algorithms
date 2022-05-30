
from left_join_hashmap.left_join_hashmap import left_join, HashTable
import pytest

def test_left_join():
    ht1 = HashTable()
    ht2 = HashTable()

    ht1.set('diligent', 'employed')
    ht1.set('fond', 'enamored')
    ht1.set('guide', 'usher')
    ht1.set('outfit', 'garb')
    ht1.set('wrath', 'anger')

    ht2.set('diligent', 'idle')
    ht2.set('fond', 'averse')
    ht2.set('guide', 'follow')
    ht2.set('flow', 'jam')
    ht2.set('wrath', 'delight')


    output = [['wrath', 'anger', 'delight'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse']]
    assert output == left_join(ht1, ht2)


