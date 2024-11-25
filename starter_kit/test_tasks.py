from autonity import networks
from web3 import Web3

from .tasks import Task, tasks


def pytest_generate_tests(metafunc):
    if "task" in metafunc.fixturenames:
        metafunc.parametrize("task", tasks, ids=[task.__name__ for task in tasks])


def test_task(task: Task):
    w3 = Web3(networks.piccadilly.http_provider)
    task(w3)
