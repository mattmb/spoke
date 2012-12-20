from hub.lib.client import Client
import time

def update_job(name, job_id, parent_id, result, status='SUCCESS'):
    client = Client('/usr/local/pkg/hub/etc/hub.conf')
    taskdata = {'status': status, 'name': name, 'data': result, 'id': job_id, 'parent_id': parent_id }
    client.post(parent_id, 'update', taskdata=taskdata)
    return True

def get_job(job_id):
    client = Client('/usr/local/pkg/hub/etc/hub.conf')
    response = client.post_wait(job_id, 'get')
    return response

def sleep(secs, name, job_id, parent_id, result, status='SUCCESS'):
    time.sleep(secs)
    client = Client('/usr/local/pkg/hub/etc/hub.conf')
    taskdata = {'status': status, 'name': name, 'data': result, 'id': job_id, 'parent_id': parent_id }
    client.post(parent_id, 'update', taskdata=taskdata)
    return True