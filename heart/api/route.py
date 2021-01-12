from heart.api.viewsets import person, department
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'persons', person.PersonViewSet)
router.register(r'departments', department.DepartmentViewSet)