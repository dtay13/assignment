#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:05:33 2019

@author: dtay
"""
import math

def expected(M,N):
    assert type(M) is int
    assert type(N) is int
    # Termination condition when M = 1
    if M==1:
        expectM = sum(range(1, N+1))/N
        return expectM
    else:
        # Calculate lowest number we will accept on the M-th row
        # This depends on the expected(M-1,N)
        lowest_acceptable = int(math.ceil(expected(M-1,N)))
        # Expected M-th roll income.. Note: I used the Arithimetic Progression formula here
        S = (N-lowest_acceptable+1)*(lowest_acceptable+N)/2 # sum from lowest_acceptable to N
        expectM = (1/N)*S + (lowest_acceptable-1)/N*(expected(M-1,N))
        return expectM

"""
expected(2,6)
# 4.25

expected(3,6)
# 4.666666666666666

expected(4,6)
# 4.944444444444444
"""