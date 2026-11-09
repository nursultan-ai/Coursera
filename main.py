from fastapi import FastAPI
import uvicorn

from mysite.api import users, categories, applications,courses,enrollments,study_groups,ai
from mysite.database.db import Base, engine
from mysite.admin.setup import setup_admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Courser Project6-7')

app.include_router(users.user_router)
app.include_router(applications.application_router)
app.include_router(enrollments.enrollment_router)
app.include_router(study_groups.study_group_router)
app.include_router(categories.category_router)
app.include_router(courses.course_router)
app.include_router(ai.ai_router)
setup_admin(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)