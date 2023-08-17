import Testes_Validacao as tests

def testes():

    print('bateria testes de validacao em locadora:')

    print('testes com tuplas validas:')

    for i in range(1,11):
        print('teste: '+str(i))
        tests.test_valid_locadora()
        print('\n')

    print('fim dos testes com tuplas validas! \n')

testes()
