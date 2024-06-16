from lambda_utils import invoke_lambda


def test_AC_fat_1():
    assert invoke_lambda('fatorial/good/jorge.c', 'fatorial') == "Accepted"

def test_AC_fat_2():
    assert invoke_lambda('fatorial/good/sinayra.c', 'fatorial') == "Accepted"

def test_AC_primos_arrojados_1():
    assert invoke_lambda('primos_arrojados/good/ribas-ac.c', 'primos_arrojados') == "Accepted"


