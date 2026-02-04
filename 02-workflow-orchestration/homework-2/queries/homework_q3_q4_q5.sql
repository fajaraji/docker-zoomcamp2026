-- Question 3 (Yellow Taxi 2020)
SELECT COUNT(*) 
FROM `de-zoomcamp-2026-01.zoomcamp.yellow_tripdata`
WHERE filename LIKE '%2020%';

-- Question 4 (Green Taxi 2020)
SELECT COUNT(*) 
FROM `de-zoomcamp-2026-01.zoomcamp.green_tripdata`
WHERE filename LIKE '%2020%';

-- Question 5 (Yellow Taxi Maret 2021)
SELECT COUNT(*) 
FROM `de-zoomcamp-2026-01.zoomcamp.yellow_tripdata`
WHERE filename LIKE '%2021-03%';