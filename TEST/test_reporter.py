import pytest
import sys
import os

from EMERCENCIES.MODULE.Reporter import ReporterInfo, ReporterRole

def test_valid_non_anonymous_with_callback():
    person = ReporterInfo(
        role=ReporterRole.VICTIM,
        name="Do Minh Triet",
        phone_number="0388550712",
        allow_call_back = True
    )

    info = person.getReporterInfo()

    assert info["role"] == ReporterRole.VICTIM
    assert info["name"] == "Do Minh Triet"
    assert info["phone_number"] == "0388550712"
    assert info["allow_call_back"] is True
    
    

