from rest_framework import permissions
from .permissions import  IsStaffPermission


class StaffEditorPermissionMixin():
    permission_classes=[permissions.IsAdminUser,IsStaffPermission]

