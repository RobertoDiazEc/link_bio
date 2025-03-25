#!/bin/bash
if [ -d alembic ]; then
    reflex db migrate
fi
exec reflex run --env prod --backend-only