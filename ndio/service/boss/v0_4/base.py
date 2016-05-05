# Copyright 2016 The Johns Hopkins University Applied Physics Laboratory
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ndio.service.boss.baseversion import BaseVersion
from . import BOSS_VERSION
from . import BOSS_ENDPOINT

class Base(BaseVersion):
    """This is the common parent for all interfaces to the Boss v.04.
    """

    def __init__(self):
        super().__init__()
        self._token = None

    @property
    def version(self):
        return BOSS_VERSION

    @property
    def endpoint(self):
        return BOSS_ENDPOINT
