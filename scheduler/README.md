
# Introduction to CRON

## What is CRON?
CRON is a time-based job scheduler in Unix-like operating systems. It allows users to schedule scripts or commands to run automatically at specified intervals.

## CRON Syntax
A CRON job is defined using the following syntax:
```
* * * * * /path/to/command
- - - - -
| | | | |
| | | | +---- Day of the week (0 - 7, Sunday is both 0 and 7)
| | | +------ Month (1 - 12)
| | +-------- Day of the month (1 - 31)
| +---------- Hour (0 - 23)
+------------ Minute (0 - 59)
```

### Examples:
- `0 5 * * * /path/to/script.sh`: Runs the script every day at 5:00 AM.
- `*/15 * * * * /path/to/script.sh`: Runs the script every 15 minutes.

## Scheduling `job.sh` in CRON
To schedule `job.sh` using CRON:
1. Open the CRON editor:
   ```bash
   crontab -e
   ```
2. Add the following line to schedule `job.sh` (e.g., every day at 2:00 AM):
   ```bash
   0 2 * * * /path/to/job.sh >> /path/to/job.log 2>&1
   ```

### Explanation:
- `0 2 * * *`: Runs the script at 2:00 AM every day.
- `/path/to/job.sh`: Full path to the `job.sh` script.
- `>> /path/to/job.log 2>&1`: Appends output and errors to `job.log`.

## Checking CRON Jobs
To view scheduled CRON jobs:
```bash
crontab -l
```

## Notes:
- Ensure `job.sh` is executable:
  ```bash
  chmod +x /path/to/job.sh
  ```
- Use absolute paths in `job.sh` to avoid issues with relative paths.

- Ensure that `crontab` has access to the file. On macOS (e.g., macOS Sequoia), `crontab` does not have access to folders or files by default. You need to grant access explicitly in the **System Settings**:
1. Go to **System Settings** > **Privacy & Security** > **Full Disk Access**.
2. Add your terminal application (e.g., Terminal, iTerm) to the list.
3. Restart the terminal and reconfigure your `crontab` if necessary.