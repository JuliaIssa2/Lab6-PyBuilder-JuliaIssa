"""PyBuilder configuration for calculator_Julia_Issa."""

from pybuilder.core import init, use_plugin


use_plugin("python.core")
use_plugin("python.unittest")


name = "calculator_Julia_Issa"
version = "0.1.0"
default_task = "run_unit_tests"


@init
def set_properties(project):
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property("dir_source_unittest_python", "tests/unittest/calculator_Julia_Issa")
    project.set_property("unittest_module_glob", "test_*")
