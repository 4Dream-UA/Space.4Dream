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
            "priority": 1,
        },
    "Senior Project Manager":
        {
            "name": "Project Manager",
            "rank:": "Senior",
            "invite_able": True,
            "priority": 2,
        },
    "Project Manager":
        {
            "name": "Project Manager",
            "rank:": EMPLOYEE,
            "invite_able": True,
            "priority": 3,
        },
    "HR Manager":
        {
            "name": "HR Manager",
            "rank:": EMPLOYEE,
            "invite_able": True,
            "priority": 4,
        },
    "Senior Python Developer":
        {
            "name": "Python Developer",
            "rank:": "Senior",
            "invite_able": UNABLE_TO_INVITE,
            "priority": 5,
        },
    "Middle Python Developer":
        {
            "name": "Python Developer",
            "rank:": "Middle",
            "invite_able": UNABLE_TO_INVITE,
            "priority": 6,
        },
    "JavaScript Developer":
        {
            "name": "JavaScript Developer",
            "rank:": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "priority": 7,
        },
    "Senior DevOps":
        {
            "name": "DevOps",
            "rank:": "Senior",
            "invite_able": UNABLE_TO_INVITE,
            "priority": 8,
        },
    "DevOps":
        {
            "name": "DevOps",
            "rank:": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "priority": 9,
        },
    "QA Engineer":
        {
            "name": "QA Engineer",
            "rank:": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "priority": 10,
        },
    "Designer":
        {
            "name": "Designer",
            "rank:": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "priority": 11,
        },
}


###############################################################
# FUNCTIONS RETURNING
###############################################################

def invite_able_returning() -> list:

    list_ = list()

    for value in POSITION_VALUE.values():

        if value["invite_able"]:
            list_.append(value["name"])

    return list_

def priority_returning() -> dict:
    dict_ = dict()


    for key, value in POSITION_VALUE.items():
        dict_[key] = value["priority"]

    return dict_
