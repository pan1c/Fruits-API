# CI/CD for Fruit API

This workflow automates testing, building, and publishing Docker images for the Fruit API project.

**What the pipeline does:**
- Runs linters and unit tests inside a Docker container (fast, and ensures consistent environment).
- Spins up PostgreSQL as a service for integration tests.
- Builds test and production images using Docker Buildx.
- Uses GitHub Actions cache to speed up Docker builds.
- Runs integration tests against the real API and database.
- Pushes the production image to GitHub Container Registry (ghcr.io) with both latest and short SHA tags (this can be changed to semver, branch name, or another tagging scheme if needed).

**Key decisions:**
- **Docker-only tests:** All checks and tests run in containers to avoid "works on my machine" issues, and this turned out to be faster than installing Python and dependencies on the runner.
- **Multi-stage Dockerfile:** Separate prod/test stages: prod image is minimal, test image includes dev dependencies.
- **Caching:** BuildKit cache (type=gha) is used to avoid reinstalling dependencies on every push.
- **Network for integration:** API and DB run in the same Docker network for proper integration testing.
- **Image tags:** Tags are based on owner/repo and short SHA
