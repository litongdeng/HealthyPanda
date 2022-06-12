from teenhealth.__init__ import app
# app will import from __init__.py

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)