"""Fixtures compartilhadas para os testes da API."""

import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

# Snapshot do estado inicial, capturado uma única vez na importação do módulo.
_INITIAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restaura o banco em memória antes de cada teste para garantir isolamento."""
    activities.clear()
    activities.update(copy.deepcopy(_INITIAL_ACTIVITIES))
    yield


@pytest.fixture
def client():
    return TestClient(app)
