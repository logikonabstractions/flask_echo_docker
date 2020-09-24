about
-----------------

a basic flask-server demo (2 servers) that echo each others on a docker network

structure
----------------

#. flask-1 server
#. flask-2 server


interactions
~~~~~~~~~~~~~~~

*. if either server is ping, it logs the ping it receives & also pings the other server
*. the other server logs the ping from the other server (but doesn't re-ping to avoid infinite pings loop)
*. if the ping includes an argument ``?foo=value``, then the value is passed to the other server

networks & communication
------------------------------

* the general syntax for communication between 2 containers is:
    * ``http://my_service_name:internal_port``, where ``my_service_name`` is the section title for that container in docker-compose
    * you can then use something like ``requests`` in python to make those get/post calls