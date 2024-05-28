
## С Redis
wrk -t4 -c100 -d30s http://127.0.0.1:8000/api/route/664f6df7941b21d70ff97ed0
Running 30s test @ http://127.0.0.1:8000/api/route/664f6df7941b21d70ff97ed0
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    68.13ms  105.60ms   1.98s    98.32%
    Req/Sec   438.51    113.81     1.06k    68.99%
  51980 requests in 30.03s, 12.39MB read
  Socket errors: connect 0, read 0, write 0, timeout 2
Requests/sec:   1731.06
Transfer/sec:    422.62KB
## Без кэша
wrk -t4 -c100 -d30s http://127.0.0.1:8000/api/route/664f6df7941b21d70ff97ed0
Running 30s test @ http://127.0.0.1:8000/api/route/664f6df7941b21d70ff97ed0
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   183.88ms   68.77ms 668.69ms   85.16%
    Req/Sec   137.05     52.61   242.00     61.25%
  16320 requests in 30.03s, 3.89MB read
Requests/sec:    543.53
Transfer/sec:    132.70KB