---
mode: agent
model: GPT-4.1
---

# Django App Updates

- All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory.

1. Update `settings.py` for MongoDB connection and CORS.
2. Update `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py`, and `admin.py` to support users, teams, activities, leaderboard, and workouts collections.
3. Ensure `/` points to the api and `api_root` is present in `urls.py`. (See <attachments> above for file contents. You may not need to search or read the file again.)

Notes and expectations:

- Use Django ORM (djongo/djongo-compatible setup) and follow project conventions already present in the repository.
- `settings.py` should include MongoDB connection settings (host, port, db name) and `CORS` configuration (allow origins appropriate for local development). Use environment variables where appropriate and include clear placeholder names.
- `models.py` should declare models for User (if custom), Team, Activity, Workout, and Leaderboard entries. Keep models simple and explicit about relationships (ForeignKey/ManyToMany) and indexing where applicable.
- Add `serializers.py` implementing DRF serializers for each model mentioned.
- `views.py` should expose viewsets or APIViews for CRUD operations and any leaderboard aggregation endpoints.
- `urls.py` should include `api_root` and register routers so that the project root `/` points to the API (e.g., route `/` -> api root view or a redirect to `/api/`).
- `tests.py` should include at least basic unit tests for model creation and one API endpoint (happy path) per major resource.
- `admin.py` should register all models for admin usage.

Assumptions:

- If a custom user model is not already in place, prefer using Django's default `User` and create profile-related models as needed.
- Environment variable names to use: `MONGO_HOST`, `MONGO_PORT`, `MONGO_DB_NAME`, `CORS_ALLOWED_ORIGINS`.

Delivery expectations:

- This prompt file will be used by an agent mode workflow to implement the changes across the Django app.
- Keep the instructions concise and actionable for an automated agent; do not include extraneous commentary.
