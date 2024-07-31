#!/bin/bash

CONTAINER_NAME=api_with_bot_db
DB_USER=postgresq
DB_NAME=api_with_bot

SCRIPT_DIR=$(dirname $(realpath $0))

SQL_FILE1=$SCRIPT_DIR/cats_breed.sql
SQL_FILE2=$SCRIPT_DIR/cats_cat.sql

echo "Inserting breeds..."
docker exec -i $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -f $SQL_FILE1

echo "Inserting cats..."
docker exec -i $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -f $SQL_FILE2
echo "DB populated successfully"
