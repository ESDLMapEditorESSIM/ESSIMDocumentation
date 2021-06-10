import json
import time
import pytz
import base64
import requests
from os import path
from datetime import datetime as dt

# Common Constants
ESSIM_URL = 'http://localhost:8112/essim/simulation'
INFLUXDB_URL = 'http://influxdb:8086'
ESSIM_HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}
ESSIM_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z'
PROGRESS_UPDATE_INTERVAL = 1  # in seconds

# Simulation-specific constants
ESSIM_USER = 'John Doe'
ESSIM_SCENARIO_ID = 'TestScenario'
ESDL_FILE = 'SmallestESDL_np.esdl'
SIMULATION_DESCRIPTION = 'Testing ESSIM API'
START_DATE = dt(2021, 1, 1, 0, 0, 0, 0, pytz.UTC)
END_DATE = dt(2022, 1, 1, 0, 0, 0, 0, pytz.UTC)


class ESSIMSimulation:

    def __init__(self, esdl_file):
        """
        Constructor to create an ESSIM Simulation object
        :param esdl_file: Path to ESDL file to simulate with ESSIM
        """
        self.simulation_id = None
        self.dashboardURL = None
        self.esdl_file = esdl_file
        if not path.exists(self.esdl_file):
            raise ValueError('File {} does not exist!'.format(path.abspath(self.esdl_file)))

    def encode_esdl(self):
        """
        Function to encode contents of ESDL file into Base64
        :return: Base64-encoded contents of ESDL file
        """
        with open(self.esdl_file, 'r') as f:
            esdl_string = f.read().replace('\n', '')
        message_bytes = esdl_string.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        encoded_esdl = base64_bytes.decode('utf-8')
        return encoded_esdl

    def display_dashboard_url(self):
        """
        Function to display the Grafana Dashboard URL
        """
        if self.simulation_id is None:
            print('No simulation is started yet!')
            return
        status_path = '{}/{}'.format(ESSIM_URL, self.simulation_id)
        r = requests.get(url=status_path, headers=ESSIM_HEADERS)
        response = r.json()
        status_code = r.status_code
        if status_code == 200:
            if 'dashboardURL' in response:
                self.dashboardURL = response['dashboardURL']
                print('Dashboard URL: {}'.format(self.dashboardURL))
            else:
                print('Dashboard URL not found! Simulation meta-data looks like so:\n{}'.format(
                    json.dumps(response, indent=4, sort_keys=True)))
        elif status_code == 404:
            print(response['Description'])

    def display_progress(self):
        """
        Function to display progress of ESSIM simulation
        """
        if self.simulation_id is None:
            print('No simulation is started yet!')
            return

        status_path = '{}/{}/status'.format(ESSIM_URL, self.simulation_id)
        while True:
            r = requests.get(url=status_path, headers=ESSIM_HEADERS)
            response = r.json()
            status_code = r.status_code
            if status_code == 200:
                if response['State'] == 'RUNNING':
                    print('{:.1f}% complete'.format(100 * float(response['Description'])))
                    time.sleep(PROGRESS_UPDATE_INTERVAL)
                elif response['State'] == 'COMPLETE':
                    print('Simulation {}'.format(response['Description']))
                    break
                elif response['State'] == 'ERROR':
                    print('Simulation failed because of {}'.format(response['Description']))
                    break
            elif status_code == 404:
                print(response['Description'])
                break

    def start_simulation(self):
        """
        Function to start an ESSIM simulation
        """
        while True:
            data = {
                'user': ESSIM_USER,
                'startDate': START_DATE.strftime(ESSIM_DATE_FORMAT),
                'endDate': END_DATE.strftime(ESSIM_DATE_FORMAT),
                'scenarioID': ESSIM_SCENARIO_ID,
                'simulationDescription': SIMULATION_DESCRIPTION,
                'influxURL': INFLUXDB_URL,
                'esdlContents': self.encode_esdl()
            }
            print('Starting ESSIM Simulation')
            r = requests.post(url=ESSIM_URL, data=json.dumps(data), headers=ESSIM_HEADERS)
            response = r.json()
            status_code = r.status_code
            if status_code == 201:
                self.simulation_id = response['id']
                print(
                    'Successfully started ESSIM Simulation with id {id}'.format(id=response['id']))
                break
            elif status_code == 503:
                print('The ESSIM Engine is busy. Retrying in 5 seconds...')
                time.sleep(5)
            else:
                error = response['description']
                print('ESSIM Simulation failed because: {reason}'.format(reason=error))
                break


if __name__ == '__main__':
    essim = ESSIMSimulation(ESDL_FILE)
    essim.start_simulation()
    essim.display_dashboard_url()
    essim.display_progress()
    print('Done!')
