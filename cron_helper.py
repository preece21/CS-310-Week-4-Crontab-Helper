import subprocess
import sys
import os

main():
  program = input("Enter the full path to the program you want to schedule: ")

  print("Please choose a schedule")
  print("1: Hourly")
  print("2: Daily")
  print("3: Weekly")
  print("4: Monthly")
  print("5: Custom")

  schedule_choice = input("Enter your choice(1-5): ")

  if schedule_choice == "1":
    schedule = "0 * * * *" # Every hour on minute 0
  elif schedule_choice == "2":
    schedule = "0 0 * * *": # Every day at midnight
  elif schedule_choice == "3":
    schedule = "0 0 * * 0" # Every Sunday at midnight
  elif schedule_choice == "4":
    schedule = "0 0 1 * *" # Every month of the first day of the month
  elif schedule_choice == "5":
    schedule = input("Enter custom cron schedule (ex: 0 0 * * 1): ")

  print(f"\nProcess to be scheduled: {program}\nCron Schedule: {schedule}\n")

  existing_cron = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
  if existing_cron.returncode == 0:
    cron_lines = existing_cron.stdout
  else:
    cron_lines = ""

  new_cron = cron_lines + f"{schedule} {program}\n"

  cmd = subprocess.run(["crontab", "-"], input=new_cron, text=True)

  if cmd.returncode == 0:
    print("Cron job successfully scheduled")
  else:
    print("Failed to schedule cron job")


if __name__ == "__main__":
  main()
  
