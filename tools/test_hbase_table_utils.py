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

import os
import sys

from oslo_config import cfg

from aodh import storage


def main(argv):
    cfg.CONF([], project='aodh')
    if os.getenv("AODH_TEST_HBASE_URL"):
        url = ("%s?table_prefix=%s" %
               (os.getenv("AODH_TEST_HBASE_URL"),
                os.getenv("AODH_TEST_HBASE_TABLE_PREFIX", "test")))
        alarm_conn = storage.get_connection(url, 'AODH.alarm.storage')
        for arg in argv:
            if arg == "--upgrade":
                alarm_conn.upgrade()
            if arg == "--clear":
                alarm_conn.clear()


if __name__ == '__main__':
    main(sys.argv[1:])
