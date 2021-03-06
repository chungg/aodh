#
# Copyright 2015 Red Hat, Inc
#
# Authors: Eoghan Glynn <eglynn@redhat.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from stevedore import extension


EVALUATOR_EXTENSIONS_NAMESPACE = "aodh.alarm.evaluator"
NOTIFIER_EXTENSIONS_NAMESPACE = "aodh.alarm.notifier"

NOTIFIERS = extension.ExtensionManager(NOTIFIER_EXTENSIONS_NAMESPACE,
                                       invoke_on_load=True)
NOTIFIER_SCHEMAS = NOTIFIERS.map(lambda x: x.name)
