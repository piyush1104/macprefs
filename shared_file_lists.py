from utils import copy_files, ensure_dir_owned_by_user
import config


def backup():
    print ''
    print 'Backing up shared file lists...'
    source = config.get_shared_file_lists_dir()
    dest = config.get_shared_file_lists_backup_dir()
    copy_files(source, dest)


def restore():
    print ''
    print 'Restoring shared file lists...'
    dest = config.get_shared_file_lists_dir()
    source = config.get_shared_file_lists_backup_dir()
    copy_files(source, dest, with_sudo=True, as_archive=False, as_dir=True)
    ensure_dir_owned_by_user(dest, config.get_user())
