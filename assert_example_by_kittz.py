

def test_substring(full_string, substring) :
    assert substring in full_string, "expected '{}' to be substring of '{}'".format(substring,full_string)


test_substring("Привет, меня зовут Катя", "Катя9")