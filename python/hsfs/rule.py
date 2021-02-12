#
#   Copyright 2020 Logical Clocks AB
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import humps
import json

from hsfs import util


class Rule:
    """Metadata object representing the validation rule that is used by feature group expectations.

    This class is made for hsfs internal use only.
    """

    def __init__(
        self,
        name: str,
        level,
        min=None,
        max=None,
        pattern=None,
        accepted_type=None,
        legal_values=None,
        href=None,
        expand=None,
        items=None,
        count=None,
        type=None,
    ):
        self.name = name
        self._level = level
        self._min = min
        self._max = max
        self._pattern = pattern
        self._accepted_type = accepted_type
        self._legal_values = legal_values

    @classmethod
    def from_response_json(cls, json_dict):
        json_decamelized = humps.decamelize(json_dict)
        if json_decamelized["count"] == 0:
            return []
        return [cls(**rule) for rule in json_decamelized["items"]]

    def json(self):
        return json.dumps(self, cls=util.FeatureStoreEncoder)

    def to_dict(self):
        return {
            "name": self._name,
            "level": self._level,
            "min": self._min,
            "max": self._max,
            "pattern": self._pattern,
            "acceptedType": self._accepted_type,
            "legalValues": self._legal_values,
        }

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.upper()

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, min):
        self._min = min

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, max):
        self._max = max

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        self._pattern = pattern

    @property
    def accepted_type(self):
        return self._accepted_type

    @accepted_type.setter
    def accepted_type(self, accepted_type):
        self._accepted_type = accepted_type

    @property
    def legal_values(self):
        return self._legal_values

    @legal_values.setter
    def legal_values(self, legal_values):
        self._legal_values = legal_values
