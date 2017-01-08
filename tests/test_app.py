import foobar, requests

# app unit test
def test_app():
    app = foobar.app.test_client()
    app.testing = True
    response = app.get('/foo')
    assert response.data.decode() == 'foo'
    response = app.get('/bar')
    assert response.data.decode() == 'bar'
