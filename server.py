#  / server.py
# Created by azat at 8.02.2023

# REF: [Debugging async Django under Uvicorn with Pycharm](https://www.valentinog.com/blog/pycharm-uvicorn/)

import uvicorn

if __name__ == '__main__':
    uvicorn.run("dj_ninja.asgi:application", reload=True)
