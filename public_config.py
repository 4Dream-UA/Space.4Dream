###############################################################
# VARIABLES CONSTANTS
###############################################################

UNABLE_TO_INVITE = False
EMPLOYEE = "Employee"


###############################################################
# LISTS CONSTANTS
###############################################################

TASK_TYPE_VALUE = [
    "bug",
    "feature",
    "change",
    "refactoring",
    "review",
    "quality assurance"
]


###############################################################
# DICTIONARIES CONSTANTS
###############################################################

USERS = {
    "superuser":
        {
            """ Advice: this one ONLY for admin panel working! """
            "username": "pm_fletcher",
            "password": "PositionPM",
        },
    "cto":
        {
            "username": "ghost",
            "password": "PositionCTO",
        },
    "project_manager":
        {
            "username": "pm_fletcher",
            "password": "PositionPM",
        },
    "senior_python_developer":
        {
            "username": "j.rosati",
            "password": "PositionSPD",
        },
    "middle_python_developer":
        {
            "username": "f.lorenco",   # noqa -> For PyCharm it's uncorrect str 'lorenco'
            "password": "PositionMPD",
        }
}


POSITION_VALUE = {
    "CTO":
        {
            "name": "CTO",
            "rank": EMPLOYEE,
            "invite_able": True,
            "user": USERS["cto"],
        },
    "Senior Python Developer":
        {
            "name": "Python Developer",
            "rank:": "Senior",
            "invite_able": UNABLE_TO_INVITE,
            "user": USERS["senior_python_developer"],
        },
    "Middle Python Developer":
        {
            "name": "Python Developer",
            "rank:": "Middle",
            "invite_able": UNABLE_TO_INVITE,
            "user": USERS["middle_python_developer"],
        },
    "JavaScript Developer":
        {
            "name": "JavaScript Developer",
            "rank:": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "user": "NotUserNow",
        },
    "Senior Project Manager":
        {
            "name": "Project Manager",
            "rank:": "Senior",
            "invite_able": True,
            "user": "NotUserNow",
        },
    "Project Manager":
        {
            "name": "Project Manager",
            "rank:": EMPLOYEE,
            "invite_able": True,
            "user": USERS["project_manager"],
        },
    "HR Manager":
        {
            "name": "HR Manager",
            "rank:": EMPLOYEE,
            "invite_able": True,
            "user": "NotUserNow",
        },
    "QA Engineer":
        {
            "name": "QA Engineer",
            "rank:": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "user": "NotUserNow",
        },
    "Designer":
        {
            "name": "Designer",
            "rank:": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "user": "NotUserNow",
        },
    "Senior DevOps":
        {
            "name": "DevOps",
            "rank:": "Senior",
            "invite_able": UNABLE_TO_INVITE,
            "user": "NotUserNow",
        },
    "DevOps":
        {
            "name": "DevOps",
            "rank:": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "user": "NotUserNow",
        },
}
