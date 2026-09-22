from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

print("1. Testing signup...")
try:
    signup_res = client.post('/auth/signup', json={
        'full_name': 'Test User',
        'mobile': '9876543210',
        'email': 'debug_user_1@example.com',
        'password': 'password123',
        'preferred_language': 'en',
        'state': 'Maharashtra',
        'district': 'Pune'
    })
    print('Signup status:', signup_res.status_code)
    print('Signup response:', signup_res.text)
except Exception as e:
    print('Signup exception:', e)

print("\n2. Testing login...")
try:
    login_res = client.post('/auth/login', json={
        'email': 'debug_user_1@example.com',
        'password': 'password123'
    })
    print('Login status:', login_res.status_code)
    print('Login response:', login_res.text)
    if login_res.status_code == 200:
        token = login_res.json().get('access_token')
        print("\n3. Testing /me...")
        me_res = client.get('/auth/me', headers={'Authorization': f'Bearer {token}'})
        print('Me status:', me_res.status_code)
        print('Me response:', me_res.text)
except Exception as e:
    print('Login exception:', e)

print("\n4. Testing CORS preflight with Origin: http://localhost:3000...")
cors_res = client.options('/auth/login', headers={
    'Origin': 'http://localhost:3000',
    'Access-Control-Request-Method': 'POST',
    'Access-Control-Request-Headers': 'content-type'
})
print('CORS preflight status:', cors_res.status_code)
print('CORS preflight headers:', dict(cors_res.headers))

print("\n5. Testing POST with Origin: http://localhost:3000...")
post_cors = client.post('/auth/login', json={
    'email': 'debug_user_1@example.com',
    'password': 'password123'
}, headers={'Origin': 'http://localhost:3000'})
print('POST with Origin status:', post_cors.status_code)
print('Access-Control-Allow-Origin header:', post_cors.headers.get('access-control-allow-origin'))
