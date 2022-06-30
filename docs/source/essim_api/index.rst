ESSIM API
=========

.. note::
    This documentation is work in progress and far from finished. New sections will be added in the near future.
    Whenever questions or feedback is received from end users, we're trying to update this documentation on the fly.
    So don't hesitate to contact us, whenever you run into problems.

Sequence
--------
ESSIM provides a REST API that allows users to interact with ESSIM for starting a simulation, requesting its progress, etc. The usual sequence to invoking a simulation and interacting with it is as follows:

  .. figure:: ../images/APISequence.png
    :scale: 90 %
    :align: center

APIs:
-----


/simulation
^^^^^^^^^^^

* **HTTP Method**: POST
* **Description**: Create a new simulation
* **Request Body**:
    * *endDate*: End date of simulation in ISO-8601 format (``YYYY-MM-DDTHH:mm:ss±hh:mm``)
    * *esdlContents*: 64-bit encoded ESDL string
    * *influxURL*: URL of InfluxDB instance to store simulation results in
    * *scenarioID*: String ID representing the scenario being simulated. This ID is used to name the database in InfluxDB.
    * *simulationDescription*: Human-readable description of the simulation visible in the dashboard
    * *startDate*: Start date of simulation in ISO-8601 format (``YYYY-MM-DDTHH:mm:ss±hh:mm``)
    * *user*: Name of the user running the simulation. Used to tag the name of the Grafana dashboard
    * *csvFilesLocation*: (Optional) To export ESSIM simulation data into CSV, specify a location here
    * *mqttURL*: (Optional) To publish ESSIM data to an MQTT bus, specify the URL to an MQTT server here
    * *amqpURL*: (Optional) To publish ESSIM data to an AMQP bus, specify the URL to an AMQP server here
    * *kafkaURL*: (Optional) To publish ESSIM data to an Apache Kafka server, specify the URL to the server here
    * *nodeConfig*: (Optional) To use a remote node with ESSIM, specify the following:

       *  *esdlNodeId*: The ESDL ID of the asset represented by this node
       *  *config*: Any key-value configuration to provide this node
       *  *mqttHost*: MQTT Host URL
       *  *mqttPort*: MQTT Port number
       *  *mqttTopic*: Topic to reach the ESDL Node
    
    **Example**:

      .. code-block:: json

        {
            "user": "john doe",
            "scenarioID": "essim",
            "simulationDescription": "A simple ES with one geothermal source and a heat demand",
            "startDate": "2019-01-01T00:00:00+0100",
            "endDate": "2020-01-01T00:00:00+0100",
            "influxURL": "http://influxdb:8086",
            "esdlContents": "PD94bWwgdmVyc2lvbj0nMS4wJyBlbmNvZGluZz0nVVRGLTgnPz4KPGVzZGw6RW5lcmd5U3lzdGVtIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiIHhtbG5zOmVzZGw9Imh0dHA6Ly93d3cudG5vLm5sL2VzZGwiIGVzZGxWZXJzaW9uPSJ2MjEwMiIgdmVyc2lvbj0iMSIgaWQ9ImVlMTBjYTVmLWEwOGQtNDIwMS04MjNjLWZhN2FiY2MxYmExYiIgbmFtZT0iVW50aXRsZWQgRW5lcmd5U3lzdGVtIiBkZXNjcmlwdGlvbj0iIj4KICA8ZW5lcmd5U3lzdGVtSW5mb3JtYXRpb24geHNpOnR5cGU9ImVzZGw6RW5lcmd5U3lzdGVtSW5mb3JtYXRpb24iIGlkPSI3NTE4NDJiNy04MGUxLTRlODItYTIyMi1mZGViZWNhOGE3OTciPgogICAgPGNhcnJpZXJzIHhzaTp0eXBlPSJlc2RsOkNhcnJpZXJzIiBpZD0iMGEzY2I2OTYtMjU1OC00OGY0LTllMjMtYWZmMTFlMTAyMGE0Ij4KICAgICAgPGNhcnJpZXIgeHNpOnR5cGU9ImVzZGw6SGVhdENvbW1vZGl0eSIgbmFtZT0iSGVhdCIgaWQ9ImZjZDYyZThmLWVmN2EtNDA0Yy04ZDNmLWQ5NGU5ZGQ0OGNkMyIgc3VwcGx5VGVtcGVyYXR1cmU9IjgwLjAiIHJldHVyblRlbXBlcmF0dXJlPSI0MC4wIi8+CiAgICA8L2NhcnJpZXJzPgogICAgPHF1YW50aXR5QW5kVW5pdHMgeHNpOnR5cGU9ImVzZGw6UXVhbnRpdHlBbmRVbml0cyIgaWQ9IjNmMWEzNjAzLTIwMTgtNGExNi05N2U5LTY3ZWVlZTE5NWE1YiI+CiAgICAgIDxxdWFudGl0eUFuZFVuaXQgeHNpOnR5cGU9ImVzZGw6UXVhbnRpdHlBbmRVbml0VHlwZSIgcGh5c2ljYWxRdWFudGl0eT0iRU5FUkdZIiB1bml0PSJKT1VMRSIgbXVsdGlwbGllcj0iR0lHQSIgaWQ9ImViMDdiY2NiLTIwM2YtNDA3ZS1hZjk4LWU2ODc2NTZhMjIxZCIgZGVzY3JpcHRpb249IkVuZXJneSBpbiBHSiIvPgogICAgPC9xdWFudGl0eUFuZFVuaXRzPgogIDwvZW5lcmd5U3lzdGVtSW5mb3JtYXRpb24+CiAgPGluc3RhbmNlIHhzaTp0eXBlPSJlc2RsOkluc3RhbmNlIiBuYW1lPSJVbnRpdGxlZCBJbnN0YW5jZSIgaWQ9IjQyYTY0ODU1LWRlODYtNGE2Ni1iMjY3LWIwMGM2NmI0M2I1OCI+CiAgICA8YXJlYSB4c2k6dHlwZT0iZXNkbDpBcmVhIiBuYW1lPSJVbnRpdGxlZCBBcmVhIiBpZD0iN2JjZjVjZDktZDNmZS00NjI2LTg1OWEtYzE2ZDg5ZGRmNTUyIj4KICAgICAgPGFzc2V0IHhzaTp0eXBlPSJlc2RsOkdlb3RoZXJtYWxTb3VyY2UiIG5hbWU9Ikdlb3RoZXJtYWxTb3VyY2VfYjU3MiIgaWQ9ImI1NzJkNmNiLTMxM2UtNDg5Zi1iNDg5LWE4NmJiZDZlY2QyMSI+CiAgICAgICAgPGdlb21ldHJ5IHhzaTp0eXBlPSJlc2RsOlBvaW50IiBsb249IjQuNzAyNzkyMTY3NjYzNTc1IiBDUlM9IldHUzg0IiBsYXQ9IjUyLjEyMTcwNjEzMzM3ODU5Ii8+CiAgICAgICAgPHBvcnQgeHNpOnR5cGU9ImVzZGw6T3V0UG9ydCIgaWQ9IjE1ZmY3MDk5LThiN2YtNDZhZi1iY2M0LTYzZTAzZjE3NzIyZSIgbmFtZT0iT3V0IiBjb25uZWN0ZWRUbz0iYTA5ODU3YjUtNTA5My00OTljLTgzY2UtNTRlY2M1NGE3NTE4IiBjYXJyaWVyPSJmY2Q2MmU4Zi1lZjdhLTQwNGMtOGQzZi1kOTRlOWRkNDhjZDMiPgogICAgICAgICAgPHByb2ZpbGUgeHNpOnR5cGU9ImVzZGw6U2luZ2xlVmFsdWUiIHZhbHVlPSI1LjAiIGlkPSJhMzgwNGI2Mi00MjA1LTRhZmItYmY3OC02MGNkNzNkMzM5ZjIiPgogICAgICAgICAgICA8cHJvZmlsZVF1YW50aXR5QW5kVW5pdCB4c2k6dHlwZT0iZXNkbDpRdWFudGl0eUFuZFVuaXRSZWZlcmVuY2UiIHJlZmVyZW5jZT0iZWIwN2JjY2ItMjAzZi00MDdlLWFmOTgtZTY4NzY1NmEyMjFkIi8+CiAgICAgICAgICA8L3Byb2ZpbGU+CiAgICAgICAgPC9wb3J0PgogICAgICA8L2Fzc2V0PgogICAgICA8YXNzZXQgeHNpOnR5cGU9ImVzZGw6SGVhdGluZ0RlbWFuZCIgbmFtZT0iSGVhdGluZ0RlbWFuZF9iNTA1IiBpZD0iYjUwNWMxMGItYmRlNC00NjA2LThkNjgtN2Y4ZTAxODhjMzgzIj4KICAgICAgICA8Z2VvbWV0cnkgeHNpOnR5cGU9ImVzZGw6UG9pbnQiIGxvbj0iNC43MTIzODM3NDcxMDA4MzEiIENSUz0iV0dTODQiIGxhdD0iNTIuMTIxOTE2OTI4MzE4ODYiLz4KICAgICAgICA8cG9ydCB4c2k6dHlwZT0iZXNkbDpJblBvcnQiIGNvbm5lY3RlZFRvPSIxNWZmNzA5OS04YjdmLTQ2YWYtYmNjNC02M2UwM2YxNzcyMmUiIGlkPSJhMDk4NTdiNS01MDkzLTQ5OWMtODNjZS01NGVjYzU0YTc1MTgiIG5hbWU9IkluIiBjYXJyaWVyPSJmY2Q2MmU4Zi1lZjdhLTQwNGMtOGQzZi1kOTRlOWRkNDhjZDMiPgogICAgICAgICAgPHByb2ZpbGUgeHNpOnR5cGU9ImVzZGw6U2luZ2xlVmFsdWUiIHZhbHVlPSI1LjAiIGlkPSJlNGU2OTE5YS1jNTY4LTRlNTgtODkwNC1jZmUzMWI5YjVkN2MiPgogICAgICAgICAgICA8cHJvZmlsZVF1YW50aXR5QW5kVW5pdCB4c2k6dHlwZT0iZXNkbDpRdWFudGl0eUFuZFVuaXRSZWZlcmVuY2UiIHJlZmVyZW5jZT0iZWIwN2JjY2ItMjAzZi00MDdlLWFmOTgtZTY4NzY1NmEyMjFkIi8+CiAgICAgICAgICA8L3Byb2ZpbGU+CiAgICAgICAgPC9wb3J0PgogICAgICA8L2Fzc2V0PgogICAgPC9hcmVhPgogIDwvaW5zdGFuY2U+CjwvZXNkbDpFbmVyZ3lTeXN0ZW0+Cg"
        }

* **Response**:
    * CREATED (HTTP status code - 201)
        * *status*: CREATED
        * *id*: Unique ID for this simulation run. This ID will be tagged in all simulation data from this run.

        **Example:**

         .. code-block:: json
         
           {
             "status": "CREATED",
             "id": "60c0c0a84840404e8b19df9b"
           }
      
    * BAD REQUEST (HTTP status code - 400)
        * *status*: ERROR
        * *description*: Description of the error

        **Example:**

         .. code-block:: json
         
           {
             "status": "ERROR",
             "description": "Internal error: Error in Observation Manager init: Connecting to InfluxDB @ http://non-existing-host:8088 timed out. Please check URL!"
           }
      
    * SERVICE UNAVAILABLE (HTTP status code - 503)
        * If a simulation is already running while a new one is started, HTTP status code 503 is returned with a text body ``Busy``.
   
/simulation/<simulation-id>
^^^^^^^^^^^^^^^^^^^^^^^^^^^
* **HTTP Method**: GET
* **Description**: Retrieve meta-data of simulation run. This includes information provided by the user at the time of starting the simulation and some run-time data. This API call can be used to retrieve the dashboard URL as soon as a simulation is *CREATED*
* **Request Body**:
    * None
* **Response**:
    * NOT FOUND (HTTP status code - 404)
        * *status*: ERROR
        * *description*: Description of the error
      
        **Example:**
        
          .. code-block:: json

            {
                "status": "ERROR",
                "description": "SimulationID 60c0c0a84840404e8b19479b not found!"
            }
    
    * OK (HTTP status code - 200)
        * *status*: The last known status of the simulation.
        * *simRunDate*: The date when the simulation was run in ISO-8601 format (``YYYY-MM-DDTHH:mm:ss±hh:mm``).
        * *transport*: An HTML visualisation of ESSIM's internal transport network trees created per commodity. The HTML pages are URL-encoded and tagged with the name of the network.
        * *dashboardURL*: A link to the Grafana dashboard created by ESSIM for this simulation.

        **Example:**
        
          .. code-block:: json
          
            {
                "esdlContents": "PD94bWwgdmVyc2lvbj0nMS4wJyBlbmNvZGluZz0nVVRGLTgnPz4KPGVzZGw6RW5lcmd5U3lzdGVtIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiIHhtbG5zOmVzZGw9Imh0dHA6Ly93d3cudG5vLm5sL2VzZGwiIGVzZGxWZXJzaW9uPSJ2MjEwMiIgdmVyc2lvbj0iMSIgaWQ9ImVlMTBjYTVmLWEwOGQtNDIwMS04MjNjLWZhN2FiY2MxYmExYiIgbmFtZT0iVW50aXRsZWQgRW5lcmd5U3lzdGVtIiBkZXNjcmlwdGlvbj0iIj4KICA8ZW5lcmd5U3lzdGVtSW5mb3JtYXRpb24geHNpOnR5cGU9ImVzZGw6RW5lcmd5U3lzdGVtSW5mb3JtYXRpb24iIGlkPSI3NTE4NDJiNy04MGUxLTRlODItYTIyMi1mZGViZWNhOGE3OTciPgogICAgPGNhcnJpZXJzIHhzaTp0eXBlPSJlc2RsOkNhcnJpZXJzIiBpZD0iMGEzY2I2OTYtMjU1OC00OGY0LTllMjMtYWZmMTFlMTAyMGE0Ij4KICAgICAgPGNhcnJpZXIgeHNpOnR5cGU9ImVzZGw6SGVhdENvbW1vZGl0eSIgbmFtZT0iSGVhdCIgaWQ9ImZjZDYyZThmLWVmN2EtNDA0Yy04ZDNmLWQ5NGU5ZGQ0OGNkMyIgc3VwcGx5VGVtcGVyYXR1cmU9IjgwLjAiIHJldHVyblRlbXBlcmF0dXJlPSI0MC4wIi8+CiAgICA8L2NhcnJpZXJzPgogICAgPHF1YW50aXR5QW5kVW5pdHMgeHNpOnR5cGU9ImVzZGw6UXVhbnRpdHlBbmRVbml0cyIgaWQ9IjNmMWEzNjAzLTIwMTgtNGExNi05N2U5LTY3ZWVlZTE5NWE1YiI+CiAgICAgIDxxdWFudGl0eUFuZFVuaXQgeHNpOnR5cGU9ImVzZGw6UXVhbnRpdHlBbmRVbml0VHlwZSIgcGh5c2ljYWxRdWFudGl0eT0iRU5FUkdZIiB1bml0PSJKT1VMRSIgbXVsdGlwbGllcj0iR0lHQSIgaWQ9ImViMDdiY2NiLTIwM2YtNDA3ZS1hZjk4LWU2ODc2NTZhMjIxZCIgZGVzY3JpcHRpb249IkVuZXJneSBpbiBHSiIvPgogICAgPC9xdWFudGl0eUFuZFVuaXRzPgogIDwvZW5lcmd5U3lzdGVtSW5mb3JtYXRpb24+CiAgPGluc3RhbmNlIHhzaTp0eXBlPSJlc2RsOkluc3RhbmNlIiBuYW1lPSJVbnRpdGxlZCBJbnN0YW5jZSIgaWQ9IjQyYTY0ODU1LWRlODYtNGE2Ni1iMjY3LWIwMGM2NmI0M2I1OCI+CiAgICA8YXJlYSB4c2k6dHlwZT0iZXNkbDpBcmVhIiBuYW1lPSJVbnRpdGxlZCBBcmVhIiBpZD0iN2JjZjVjZDktZDNmZS00NjI2LTg1OWEtYzE2ZDg5ZGRmNTUyIj4KICAgICAgPGFzc2V0IHhzaTp0eXBlPSJlc2RsOkdlb3RoZXJtYWxTb3VyY2UiIG5hbWU9Ikdlb3RoZXJtYWxTb3VyY2VfYjU3MiIgaWQ9ImI1NzJkNmNiLTMxM2UtNDg5Zi1iNDg5LWE4NmJiZDZlY2QyMSI+CiAgICAgICAgPGdlb21ldHJ5IHhzaTp0eXBlPSJlc2RsOlBvaW50IiBsb249IjQuNzAyNzkyMTY3NjYzNTc1IiBDUlM9IldHUzg0IiBsYXQ9IjUyLjEyMTcwNjEzMzM3ODU5Ii8+CiAgICAgICAgPHBvcnQgeHNpOnR5cGU9ImVzZGw6T3V0UG9ydCIgaWQ9IjE1ZmY3MDk5LThiN2YtNDZhZi1iY2M0LTYzZTAzZjE3NzIyZSIgbmFtZT0iT3V0IiBjb25uZWN0ZWRUbz0iYTA5ODU3YjUtNTA5My00OTljLTgzY2UtNTRlY2M1NGE3NTE4IiBjYXJyaWVyPSJmY2Q2MmU4Zi1lZjdhLTQwNGMtOGQzZi1kOTRlOWRkNDhjZDMiPgogICAgICAgICAgPHByb2ZpbGUgeHNpOnR5cGU9ImVzZGw6U2luZ2xlVmFsdWUiIHZhbHVlPSI1LjAiIGlkPSJhMzgwNGI2Mi00MjA1LTRhZmItYmY3OC02MGNkNzNkMzM5ZjIiPgogICAgICAgICAgICA8cHJvZmlsZVF1YW50aXR5QW5kVW5pdCB4c2k6dHlwZT0iZXNkbDpRdWFudGl0eUFuZFVuaXRSZWZlcmVuY2UiIHJlZmVyZW5jZT0iZWIwN2JjY2ItMjAzZi00MDdlLWFmOTgtZTY4NzY1NmEyMjFkIi8+CiAgICAgICAgICA8L3Byb2ZpbGU+CiAgICAgICAgPC9wb3J0PgogICAgICA8L2Fzc2V0PgogICAgICA8YXNzZXQgeHNpOnR5cGU9ImVzZGw6SGVhdGluZ0RlbWFuZCIgbmFtZT0iSGVhdGluZ0RlbWFuZF9iNTA1IiBpZD0iYjUwNWMxMGItYmRlNC00NjA2LThkNjgtN2Y4ZTAxODhjMzgzIj4KICAgICAgICA8Z2VvbWV0cnkgeHNpOnR5cGU9ImVzZGw6UG9pbnQiIGxvbj0iNC43MTIzODM3NDcxMDA4MzEiIENSUz0iV0dTODQiIGxhdD0iNTIuMTIxOTE2OTI4MzE4ODYiLz4KICAgICAgICA8cG9ydCB4c2k6dHlwZT0iZXNkbDpJblBvcnQiIGNvbm5lY3RlZFRvPSIxNWZmNzA5OS04YjdmLTQ2YWYtYmNjNC02M2UwM2YxNzcyMmUiIGlkPSJhMDk4NTdiNS01MDkzLTQ5OWMtODNjZS01NGVjYzU0YTc1MTgiIG5hbWU9IkluIiBjYXJyaWVyPSJmY2Q2MmU4Zi1lZjdhLTQwNGMtOGQzZi1kOTRlOWRkNDhjZDMiPgogICAgICAgICAgPHByb2ZpbGUgeHNpOnR5cGU9ImVzZGw6U2luZ2xlVmFsdWUiIHZhbHVlPSI1LjAiIGlkPSJlNGU2OTE5YS1jNTY4LTRlNTgtODkwNC1jZmUzMWI5YjVkN2MiPgogICAgICAgICAgICA8cHJvZmlsZVF1YW50aXR5QW5kVW5pdCB4c2k6dHlwZT0iZXNkbDpRdWFudGl0eUFuZFVuaXRSZWZlcmVuY2UiIHJlZmVyZW5jZT0iZWIwN2JjY2ItMjAzZi00MDdlLWFmOTgtZTY4NzY1NmEyMjFkIi8+CiAgICAgICAgICA8L3Byb2ZpbGU+CiAgICAgICAgPC9wb3J0PgogICAgICA8L2Fzc2V0PgogICAgPC9hcmVhPgogIDwvaW5zdGFuY2U+CjwvZXNkbDpFbmVyZ3lTeXN0ZW0+Cg",
                "user": "john doe",
                "scenarioID": "essim",
                "simulationDescription": "A simple ES with one geothermal source and a heat demand",
                "startDate": "2018-12-31T23:00:00+0000",
                "endDate": "2019-12-31T23:00:00+0000",
                "status": {
                    "state": "COMPLETE",
                    "description": "Finished in PT1.099S"
                },
                "influxURL": "http://influxdb:8086",
                "simRunDate": "2021-06-09T13:22:48+0000",
                "transport": [
                    {
                        "name": "Untitled EnergySystem Heat Network 0",
                        "networkHTMLDiag": "%3C%21DOCTYPE+html%3E%0A%3Chtml+lang%3D%22en%22%3E%0A++%3Chead%3E%0A++++%3Cmeta+charset%3D%22utf-8%22%3E%0A%0A++++%3Ctitle%3E%0A%09Untitled+EnergySystem+Heat+Network+0%0A%09%3C%2Ftitle%3E%0A%0A++++%3Cstyle%3E%0A++++%0A++++.node+%7B%0A++++++++cursor%3A+pointer%3B%0A++++%7D%0A%0A++++.node+circle+%7B%0A++++++fill%3A+%23fff%3B%0A++++++stroke%3A+steelblue%3B%0A++++++stroke-width%3A+3px%3B%0A++++%7D%0A%0A++++.node+text+%7B%0A++++++font%3A+12px+sans-serif%3B%0A++++%7D%0A%0A++++.link+%7B%0A++++++fill%3A+none%3B%0A++++++stroke%3A+%23ccc%3B%0A++++++stroke-width%3A+2px%3B%0A++++%7D%0A++++%0A++++%3C%2Fstyle%3E%0A%0A++%3C%2Fhead%3E%0A%0A++%3Cbody%3E%0A%0A%3C%21--+load+the+d3.js+library+--%3E+%0A%3Cscript+src%3D%22http%3A%2F%2Fd3js.org%2Fd3.v3.min.js%22%3E%3C%2Fscript%3E%0A++++%0A%3Cscript%3E%0A%0Avar+treeData%3D%5B%7B%22parent%22%3A%22null%22%2C%22children%22%3A%5B%7B%22parent%22%3A%22GeothermalSource_b572%28PRODUCER%29%22%2C%22name%22%3A%22b505c10b-bde4-4606-8d68-7f8e0188c383%28CONSUMER%29%22%7D%5D%2C%22name%22%3A%22GeothermalSource_b572%28PRODUCER%29%22%7D%5D%3B%0A%0A%2F%2F+**************+Generate+the+tree+diagram++*****************%0Avar+margin+%3D+%7Btop%3A+20%2C+right%3A+120%2C+bottom%3A+20%2C+left%3A+200%7D%2C%0A++++width+%3D+1960+-+margin.right+-+margin.left%2C%0A++++height+%3D+500+-+margin.top+-+margin.bottom%3B%0A++++%0Avar+i+%3D+0%2C%0A++++duration+%3D+750%2C%0A++++root%3B%0A%0Avar+tree+%3D+d3.layout.tree%28%29%0A++++.size%28%5Bheight%2C+width%5D%29%3B%0A%0Avar+diagonal+%3D+d3.svg.diagonal%28%29%0A++++.projection%28function%28d%29+%7B+return+%5Bd.y%2C+d.x%5D%3B+%7D%29%3B%0A%0Avar+svg+%3D+d3.select%28%22body%22%29.append%28%22svg%22%29%0A++++.attr%28%22width%22%2C+width+%2B+margin.right+%2B+margin.left%29%0A++++.attr%28%22height%22%2C+height+%2B+margin.top+%2B+margin.bottom%29%0A++.append%28%22g%22%29%0A++++.attr%28%22transform%22%2C+%22translate%28%22+%2B+margin.left+%2B+%22%2C%22+%2B+margin.top+%2B+%22%29%22%29%3B%0A%0Aroot+%3D+treeData%5B0%5D%3B%0Aroot.x0+%3D+height+%2F+2%3B%0Aroot.y0+%3D+0%3B%0A++%0Aupdate%28root%29%3B%0A%0Ad3.select%28self.frameElement%29.style%28%22height%22%2C+%22500px%22%29%3B%0A%0Afunction+update%28source%29+%7B%0A%0A++%2F%2F+Compute+the+new+tree+layout.%0A++var+nodes+%3D+tree.nodes%28root%29.reverse%28%29%2C%0A++++++links+%3D+tree.links%28nodes%29%3B%0A%0A++%2F%2F+Normalize+for+fixed-depth.%0A++nodes.forEach%28function%28d%29+%7B+d.y+%3D+d.depth+*+250%3B+%7D%29%3B%0A%0A++%2F%2F+Update+the+nodes%E2%80%A6%0A++var+node+%3D+svg.selectAll%28%22g.node%22%29%0A++++++.data%28nodes%2C+function%28d%29+%7B+return+d.id+%7C%7C+%28d.id+%3D+%2B%2Bi%29%3B+%7D%29%3B%0A%0A++%2F%2F+Enter+any+new+nodes+at+the+parent%27s+previous+position.%0A++var+nodeEnter+%3D+node.enter%28%29.append%28%22g%22%29%0A++++++.attr%28%22class%22%2C+%22node%22%29%0A++++++.attr%28%22transform%22%2C+function%28d%29+%7B+return+%22translate%28%22+%2B+source.y0+%2B+%22%2C%22+%2B+source.x0+%2B+%22%29%22%3B+%7D%29%0A++++++.on%28%22click%22%2C+click%29%3B%0A%0A++nodeEnter.append%28%22circle%22%29%0A++++++.attr%28%22r%22%2C+1e-6%29%0A++++++.style%28%22fill%22%2C+function%28d%29+%7B+return+d._children+%3F+%22lightsteelblue%22+%3A+%22%23fff%22%3B+%7D%29%3B%0A%0A++nodeEnter.append%28%22text%22%29%0A++++++.attr%28%22x%22%2C+function%28d%29+%7B+return+d.children+%7C%7C+d._children+%3F+-13+%3A+13%3B+%7D%29%0A++++++.attr%28%22dy%22%2C+%22.35em%22%29%0A++++++.attr%28%22text-anchor%22%2C+function%28d%29+%7B+return+d.children+%7C%7C+d._children+%3F+%22end%22+%3A+%22start%22%3B+%7D%29%0A++++++.text%28function%28d%29+%7B+return+d.name%3B+%7D%29%0A++++++.style%28%22fill-opacity%22%2C+1e-6%29%3B%0A%0A++%2F%2F+Transition+nodes+to+their+new+position.%0A++var+nodeUpdate+%3D+node.transition%28%29%0A++++++.duration%28duration%29%0A++++++.attr%28%22transform%22%2C+function%28d%29+%7B+return+%22translate%28%22+%2B+d.y+%2B+%22%2C%22+%2B+d.x+%2B+%22%29%22%3B+%7D%29%3B%0A%0A++nodeUpdate.select%28%22circle%22%29%0A++++++.attr%28%22r%22%2C+10%29%0A++++++.style%28%22fill%22%2C+function%28d%29+%7B+return+d._children+%3F+%22lightsteelblue%22+%3A+%22%23fff%22%3B+%7D%29%3B%0A%0A++nodeUpdate.select%28%22text%22%29%0A++++++.style%28%22fill-opacity%22%2C+1%29%3B%0A%0A++%2F%2F+Transition+exiting+nodes+to+the+parent%27s+new+position.%0A++var+nodeExit+%3D+node.exit%28%29.transition%28%29%0A++++++.duration%28duration%29%0A++++++.attr%28%22transform%22%2C+function%28d%29+%7B+return+%22translate%28%22+%2B+source.y+%2B+%22%2C%22+%2B+source.x+%2B+%22%29%22%3B+%7D%29%0A++++++.remove%28%29%3B%0A%0A++nodeExit.select%28%22circle%22%29%0A++++++.attr%28%22r%22%2C+1e-6%29%3B%0A%0A++nodeExit.select%28%22text%22%29%0A++++++.style%28%22fill-opacity%22%2C+1e-6%29%3B%0A%0A++%2F%2F+Update+the+links%E2%80%A6%0A++var+link+%3D+svg.selectAll%28%22path.link%22%29%0A++++++.data%28links%2C+function%28d%29+%7B+return+d.target.id%3B+%7D%29%3B%0A%0A++%2F%2F+Enter+any+new+links+at+the+parent%27s+previous+position.%0A++link.enter%28%29.insert%28%22path%22%2C+%22g%22%29%0A++++++.attr%28%22class%22%2C+%22link%22%29%0A++++++.attr%28%22d%22%2C+function%28d%29+%7B%0A++++++++var+o+%3D+%7Bx%3A+source.x0%2C+y%3A+source.y0%7D%3B%0A++++++++return+diagonal%28%7Bsource%3A+o%2C+target%3A+o%7D%29%3B%0A++++++%7D%29%3B%0A%0A++%2F%2F+Transition+links+to+their+new+position.%0A++link.transition%28%29%0A++++++.duration%28duration%29%0A++++++.attr%28%22d%22%2C+diagonal%29%3B%0A%0A++%2F%2F+Transition+exiting+nodes+to+the+parent%27s+new+position.%0A++link.exit%28%29.transition%28%29%0A++++++.duration%28duration%29%0A++++++.attr%28%22d%22%2C+function%28d%29+%7B%0A++++++++var+o+%3D+%7Bx%3A+source.x%2C+y%3A+source.y%7D%3B%0A++++++++return+diagonal%28%7Bsource%3A+o%2C+target%3A+o%7D%29%3B%0A++++++%7D%29%0A++++++.remove%28%29%3B%0A%0A++%2F%2F+Stash+the+old+positions+for+transition.%0A++nodes.forEach%28function%28d%29+%7B%0A++++d.x0+%3D+d.x%3B%0A++++d.y0+%3D+d.y%3B%0A++%7D%29%3B%0A%7D%0A%0A%2F%2F+Toggle+children+on+click.%0Afunction+click%28d%29+%7B%0A++if+%28d.children%29+%7B%0A++++d._children+%3D+d.children%3B%0A++++d.children+%3D+null%3B%0A++%7D+else+%7B%0A++++d.children+%3D+d._children%3B%0A++++d._children+%3D+null%3B%0A++%7D%0A++update%28d%29%3B%0A%7D%0A%0A%3C%2Fscript%3E%0A++++%0A++%3C%2Fbody%3E%0A%3C%2Fhtml%3E"
                    }
                ],
                "dashboardURL": "https://essim-dashboard.hesi.energy/d/gUtvSu6Mk/untitled-energysystem-john-doe-2021-06-09t13-22-48-55"
            }

/simulation/<simulation-id>/status
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* **HTTP Method**: GET
* **Description**: Retrieve status of a simulation run. This API can be used as soon as a simulation is *CREATED*
* **Request Body**:
    * None
* **Response**:
    * NOT FOUND (HTTP status code - 404)
        * *status*: ERROR
        * *description*: Description of the error
      
        **Example:**
        
          .. code-block:: json

            {
                "status": "ERROR",
                "description": "SimulationID 60c0c0a84840404e8b19479b not found!"
            }
            
    * OK (HTTP status code - 200)
        * Running
            * *State*: RUNNING
            * *Description*: Percentage progress of the simulation as a limiting to 1.0

              .. code-block:: json
              
                {
                    "State": "RUNNING"
                    "Description": "0.7604529616724739",
                }
        * Finished
            * *State*: COMPLETE
            * *Description*: Time for simulation to complete

              .. code-block:: json
              
                {
                    "State": "COMPLETE"
                    "Description": "Finished in PT35.306S",
                }
        * Error
            * *State*: ERROR
            * *Description*: Description of the error

              .. code-block:: json
              
                {
                    "State": "ERROR"
                    "Description": "Cannot connect to InfluxDB service at [http://non-existing-host:8086] to query profile with id 3499a337-1785-4601-8098-3c46b6d42b7c. Please verify the URL!",
                }

Code Example
------------
Following is a simple code example to access the ESSIM APIs using python. Before you run this example:

  1. Copy the ESDL file below the python example to the same folder as the script. Adjust the name of the file in the script (line 21) appropriately if the name of the ESDL file is changed.
  2. Install the necessary python libraries using ``pip install requests pytz``.
  3. Start ESSIM following the instructions `here <https://github.com/ESDLMapEditorESSIM/docker-toolsuite#steps-to-follow>`_.

Python Code:
^^^^^^^^^^^^
  .. literalinclude:: simulation.py
    :linenos:
    :language: python

ESDL File (`sim.esdl`):
^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: sim.esdl
  :language: xml

