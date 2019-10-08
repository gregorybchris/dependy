from dependy.logging import logging_utilities


def test_log_context():
    @logging_utilities.log_context('name', context_tag='tag')
    def test_func(a):
        assert a == 4

    test_func(5)
