import foobar
import multiprocessing, pytest, requests, socket

# system tests that assumes app is running
def test_system_simple():
    response = requests.get('http://127.0.0.1:5000/foo') # TODO need same port the docker is linked to:/
    assert response.text == 'foo'
    assert response.status_code == 200

# system test that uses fixtures
test_host = '127.0.0.1'
test_port = 5001

def run_server():
    foobar.app.run(test_host, test_port)

@pytest.fixture
def server():
    p = multiprocessing.Process(target=run_server)
    p.start()
    while True:
        try:
            s = socket.socket() 
            s.connect((test_host, test_port))
            break
        except:
            pass
        finally:
             s.close()
    yield None 
    p.terminate()    
    p.join()    

# unneeded test since we use docker and assume the server is up        
def atest_system_fixture(server):
    response = requests.get('http://%s:%s/foo' % (test_host, test_port)) 
    assert response.text == 'foo'
    assert response.status_code == 200
