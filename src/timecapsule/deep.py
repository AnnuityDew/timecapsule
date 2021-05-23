# import native Python packages
from enum import Enum

# import third party packages
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


# router and templates
tcd_views = APIRouter(prefix="/deep")
templates = Jinja2Templates(directory='templates')


class DeepTemplateID(str, Enum):
    CAREERENTRY = "3careerentry"
    CAREERHOME = "3careerhome"
    CP = "cp"
    DA = "da"
    DDR = "ddr"
    DDRLINKS = "ddrlinks"
    DDRPICS = "ddrpics"
    DDRVIDEOS = "ddrvideos"
    ENTER = "enter"
    INSANITY = "insanity"
    NSA = "nsa"
    OTHERHOME = "otherhome"
    REVIEWSFAQS = "reviewsfaqs"
    SCHOOLPROJECTS = "schoolprojects"
    STEPMANIA = "stepmania"


@tcd_views.get('/{template_id}', tags=["enumerated_path_view"])
def timecapsuledeep(request: Request, template_id: DeepTemplateID):
    template_url = f'timecapsuledeep/{template_id}.html'
    return templates.TemplateResponse(
        template_url,
        context={'request': request},
    )
