# Permissions and Groups in Django Application

## Custom Permissions
- The `Article` model has the following custom permissions:
  - `can_view`: Allows viewing articles.
  - `can_create`: Allows creating articles.
  - `can_edit`: Allows editing articles.
  - `can_delete`: Allows deleting articles.

## Groups
- Three groups have been created and assigned permissions:
  - **Viewers**
    - Permissions: `can_view`
  - **Editors**
    - Permissions: `can_edit`, `can_create`
  - **Admins**
    - Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`

## Permission Enforcement
- Permissions are enforced in views using the `@permission_required` decorator to restrict access based on user roles.

## Testing
- Test users should be created and assigned to different groups to ensure that permissions apply correctly when accessing various views.
