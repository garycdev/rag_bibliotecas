#!/bin/bash
export $(cat .env | xargs)
uvicorn app.main:app --host $HOST --port $PORT --workers ${WORKERS:-4}
