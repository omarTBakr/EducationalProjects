from classes import CPU
import pytest

@pytest.fixture
def cpu_values():
    return {'name': 'Test',
            'manufacture': 'Test',
            'total': 100,
            'allocated': 50 ,
            'cores':10 ,
            'power_watts' :100 ,
            'sockets':3}

@pytest.fixture
def cpu(cpu_values):
    return CPU(**cpu_values)


def test_create_cpu(cpu,cpu_values):
    for key ,value in cpu_values.items():
        assert getattr(cpu,key) == value

@pytest.mark.parametrize(
    'cores , exception', [(-1 , ValueError), (1.1 , TypeError) , (0, ValueError)])
def test_invalid_cores(cores, exception , cpu_values ):
    with pytest.raises(exception):
        cpu_values['cores'] = cores
        CPU(**cpu_values)

@pytest.mark.parametrize(
    'sockets , exception', [(-1 , ValueError) , (1.1 , TypeError) , (0,ValueError)]
)

def test_invalid_sockets(sockets , exception, cpu_values):

    with pytest.raises(exception):
        cpu_values['sockets'] = sockets
        CPU(**cpu_values)



@pytest.mark.parametrize(
    'power_watts , exception', [(-1 , ValueError) , (1.1 , TypeError) , (0,ValueError)]
)

def test_invalid_pwer_watts(power_watts , exception, cpu_values):

    with pytest.raises(exception):
        cpu_values['power_watts'] = power_watts
        CPU(**cpu_values)
