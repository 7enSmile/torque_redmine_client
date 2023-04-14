import requests
import json
import time
import torquepy

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/webhook'
    headers = {'Content-type': 'application/json'}
    current_list_job_id = torquepy.TorqueManager.get_list_job_id()
    while True:
        new_list_job_id = torquepy.TorqueManager.get_list_job_id()

        if set(current_list_job_id) != set(new_list_job_id):
            for job_id in new_list_job_id:
                if not(job_id in current_list_job_id):
                    response = requests.post(url, data=json.dumps(torquepy.TorqueManager.get_info_job_id(job_id)),
                                             headers=headers)
        current_list_job_id = new_list_job_id
        time.sleep(10)