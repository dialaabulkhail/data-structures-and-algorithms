from stack_queue_brackets.stack_queue_brackets import Stack, validate_brackets


def test_valid_brackets():
    assert True == validate_brackets('{}')
    assert True == validate_brackets('{}(){}')
    assert True == validate_brackets('()[[Extra Characters]]')
    assert True == validate_brackets('(){}[[]]')
    assert True == validate_brackets('{}{Code}[Fellows](())')
   
def test_invalid_brackets():
    assert False == validate_brackets('[({}]')
    assert False == validate_brackets('(](')
    assert False == validate_brackets('{(})')

def test_edge_cases():
    assert False == validate_brackets(')')
    assert False == validate_brackets('{')
    assert False == validate_brackets('[}')



