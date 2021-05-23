# import native Python packages
from enum import Enum

# import third party packages
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

# custom local stuff
from src.timecapsule.deep import tcd_views


class TemplateID(str, Enum):
    APARGUMENT = "apargument"
    APARGUMENTSCAN = "apargumentscan"
    APENGLISH12 = "apenglish12"
    APPS = "apps"
    APSCHOLARD = "apscholard"
    BLUEBIRD = "Bluebird"
    BOWLINGPIC = "bowlingpic"
    CALCULUS = "calculus"
    CARPAYMENT = "CarPayment"
    DIPLOMA = "diploma"
    DOYOUKNOWME = "DoYouKnowMe"
    ECSP = "ecsp"
    ENGLISH10 = "english10"
    FIRSTAPPLET = "FirstApplet"
    GPA = "gpa"
    INDEX = "index"
    JAVAPROJECTS = "javaprojects"
    JGS = "jgs"
    MATHANALYSIS = "mathanalysis"
    MOMANDDAD = "momanddad"
    MTGP = "mtgp"
    MTHS = "mths"
    MYINDEX = "myindex"
    OOPS = "oops"
    PHYSICS = "physics"
    PORTFOLIO07 = "portfolio07"
    PORTFOLIO09 = "portfolio09"
    PORTFOLIO10 = "portfolio10"
    PRESIDENTGOLD = "presidentgold"
    PROJECTS = "projects"
    UCONNDIPLOMA = "uconndiploma"
    VAPILOT = "vapilot"
    VAPILOT2 = "vapilot2"
    VAPILOT3 = "vapilot3"
    WRITINGGOALS = "writinggoals"


def create_fastapi_app():
    # create the app
    view_app = FastAPI(
        title="timecapsule.tarpey.dev",
        description="Time capsule for miketarpey.com. We've come a long way since 2006...",
        docs_url=None,
        redoc_url=None,
        default_response_class=ORJSONResponse,
    )

    # templates
    templates = Jinja2Templates(directory='templates')

    # custom exception page to convert the 422 into a 404.
    @view_app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc):
        return templates.TemplateResponse(
            'error.html',
            context={
                'request': request,
                'exc': 'This page doesn\'t exist.',
                'status_code': 404,
            },
            status_code=404,
        )

    # custom exception page to convert a starlette (not FastAPI) exception
    @view_app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc):
        return templates.TemplateResponse(
            'error.html',
            context={
                'request': request,
                'exc': str(exc.detail),
                'status_code': exc.status_code,
            }
        )

    # config stuff
    view_app.mount("/static", app=StaticFiles(directory='static'), name="static")

    # routes
    @view_app.get('/', tags=["enumerated_path_view"])
    async def enter(request: Request):
        template_url = f'timecapsule/enter.html'
        return templates.TemplateResponse(
            template_url,
            context={'request': request},
        )

    @view_app.get('/{template_id}', tags=["enumerated_path_view"])
    async def timecapsule(request: Request, template_id: TemplateID):
        template_url = f'timecapsule/{template_id}.html'
        return templates.TemplateResponse(
            template_url,
            context={'request': request},
        )
    
    # deep routes
    view_app.include_router(tcd_views)

    return view_app


# entrypoint!
app = create_fastapi_app()
