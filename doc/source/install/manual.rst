..
      Copyright 2012 Nicolas Barcet for Canonical
                2013 New Dream Network, LLC (DreamHost)

      Licensed under the Apache License, Version 2.0 (the "License"); you may
      not use this file except in compliance with the License. You may obtain
      a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
      License for the specific language governing permissions and limitations
      under the License.

.. _installing_manually:

=====================
 Installing Manually
=====================


Storage Backend Installation
============================

This step is a prerequisite for the collector, notification agent and API
services. You may use one of the listed database backends below to store
Ceilometer data.

.. note::
   Please notice, MongoDB (and some other backends like DB2 and HBase)
   require pymongo_ to be installed on the system. The required minimum
   version of pymongo is 2.4.
..


MongoDB
-------

   The recommended Ceilometer storage backend is `MongoDB`. Follow the
   instructions to install the MongoDB_ package for your operating system, then
   start the service. The required minimum version of MongoDB is 2.4.

   To use MongoDB as the storage backend, change the 'database' section in
   ceilometer.conf as follows::

    [database]
    connection = mongodb://username:password@host:27017/ceilometer

   If MongoDB is configured in replica set mode, add param in ceilometer.conf
   to use MongoReplicaSetClient::

    [database]
    mongodb_replica_set = replica_name

SQLalchemy-supported DBs
------------------------

   You may alternatively use `MySQL` (or any other SQLAlchemy-supported DB
   like `PostgreSQL`).

   In case of SQL-based database backends, you need to create a `ceilometer`
   database first and then initialise it by running::

    ceilometer-dbsync

   To use MySQL as the storage backend, change the 'database' section in
   ceilometer.conf as follows::

    [database]
    connection = mysql+pymysql://username:password@host/ceilometer?charset=utf8

HBase
-----

   HBase backend is implemented to use HBase Thrift interface, therefore it is
   mandatory to have the HBase Thrift server installed and running. To start
   the Thrift server, please run the following command::

    ${HBASE_HOME}/bin/hbase thrift start

   The implementation uses `HappyBase`_, which is a wrapper library used to
   interact with HBase via Thrift protocol. You can verify the thrift
   connection by running a quick test from a client::

    import happybase

    conn = happybase.Connection(host=$hbase-thrift-server, port=9090, table_prefix=None)
    print conn.tables() # this returns a list of HBase tables in your HBase server

   .. note::
      HappyBase version 0.5 or greater is required. Additionally, version 0.7
      is not currently supported.
   ..

   In case of HBase, the needed database tables (`project`, `user`, `resource`,
   `meter`, `alarm`, `alarm_h`) should be created manually with `f` column
   family for each one.

   To use HBase as the storage backend, change the 'database' section in
   ceilometer.conf as follows::

    [database]
    connection = hbase://hbase-thrift-host:9090

DB2
---

   DB2 installation should follow fresh IBM DB2 NoSQL installation docs.

   To use DB2 as the storage backend, change the 'database' section in
   ceilometer.conf as follows::

    [database]
    connection = db2://username:password@host:27017/ceilometer


.. _HappyBase: http://happybase.readthedocs.org/en/latest/index.html#
.. _MongoDB: http://www.mongodb.org/
.. _pymongo: https://pypi.python.org/pypi/pymongo/



