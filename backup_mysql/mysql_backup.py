#!/usr/bin/python3.6
import os
import time
import datetime
import pipes
from logger import log
 
def auth_db(x):
    database_auth = {'db_host': 'localhost', 'db_name': 'DATABASE_NAME', 'db_user': 'DB_USER', 'db_password': 'DB_PASS'}
    return database_auth[x]
 
# folder name like == "20201217-123433".
BACKUP_PATH = '/home/backups'
DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME
 
# backup folder checking


def dir_check():
    try:
        os.stat(TODAYBACKUPPATH)
    except:
        log.warning("creating backup directory ... Do Not Intrrupt ")
        os.mkdir(TODAYBACKUPPATH)
 
def backup(): 
    dir_check()
    log.warning("starting dump ...")
    log.info("it will take a few minutes")
    dumpcmd = "mysqldump -h " + auth_db("db_host") + " -u " + auth_db("db_user") + " -p" + auth_db("db_password") + " " + auth_db("db_name") + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + auth_db("db_name") + ".sql"
    os.system(dumpcmd)
    log.info("compressing dump file ... ")
    gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + auth_db("db_name") + ".sql"
    os.system(gzipcmd)
    log.info("Backup script completed")
    log.info("Your backups have been created in '" + TODAYBACKUPPATH + "' directory")


if __name__ == '__main__':
    backup()
