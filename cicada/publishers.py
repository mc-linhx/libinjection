import logging
import os
import subprocess

class PublishArtifact(object):
    """
    Publish console ouput

    artifct is relative to workspace directory
    href/linktext is made for future linking
    """

    def __init__(self, artifact, destination, href, linktext):
        self.artifact = artifact
        self.destination = destination
        self.href = href
        self.linktext = linktext

    def link(self):
        return (self.href, self.linktext)

    def run(self, workspace, project, jobname, start):
        destdir = os.path.join(self.destination, project, jobname, str(start));
        latestdir = os.path.join(self.destination, project, jobname, 'latest');
        if not os.path.exists(destdir):
            os.makedirs(destdir)
        sourcedir = os.path.join(workspace, self.artifact)
        logging.info('Copying {0} to {1}'.format(sourcedir, destdir))
        subprocess.call(['cp', '-r', sourcedir, destdir])

        # portable? link to latest
        subprocess.call(['rm', '-rf', latestdir])
        subprocess.call(['ln', '-s', destdir, latestidr])

