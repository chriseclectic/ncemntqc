"""
Utility functions for saving and loading Qiskit objects to JSON files.
"""

import json
from datetime import datetime

from qiskit.result import Result
from qiskit.providers.models import BackendProperties


class QiskitEncoder(json.JSONEncoder):
    """A JSON encoder for Qiskit objects."""

    def default(self, obj):
        if hasattr(obj, 'tolist'):
            return obj.tolist()
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        if isinstance(obj, datetime):
            return obj.isoformat()
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        return json.JSONEncoder.default(self, obj)

    
def save_to_json(obj, filename):
    """Serialize a Qiskit object to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(obj, file, cls=QiskitEncoder)


def load_properties(filename):
    """Deserialize a BackendProperties object from a JSON file."""
    with open(filename, 'r') as file:
        return BackendProperties.from_dict(json.load(file))

    
def load_result(filename):
    """Deserialize a Result object from a JSON file."""
    with open(filename, 'r') as file:
        tmp = json.load(file)
        if isinstance(tmp, list):
            return [Result.from_dict(i) for i in tmp]
        return Result.from_dict(tmp)
