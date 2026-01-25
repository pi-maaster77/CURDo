from app import create_app
import os

app = create_app()
if __name__ == "__main__":
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=8000, debug=debug_mode, use_reloader=False)