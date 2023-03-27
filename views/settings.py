from os.path import join
from pathlib import Path

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(directory=join(BASE_DIR, 'templates'))
static = StaticFiles(directory=join(BASE_DIR, 'static'))
