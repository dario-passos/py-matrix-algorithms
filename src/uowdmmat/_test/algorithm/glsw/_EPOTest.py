#  _EPOTest.py
#  Copyright (C) 2019 University of Waikato, Hamilton, New Zealand
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
from typing import List

from ._GLSWTest import GLSWTest
from ...test.misc import TestRegression, TestDataset
from ....algorithm.glsw import EPO


class EPOTest(GLSWTest[EPO]):
    @TestRegression
    def n_1(self):
        self.subject.N = 1

    @TestRegression
    def n_3(self):
        self.subject.N = 3

    def get_datasets(self) -> List[TestDataset]:
        return [TestDataset.BOLTS]

    def instantiate_subject(self) -> EPO:
        return EPO()