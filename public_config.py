USERS = {
    "superuser":
        {
            "username": "pm_fletcher",
            "password": "PositionPM",
        },
    "project_manager":
        {
            "username": "pm_fletcher",
            "password": "PositionPM",
        },
}

TASK_TYPE_VALUE = [
    "bug",
    "feature",
    "change",
    "refactoring",
    "review",
    "quality assurance"
]

POSITION_VALUE = {
    "CTO":
        {
            "name": "CTO",
        },
    "Senior Python Developer":
        {
            "name": "Python Developer",
            "rank:": "Senior",
        },
    "Middle Python Developer":
        {
            "name": "Python Developer",
            "rank:": "Middle",
        },
    "JavaScript Developer":
        {
            "name": "JavaScript Developer",
        },
    "Senior Project Manager":
        {
            "name": "Project Manager",
            "rank:": "Senior",
        },
    "Project Manager":
        {
            "name": "Project Manager",
            "user": USERS["project_manager"],
        },
    "QA Engineer":
        {
            "name": "QA Engineer",
        },
    "Designer":
        {
            "name": "Designer",
        },
    "Senior DevOps":
        {
            "name": "DevOps",
            "rank:": "Senior",
        },
    "DevOps":
        {
            "name": "DevOps",
        },
}
