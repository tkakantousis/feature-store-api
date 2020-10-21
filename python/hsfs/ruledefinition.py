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


class RuleDefinition:
    def __init__(
        self,
        name,
        predicate,
        value_type,
        description,
        href=None,
        expand=None,
        items=None,
        count=None,
        type=None,
    ):
        self._name = name
        self._predicate = predicate
        self._value_type = value_type
        self._description = description

    @classmethod
    def from_response_json(cls, json_dict):
        json_decamelized = humps.decamelize(json_dict)
        if "count" in json_decamelized:
            if json_decamelized["count"] == 0:
                return []
            return [
                cls(**ruledefinition) for ruledefinition in json_decamelized["items"]
            ]
        else:
            return cls(**json_decamelized)

    def json(self):
        return json.dumps(self, cls=util.FeatureStoreEncoder)

    def to_dict(self):
        return {
            "name": self._name,
            "predicate": self._predicate,
            "valueType": self._value_type,
            "description": self._description,
        }

    @property
    def name(self):
        return self._name

    @property
    def predicate(self):
        return self._predicate

    @property
    def value_type(self):
        return self._value_type

    @property
    def description(self):
        return self._description
