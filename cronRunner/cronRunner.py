from pprint import pprint
from elasticWatcher.watcher import watcher
from crontab import CronTab       
import pathlib


cron = CronTab(user = True)
currentPath = pathlib.Path().resolve()
basicCmd = f'*/5 * * * * elasticsearch-watcher {currentPath}/index.py'
basicIteration = cron.find_command("elasticsearch-watcher")

def createCronWatcher():
    job = cron.new(command = f'elasticsearch-watcher {currentPath}/index.py')
    job.minute.every(5)
    job.enable()
    cron.write()
    print('Cronjob does not exist and added successfully.. please see \"crontab -l\"')

def cronWatcherExists():
    for item in basicIteration:

        if str(item) == basicCmd:
            pprint('Crontab job already exist')
            return True

def cronRunner():
    if cronWatcherExists():
        watcher()
    else:
        createCronWatcher()
