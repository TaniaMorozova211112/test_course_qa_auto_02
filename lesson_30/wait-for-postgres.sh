#!/bin/sh
# Скрипт очікування запуску PostgreSQL перед тестами

set -e

host="postgres-db"
port=5432

echo "Waiting for PostgreSQL to start at $host:$port..."

# Цикл очікування, поки база буде готова
until pg_isready -h $host -p $port > /dev/null 2>&1; do
  echo "PostgreSQL is not ready yet. Sleeping..."
  sleep 1
done

echo "PostgreSQL is ready. Starting tests..."
exec "$@"
