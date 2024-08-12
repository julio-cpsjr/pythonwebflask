# from app import manager
from app import app

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=7996,
         )

# if __name__ == "__main__":
#     manager.run()
