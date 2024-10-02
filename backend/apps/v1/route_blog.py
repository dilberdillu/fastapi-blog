from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.repository.blog import list_blogs, retrieve_blog
from db.session import get_db
from typing import Optional



templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
def home(request: Request, alert: Optional[str] = None, db: Session = Depends(get_db)):
    print(dir(request))
    blogs = list_blogs(db=db)
    context = {"request": request, "blogs": blogs, "alert": alert}
    return templates.TemplateResponse("blogs/home.html", context)

@router.get("/app/blog/{id}")
def blog_detail(request: Request, id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    return templates.TemplateResponse("blogs/detail.html", {"request": request, "blog": blog})