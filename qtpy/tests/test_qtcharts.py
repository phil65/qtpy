from __future__ import absolute_import

import pytest
from qtpy import PYQT5, PYSIDE2


@pytest.mark.skipif(not (PYQT5 or PYSIDE2), reason="Only available in Qt5 bindings")
def test_qtcharts():
    """Test the qtpy.QtCharts namespace"""
    from qtpy import QtCharts
    assert QtCharts.QtCharts.QChart is not None

