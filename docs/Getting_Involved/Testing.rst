Testing
=======

You can help us testing coala in several ways.

Executing our Tests
-------------------

coala has a big test suite. It is meant to work on every platform on
every PC. If you just execute our tests you are doing us a favor.

To run tests, you first need to install some dependencies. This can be
done by executing ``pip3 install -r test-requirements.txt``.
You can execute our tests with ``py.test`` or ``python3 -m pytest``
and report any errors you get!

If you need more options about allowing skipped tests, getting code
coverage displayed or omitting/selecting tests, just query
``py.test --help``.

    **Note:**
    You will not get a test coverage of 100% - the coverage on the
    website is merged for several python versions.

Using test coverage
-------------------

To get coverage information, you can run ``py.test --cov``. You can
view the coverage report as html by running
``py.test --cov --cov-report html``. The html report will be saved
``.htmlreport`` inside the coala repository.
