#!/bin/bash

models=(
  "stg_asia"
  "stg_africa"
  "stg_america"
  "stg_atlantic"
  "stg_australia"
  "stg_europe"
  "stg_indian"
  "stg_pacific"
)

for model in "${models[@]}"
do
  file_name="${model}.py"
  touch "$file_name"
  echo "Created file: $file_name"
done
