# log_analyzer.py

logs = [
    "INFO System started",
    "ERROR Database connection failed",
    "WARNING Low disk space",
    "INFO User login successful",
    "ERROR Timeout occurred",
    "INFO Job completed"
]

summary = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

for log in logs:
    level = log.split()[0]
    if level in summary:
        summary[level] += 1

print("Log Summary:")
for level, count in summary.items():
    print(f"{level}: {count}")
