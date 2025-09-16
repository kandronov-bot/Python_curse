from exercises import *

import random
import pytest
import os

def test_list_to_pow():
    for _ in range(5):
        n = random.randint(1, 50)
        nums = [random.randint(1, 10) for i in range(n)]
        pow = random.randint(1, 10)

        result = list_to_pow(nums, pow)

        assert isinstance(result, list)
        assert len(result) == len(nums)
        assert all(list(map(lambda x: isinstance(x, int), result)))
        for a, b in zip(nums, result):
            assert a**pow == b


def test_naive_encoder():
    assert isinstance(naive_encoder(123), int)
    assert naive_encoder(0) == 0
    assert naive_encoder(1) == 123
    assert naive_encoder(2) == 246
    assert naive_encoder(3) == 369
    assert naive_encoder(4) == 492
    assert naive_encoder(5) == 615
    assert naive_encoder(6) == 738
    assert naive_encoder(7) == 861
    assert naive_encoder(8) == 984
    assert naive_encoder(9) == 1107
    assert naive_encoder(10) == 102030
    assert naive_encoder(11) == 112233
    assert naive_encoder(12) == 122436
    assert naive_encoder(13) == 132639
    assert naive_encoder(14) == 142842


def test_fibonacci_nth():
    assert isinstance(fibonacci_nth(10), int)
    assert fibonacci_nth(1) == 1
    assert fibonacci_nth(2) == 1
    assert fibonacci_nth(3) == 2
    assert fibonacci_nth(5) == 5
    assert fibonacci_nth(10) == 55
    assert fibonacci_nth(500) == 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
    assert fibonacci_nth(1024) == 4506699633677819813104383235728886049367860596218604830803023149600030645708721396248792609141030396244873266580345011219530209367425581019871067646094200262285202346655868899711089246778413354004103631553925405243

    for i in range(10):
        n, m = random.randint(5, 50), random.randint(5, 50)
        assert fibonacci_nth(n + m) == fibonacci_nth(n - 1)*fibonacci_nth(m) + fibonacci_nth(n)*fibonacci_nth(m + 1)


def test_clip_list():
    for _ in range(10):
        N = random.randint(10, 1000)
        iarr = [random.random() for _ in range(N)]
        a_min = random.uniform(0.0, 0.5)
        a_max = random.uniform(0.5, 1.0)
        oarr = clip_list(iarr, a_min, a_max)
        
        assert len(iarr) == len(oarr)
        assert isinstance(oarr[0], float)
        assert all([a_min <= n <= a_max for n in oarr])


def test_input_to_list(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: '')
    assert input_to_list() == []

    monkeypatch.setattr('builtins.input', lambda: '-999')
    assert input_to_list() == [-999]

    monkeypatch.setattr('builtins.input', lambda: '1, 2, 3, 4, 5')
    assert input_to_list() == [1, 2, 3, 4, 5]

    monkeypatch.setattr('builtins.input', lambda: '-1, -2')
    assert input_to_list() == [-1, -2]


def test_income_by_client():
    assert income_by_client([]) == {}

    recs = [('John', 100)]
    expected = {'John': 100}

    assert income_by_client(recs) == expected

    recs = [('John', 100), ('Anna', 251), ('John', 50)]
    expected = {'John': 150, 'Anna': 251}

    assert income_by_client(recs) == expected


def test_add_prefix():
    assert add_prefix([], '') == []
    assert add_prefix([], 'abracadabra') == []
    assert add_prefix(
        ['Digit', 'Letter', 'Character', 'Symbol'], 'Is') ==\
            ['IsDigit', 'IsLetter', 'IsCharacter', 'IsSymbol']
    assert add_prefix(
        ['IsDigit', 'Letter', 'Character', 'Symbol'], 'Is') ==\
            ['IsDigit', 'IsLetter', 'IsCharacter', 'IsSymbol']


def test_hide_secrets():
    assert hide_secrets([]) == []
    assert hide_secrets(['nothing to hide']) == ['nothing to hide']
    assert hide_secrets(['secret', 'top secret', 'not secret']) == []
    assert hide_secrets(['sEcRet', 'top secRET', 'not sercet']) == ['not sercet']
    assert hide_secrets(['sEcRetsecRET', 'top secRET', 'not sercet']) == ['not sercet']


def test_is_same_type():
    assert is_same_type([])
    assert is_same_type(['Hi'])
    assert is_same_type([1, 2, 3, 4, 5])
    assert is_same_type(['Hi', 'Bob'])
    assert not is_same_type([1., 2, 3, 4, 5])

    mas = [1, 2, '3', 'H', 'Hi']
    for _ in range(5):
        mean1 = random.choice(mas)
        mean2 = random.choice(mas)
        assert is_same_type([mean1, mean2]) == (type(mean1) == type(mean2))


def test_file_to_str_list():
    name = 'tmp.txt'
    def check(data):
        with open(name, 'w') as f:
            for l in data:
                f.write(f'{l}')
        try:
            assert file_to_str_list(name) == data
        except:
            os.remove(name)
            raise

    check([])
    check(['a'])
    check(['a\n', 'b\n', 'asdfadf\n', '1232'])
    os.remove(name)
