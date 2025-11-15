# Exercise 22: Solution

## Code
```python
import re
from collections import Counter, namedtuple
from datetime import datetime
from typing import Iterator

LogEntry = namedtuple('LogEntry', ['ip', 'timestamp', 'method', 'url', 'status', 'size'])


def parse_log_line(line: str) -> LogEntry:
    """Parse a single log line using regex."""
    pattern = r'(\d+\.\d+\.\d+\.\d+).*?\[(.*?)\]\s+"(\w+)\s+(.*?)\s+.*?"\s+(\d+)\s+(\d+)'
    match = re.search(pattern, line)
    if match:
        ip, timestamp, method, url, status, size = match.groups()
        return LogEntry(ip, timestamp, method, url, int(status), int(size))
    return None


def analyze_log_file(filename: str):
    """Analyze log file and generate statistics."""
    ip_counter = Counter()
    url_counter = Counter()
    status_counter = Counter()
    total_requests = 0
    unique_ips = set()

    # Process line by line (memory efficient)
    with open(filename, 'r') as f:
        for line in f:
            entry = parse_log_line(line)
            if entry:
                total_requests += 1
                unique_ips.add(entry.ip)
                ip_counter[entry.ip] += 1
                url_counter[entry.url] += 1
                status_counter[entry.status] += 1

    # Calculate statistics
    success_count = sum(count for status, count in status_counter.items() if 200 <= status < 300)
    error_count = sum(count for status, count in status_counter.items() if status >= 400)

    # Print report
    print(f"Statistics:")
    print(f"- Total requests: {total_requests}")
    print(f"- Unique IPs: {len(unique_ips)}")
    print(f"- Success rate: {success_count/total_requests*100:.1f}%")
    print(f"- Error rate: {error_count/total_requests*100:.1f}%")

    print(f"\nTop 5 IP addresses:")
    for ip, count in ip_counter.most_common(5):
        print(f"  {ip}: {count} requests")

    print(f"\nTop 5 URLs:")
    for url, count in url_counter.most_common(5):
        print(f"  {url}: {count} hits")

    print(f"\nStatus code distribution:")
    for status, count in sorted(status_counter.items()):
        print(f"  {status}: {count} requests")


# Demo with sample data
sample_log = '''192.168.1.1 - - [01/Jan/2024:10:00:00] "GET /api/users HTTP/1.1" 200 1234
192.168.1.2 - - [01/Jan/2024:10:01:00] "POST /api/login HTTP/1.1" 200 567
192.168.1.1 - - [01/Jan/2024:10:02:00] "GET /api/users HTTP/1.1" 200 1234'''

# Would call: analyze_log_file('access.log')
```

## Key Concepts
- Regex for log parsing
- Counter for aggregation
- namedtuple for structured data
- Generator for memory efficiency
- Statistics calculation
- File processing line by line
