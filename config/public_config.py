###############################################################
# VARIABLES CONSTANTS
###############################################################
from idlelib.autocomplete import TRY_A

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
            "rank": "Senior",
            "invite_able": True,
            "priority": 2,
        },
    "Project Manager":
        {
            "name": "Project Manager",
            "rank": EMPLOYEE,
            "invite_able": True,
            "priority": 3,
        },
    "HR Manager":
        {
            "name": "HR Manager",
            "rank": EMPLOYEE,
            "invite_able": True,
            "priority": 4,
        },
    "Senior Python Developer":
        {
            "name": "Python Developer",
            "rank": "Senior",
            "invite_able": UNABLE_TO_INVITE,
            "priority": 5,
        },
    "Middle Python Developer":
        {
            "name": "Python Developer",
            "rank": "Middle",
            "invite_able": UNABLE_TO_INVITE,
            "priority": 6,
        },
    "JavaScript Developer":
        {
            "name": "JavaScript Developer",
            "rank": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "priority": 7,
        },
    "Senior DevOps":
        {
            "name": "DevOps",
            "rank": "Senior",
            "invite_able": UNABLE_TO_INVITE,
            "priority": 8,
        },
    "DevOps":
        {
            "name": "DevOps",
            "rank": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "priority": 9,
        },
    "QA Engineer":
        {
            "name": "QA Engineer",
            "rank": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "priority": 10,
        },
    "Designer":
        {
            "name": "Designer",
            "rank": EMPLOYEE,
            "invite_able": UNABLE_TO_INVITE,
            "priority": 11,
        },
    "Admin":
        {
            "name": "admin",
            "rank": "admin",
            "priority": 99,
        }
}


USERS = {
    "superuser":
        {
            # """ Advice: Do this one ONLY for admin panel working! """
            "username": "a.admin",
            "password": "PasswordADM",
            "position": POSITION_VALUE["Admin"],
            "is_staff": True,
            "is_superuser": True,
        },
    "cto":
        {
            "username": "g.stealth",
            "password": "PositionCTO",
            "position": POSITION_VALUE["CTO"],
            "is_staff": True,
        },
    "senior_project_manager":
        {
            "username": "y.yamatano",
            "password": "PositionSPM",
            "position": POSITION_VALUE["Senior Project Manager"],
            "is_staff": True,
        },
    "project_manager":
        {
            "username": "f.dowel",
            "password": "PositionPM",
            "position": POSITION_VALUE["Project Manager"],
            "is_staff": True,
        },
    "hr_manager":
        {
            "username": "o.foloronce",
            "password": "PositionHRM",
            "position": POSITION_VALUE["HR Manager"],
            "is_staff": True,
        },
    "senior_python_developer":
        {
            "username": "j.rosati",
            "password": "PositionSPD",
            "position": POSITION_VALUE["Senior Python Developer"],
        },
    "middle_python_developer":
        {
            "username": "f.lorenco",   # noqa -> For PyCharm it's uncorrect str 'lorenco'
            "password": "PositionMPD",
            "position": POSITION_VALUE["Middle Python Developer"],
        },
    "java_script_developer":
        {
            "username": "t.kenlong",
            "password": "PositionJS",
            "position": POSITION_VALUE["JavaScript Developer"],
        },
    "qa_engineer":
        {
            "username": "l.kokochenko",
            "password": "PositionQAE",
            "position": POSITION_VALUE["QA Engineer"],
        },
    "designer":
        {
            "username": "o.umirenko",
            "password": "PositionD",
            "position": POSITION_VALUE["Designer"],
        },
    "senior_devops":
        {
            "username": "g.morgan",
            "password": "PositionSDO",
            "position": POSITION_VALUE["Senior DevOps"],
        },
    "devops":
        {
            "username": "k.lop",
            "password": "PositionDO",
            "position": POSITION_VALUE["DevOps"],
        }
}


###############################################################
# FUNCTIONS RETURNING
###############################################################

def priority_returning() -> dict:
    dict_ = dict()


    for key, value in POSITION_VALUE.items():
        dict_[key] = value["priority"]

    return dict_


from django.db import transaction

@transaction.atomic
def init_requirements(
        position_model: "teamspace.models.PositionModel",
        taskType_model: "teamspace.models.TaskTypeModel",
) -> bool:

   for value in POSITION_VALUE.values():
       position_model.objects.create(name=value["name"], rank=value["rank"])

   for task_type in TASK_TYPE_VALUE:
       taskType_model.objects.create(name=task_type)

   return True



@transaction.atomic
def init_users(
        worker_model: "teamspace.models.WorkerModel",
        position_model: "teamspace.models.PositionModel",
) -> bool:


    for value in USERS.values():
        is_staff = value.get("is_staff", False)
        worker_model.objects.create_user(
            username=value["username"],
            password=value["password"],
            is_staff=is_staff,
            position=position_model.objects.get(
                name=value["position"]["name"],
                rank=value["position"]["rank"]
            ),
            first_name=value["username"].split(".")[0],
            last_name=value["username"].split(".")[1],
            email=f"{value['username']}@gmail.com",
            )
    return True

