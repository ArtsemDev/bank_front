from fastapi import FastAPI

from views.settings import static
from views.views import router, exceptions_data


app = FastAPI(exception_handlers=exceptions_data)
app.mount('/static', static, 'static')
app.include_router(router=router)
