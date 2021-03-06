# Copyright 2020 Ford Motor Company 

 

# Licensed under the Apache License, Version 2.0 (the "License"); 

# you may not use this file except in compliance with the License. 

# You may obtain a copy of the License at 

 

#     http://www.apache.org/licenses/LICENSE-2.0 

 

# Unless required by applicable law or agreed to in writing, software 

# distributed under the License is distributed on an "AS IS" BASIS, 

# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 

# See the License for the specific language governing permissions and 

# limitations under the License. 

from cookiecutterassert.rules.file_contains_line import FileContainsLineRule
from unittest.mock import patch
from pathlib import Path
import os.path
from cookiecutterassert import messager

currentFolder = os.path.dirname(os.path.abspath(__file__))
outputFolder = Path(currentFolder).parent.parent
testFolder = "someoutput"

line = "looking for this line"


def test_execute_shouldLookForLineInFileAndReturnTrueIfItExists():
    fileName = "example/fileWithLine.txt"
    fileContainsLineRule = FileContainsLineRule({}, testFolder, fileName, line)
    assert fileContainsLineRule.execute(outputFolder)

@patch("cookiecutterassert.messager.printError")
def test_execute_shouldLookForLineInFileAndReturnFalseIfItDoesNotExist(printMock):
    fileName = "example/fileWithoutLine.txt"
    fileContainsLineRule = FileContainsLineRule({}, testFolder, fileName, line)
    assert fileContainsLineRule.execute(outputFolder) == False
    printMock.assert_called_once_with("assertion fileContainsLine {0} {1} failed.  Matching line not found in {2}/{0}.".format(fileName, line, outputFolder)) 

@patch("cookiecutterassert.messager.printError")
def test_execute_shouldFailAndPrintIfFileDoesNotExist(printMock):
    fileName = "example/aFileThatDoesNotExist"
    fileContainsLineRule = FileContainsLineRule({}, testFolder, fileName, line)
    assert fileContainsLineRule.execute(outputFolder) == False
    printMock.assert_called_once_with("assertion fileContainsLine {0} {1} failed. {0} does not exist in {2}.".format(fileName, line, outputFolder)) 

@patch("cookiecutterassert.messager.printError")
def test_execute_should_use_case_sensitive_exists(printMock):
    fileName = "example/fileWithline.txt"
    fileContainsLineRule = FileContainsLineRule({}, testFolder, fileName, line)
    assert fileContainsLineRule.execute(outputFolder) == False
    printMock.assert_called_once_with("assertion fileContainsLine {0} {1} failed. {0} does not exist in {2}.".format(fileName, line, outputFolder)) 
