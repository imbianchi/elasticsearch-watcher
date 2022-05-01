import json
import requests
import pprint
import common.functions as functions
import syslog
from emails.sendEmails import sendErrorEmails, sendWarningEmails
from logs.logs import errorLog, warningLog


def getElasticStatus():
    try:
        return requests.get('http://127.0.0.1:9200')
    except:
        return 500


def watcher():
    if getElasticStatus() != 500:
        syslog.syslog(
            syslog.LOG_INFO, '[elasticsearch-watcher] - Elasticsearch is up and running!')
    else:
        pprint.pprint('Something wrong...')
        syslog.syslog(syslog.LOG_WARNING,
                      '[elasticsearch-watcher] - Elasticsearch is down! Trying to reconnect...')

        outputRestartElastic = functions.cmd(
            'systemctl restart elasticsearch', 'Reconnecting...', True)

        if outputRestartElastic.returncode != 0:
            syslog.syslog(syslog.LOG_ERR,
                          '[elasticsearch-watcher] - Elasticsearch not restarted! Sending e-mails...')

            errorLog()
            sendErrorEmails()
        else:
            warningLog()
            sendWarningEmails()
