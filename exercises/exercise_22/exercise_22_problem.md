# Exercise 22: Log File Analyzer SI

**Difficulty:** Advanced++

## Objective
Create a log file analyzer using regex, file I/O, and data aggregation.

## Requirements
1. Parse Apache/Nginx-style log files
2. Extract IP addresses, timestamps, URLs, and status codes using regex
3. Count requests per IP address (use Counter)
4. Identify most accessed URLs
5. Calculate statistics: total requests, error rate, unique IPs
6. Filter logs by date range
7. Generate a summary report
8. Handle large files efficiently (process line by line)

## Expected Output
```
Processing log file: access.log
Total lines processed: 1000

Statistics:
- Total requests: 1000
- Unique IPs: 45
- Success rate: 95.2%
- Error rate: 4.8%

Top 5 IP addresses:
  192.168.1.1: 150 requests
  10.0.0.5: 120 requests
  ...

Top 5 URLs:
  /api/users: 200 hits
  /index.html: 180 hits
  ...

Status code distribution:
  200: 850 requests
  404: 30 requests
  500: 20 requests
```

## Hints
- Use regex to parse log format
- Process line by line for memory efficiency
- Use Counter for counting
- Calculate percentages for statistics
- Use datetime for date filtering
- Create a LogEntry class or use namedtuple

## Key Concepts
- Regular expressions for parsing
- File processing line by line
- Data aggregation and statistics
- Counter and collections
- Datetime handling
- Generator for memory efficiency
