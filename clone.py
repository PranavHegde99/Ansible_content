# import git
# git.Git('C:\home\Pranav\PycharmProjects').clone('git@github.com:Stack-overflow-Ds/Data_Distribution_Analysis.git', token=('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'))


# # https://github.com/Stack-overflow-Ds/Data_Distribution_Analysis.git

import os

from github import Github

g = Github("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")
org = g.get_organization("Virtual-E-Dressing")
repos = org.get_repos("")

for repo in repos:
    cmd = "git clone {}".format(repo.ssh_url)
    print("Starting to clone {}".format(repo.name))
    print("Running command '{}'".format(cmd))
    os.system(cmd)
    print("Finshed cloning {}".format(repo.name))
    print("#####################################")
    print("")

    