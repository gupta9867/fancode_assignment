from datetime import datetime
import pytest

def init_report():
    pytest_html = None  # Placeholder for the report initialization (pytest-html handles reporting)

def create_test(test_name):
    return test_name

def flush_report():
    pass  # pytest-html automatically manages the report flushing after the tests
