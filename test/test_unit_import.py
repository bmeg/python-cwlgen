#!/usr/bin/env python

'''
Unit tests for import feature of cwlgen library
'''

#  Import  ------------------------------ 

# General libraries
import os
import filecmp
import unittest

# External libraries
from cwlgen.import_cwl import CWLToolParser

#  Class(es)  ------------------------------ 

class TestImport(unittest.TestCase):

    def setUp(self):
        ctp = CWLToolParser()
        self.tool = ctp.import_cwl('test/import_cwl.cwl')


class TestImportCWL(TestImport):

    def test_load_id(self):
        self.assertEqual(self.tool.tool_id, 'tool_id')

    def test_load_baseCommand(self):
        self.assertEqual(self.tool.base_command, 'share')

    def test_load_label(self):
        self.assertEqual(self.tool.label, 'a_label')

    def test_load_doc(self):
        self.assertEqual(self.tool.doc, 'super_doc')

    def test_load_cwlVersion(self):
        self.assertEqual(self.tool.cwl_version, 'v1.0')

    def test_load_stdin(self):
        self.assertEqual(self.tool.stdin, 'in')

    def test_load_stderr(self):
        self.assertEqual(self.tool.stderr, 'err')

    def test_load_stdout(self):
        self.assertEqual(self.tool.stdout, 'out')


class TestInputsParser(TestImport):

    def test_init_input(self):
        self.assertEqual(self.tool.inputs[0].id, 'INPUT1')

    def test_load_label(self):
        self.assertEqual(self.tool.inputs[0].label, 'label_in')

    def test_load_secondaryFiles(self):
        self.assertEqual(self.tool.inputs[0].secondary_file, 'sec_file_in')

    def test_load_format(self):
        self.assertEqual(self.tool.inputs[0].format, 'format_1930')

    def test_load_streamable(self):
        self.assertTrue(self.tool.inputs[0].streamable)

    def test_load_doc(self):
        self.assertEqual(self.tool.inputs[0].doc, 'documentation_in')

    def test_load_default(self):
        self.assertEqual(self.tool.inputs[0].default, 'def_in')

    def test_load_type(self):
        self.assertEqual(self.tool.inputs[0].type, 'File')


class TestInputBindingParser(TestImport):

    def test_load_loadContents(self):
        self.assertTrue(self.tool.inputs[0].input_binding.load_contents)

    def test_load_position(self):
        self.assertEqual(self.tool.inputs[0].input_binding.position, 0)

    def test_load_prefix(self):
        self.assertEqual(self.tool.inputs[0].input_binding.prefix, '--input')

    def test_load_separate(self):
        self.assertTrue(self.tool.inputs[0].input_binding.separate)

    def test_load_itemSeparator(self):
        self.assertEqual(self.tool.inputs[0].input_binding.item_separator, ';')

    def test_load_valueFrom(self):
        self.assertEqual(self.tool.inputs[0].input_binding.value_from, 'here')

    def test_load_shellQuote(self):
        self.assertTrue(self.tool.inputs[0].input_binding.shell_quote)


class TestOutputsParser(TestImport):

    def test_init_input(self):
        self.assertEqual(self.tool.outputs[0].id, 'OUTPUT1')

    def test_load_label(self):
        self.assertEqual(self.tool.outputs[0].label, 'label_out')

    def test_load_secondaryFiles(self):
        self.assertEqual(self.tool.outputs[0].secondary_file, 'sec_file_out')

    def test_load_format(self):
        self.assertEqual(self.tool.outputs[0].format, 'format_1930')

    def test_load_streamable(self):
        self.assertTrue(self.tool.outputs[0].streamable)

    def test_load_doc(self):
        self.assertEqual(self.tool.outputs[0].doc, 'documentation_out')

    def test_load_type(self):
        self.assertEqual(self.tool.outputs[0].type, 'File')
