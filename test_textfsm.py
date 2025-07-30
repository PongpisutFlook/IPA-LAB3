import pytest
from textfsmlab import config

def test_s1():
    result = config('172.31.124.3')
    assert result['Gig 0/0'] == "Connect to G0/3 of S0"
    assert result['Gig 0/1'] == "Connect to G0/2 of R2"
    assert result['Gig 0/2'] == "Connect to PC"

def test_r1():
    result = config('172.31.124.4')
    assert result['Gig 0/0'] == "Connect to G0/1 of S0"
    assert result['Gig 0/1'] == "Connect to PC"
    assert result['Gig 0/2'] == "Connect to G0/1 of R2"

def test_r2():
    result = config('172.31.124.5')
    assert result['Gig 0/0'] == "Connect to G0/2 of S0"
    assert result['Gig 0/1'] == "Connect to G0/2 of R1"
    assert result['Gig 0/2'] == "Connect to G0/1 of S1"
    assert result['Gig 0/3'] == "Connect to WAN"