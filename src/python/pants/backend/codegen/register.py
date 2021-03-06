# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

"""Enable this backend to turn on every single codegen backend within `pants.backend.codegen`."""

from pants.backend.codegen.thrift.java.apache_thrift_java_gen import ApacheThriftJavaGen
from pants.backend.codegen.thrift.java.java_thrift_library import (
    JavaThriftLibrary as JavaThriftLibraryV1,
)
from pants.backend.codegen.thrift.java.target_types import JavaThriftLibrary
from pants.backend.codegen.thrift.python.apache_thrift_py_gen import ApacheThriftPyGen
from pants.backend.codegen.thrift.python.python_thrift_library import (
    PythonThriftLibrary as PythonThriftLibraryV1,
)
from pants.backend.codegen.thrift.python.target_types import PythonThriftLibrary
from pants.build_graph.build_file_aliases import BuildFileAliases
from pants.goal.task_registrar import TaskRegistrar as task


def build_file_aliases():
    return BuildFileAliases(
        targets={
            "java_thrift_library": JavaThriftLibraryV1,
            "python_thrift_library": PythonThriftLibraryV1,
        }
    )


def register_goals():
    task(name="thrift-java", action=ApacheThriftJavaGen).install("gen")
    task(name="thrift-py", action=ApacheThriftPyGen).install("gen")


def target_types():
    return [JavaThriftLibrary, PythonThriftLibrary]
