## Необходимо также сделать миграции при помощи alembic

python -m venv venv
(activate venv)
alembic upgrade head

## Пользователи создаваемые скриптом
| User      | Password
| ----------|-----------------
| vladushek | Pe&6>52ZDn27306d
| vaspup    | honQ?0*oL4|2:Oc:
| chernal   | xDQY&1|0I7m7b1xa
| goland    | QxsvkYqa1MES6u3o


## Маршруты создаваемые при помощи скрипта

| start_point | destination_point | driver_id | passenger_ids
|-------------|-------------------|-----------|-------------|
| Moscow      | Kazan             |  1        | [2, 3]
| Kazan       | Moscow            |  1        | [2, 3]
| Saint-Petersburg | Moscow       |  1        | [4]

## Показатели производительность
Находятся в файле performance.md
### Результат с Redis
| Thread Stats |    Avg    |   Stdev   |  Max  | +/- Stdev
|--------------|-----------|-----------|-------|----------|
|   Latency    |  68.13ms  | 105.60ms  | 1.98s |   98.32%
|   Req/Sec    | 438.51    | 113.81    | 1.06k |   68.99%

### Результат без Redis
| Thread Stats |    Avg    |   Stdev   |  Max  | +/- Stdev
|--------------|-----------|-----------|-------|----------|
|   Latency    |  183.88ms | 68.77ms   | 668.69ms |   85.16%
|   Req/Sec    | 137.05    | 52.61     | 242.00 |   61.25%