# CS310: Week 4 - Crontab Helper

## Summary

The goal of this assignment is to write a helper script
for scheduling cron tasks. This script should:
- Use simple helpers like "daily", or "hourly" to generate correct cron codes.
- Enable validation of cron codes
- Enable custom codes for power users

Your submission will include:
- A link to your version of this GitHub Repo
- A `.txt`, `.md`, `.org` written report
- A script named `cron-helper.<ext>` (either .py or .sh)

You may write this in Python or Bash

## Assignment

In this lab, you will:
- Create a script that prompts the user to answer questions:
    1. What program to schedule
    2. What is the cron schedule
        - This should have a choices, such as "daily" and "hourly"
        - It should allow custom cron schedules to be input
- Validate the data provided:
    - Check that the given program exists
    - Validate the syntax of the cron schedule given
- Print out a confirmation with the correct cron schedule
- Install the cron schedule on the crontab

### Extra Credit
In addition, detect if the system is running systemd by checking the processes, then ask if the user would want a SystemD timer created instead. Generate the timer file.

## Report

Your report is to have the following title: **CS 310 - W4 Crontab Helper.<ext>**

Your report is to answer the following questions in 1-2 sentences:
1. How do you provide choices as well as custom input to the user?
2. How did you validate the exsistence of a program?
3. How did you validate the syntax of a cron task?

## Resources
- [Awk: A powerful program to use from bash](https://learnxinyminutes.com/awk/)
- [Bash Case Statements](https://www.geeksforgeeks.org/linux-unix/bash-scripting-case-statement/)
- [Which Man Page](https://linux.die.net/man/1/which)
