## Alembic database migrations

When you make changes to the DB schema you will have to run the alembic scripts for generating an appropriate migration file.

This is how you do it:

1. Create the template migration script

```
alembic revision -m "name of the revision"
```

2. Edit the newly created python file and fill out the `upgrade()` and `downgrade()` function with the relevant code bits
3. You can now run the migration like so:

```
OONI_PG_URL=postgresql://oonipg:oonipg@localhost/oonipg hatch run alembic upgrade head
```
