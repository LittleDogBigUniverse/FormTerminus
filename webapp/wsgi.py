from app import app

if __name__ == "__main__":
    from werkzeug.serving import run_simple

    # context = ('fake.cert', 'fake.key')
    run_simple(app,
               threaded=True,
               use_reloader=True,
               use_debugger=False)
