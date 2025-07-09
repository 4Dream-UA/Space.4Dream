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
    "senior_project_manager":
        {
            "username": "y.yamatano",
            "password": "PositionSPM",
        },
    "project_manager":
        {
            "username": "pm_fletcher",
            "password": "PositionPM",
        },
    "hr_manager":
        {
            "username": "o.foloronce",
            "password": "PositionHRM",
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
        },
    "java_script_developer":
        {
            "username": "t.kenlong",
            "password": "PositionJS",
        },
    "qa_engineer":
        {
            "username": "l.kokochenko",
            "password": "PositionQAE",
        },
    "designer":
        {
            "username": "o.umirenko",
            "password": "PositionD",
        },
    "senior_devops":
        {
            "username": "g.morgan",
            "password": "PositionSDO",
        },
    "devops":
        {
            "username": "k.lop",
            "password": "PositionDO",
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
            "user": USERS["java_script_developer"],
        },
    "Senior Project Manager":
        {
            "name": "Project Manager",
            "rank:": "Senior",
            "invite_able": True,
            "user": USERS["senior_project_manager"],
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
            "user": USERS["hr_manager"],
        },
    "QA Engineer":
        {
            "name": "QA Engineer",
            "rank:": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "user": USERS["qa_engineer"],
        },
    "Designer":
        {
            "name": "Designer",
            "rank:": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "user": USERS["designer"],
        },
    "Senior DevOps":
        {
            "name": "DevOps",
            "rank:": "Senior",
            "invite_able": UNABLE_TO_INVITE,
            "user": USERS["senior_devops"],
        },
    "DevOps":
        {
            "name": "DevOps",
            "rank:": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "user": USERS["devops"],
        },
}

def invite_able_returning() -> list:

    list_ = list()

    for value in POSITION_VALUE.values():

        if value["invite_able"]:
            list_.append(value["name"])

    return list_
