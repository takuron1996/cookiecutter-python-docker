#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""テストで共通のfixture."""

from pytest_bdd import parsers, then


@then(parsers.parse("戻り値が{expected}"))
def assert_expected(expected, actual):
    """戻り値の判定.

    Args:
        expected: 予想の値
        actual: 実際の値
    """
    assert expected == actual
