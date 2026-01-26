# Question 1
docker run -it --entrypoint=bash python:3.13
pip --version

# Question 3 
uv sync
docker build -t taxi_ingest:uv .
docker run -it \
  --network=homework-1_default \
  taxi_ingest:uv \
  --host=pgdatabase

SELECT COUNT(1) AS total
FROM green_taxi_data
WHERE trip_distance <= 1
    AND lpep_pickup_datetime >= '2025-11-01 00:00:00'
    AND lpep_pickup_datetime < '2025-12-01 00:00:00'

# Question 4
SELECT 
    lpep_pickup_datetime::DATE AS pickup_day, 
    MAX(trip_distance) AS max_distance 
FROM green_taxi_data
WHERE trip_distance < 100
GROUP BY 1
ORDER BY 2  DESC
LIMIT 5

# Question 5
SELECT 
    z."Zone", 
    SUM(g.total_amount) AS totalamount
FROM zones AS z
JOIN green_taxi_data AS g
ON z."LocationID" = g."PULocationID"
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5