#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム"""
from pytest_bdd import scenarios, when

from {{cookiecutter.module}} import example

scenarios(
    "../features/{{cookiecutter.module}}/example.feature",
)

@when("main関数を実施", target_fixture="actual")
def actual():
    """関数を実施.

    Returns:
        テストしたい関数の戻り値
    """
    return example.main()


