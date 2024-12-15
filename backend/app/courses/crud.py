from app.courses.models import Course

# Cursos de exemplo
COURSES = [
    Course(1, "Blockchain Fundamentals", "Learn blockchain basics", 50, "5 weeks"),
    Course(2, "Blockchain with XRPL", "Hands-on with XRP Ledger", 80, "4 weeks"),
]

def get_courses():
    return [course.__dict__ for course in COURSES]

def get_course_details(course_id):
    for course in COURSES:
        if course.id == int(course_id):
            return course.__dict__
    return {"error": "Course not found"}
