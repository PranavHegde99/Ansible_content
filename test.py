from turtle import clone
import git

# `git init new_repo`
new_repo = git.Repo.init('new_repo')
username = 'PranavHegde99'
pswd = 'Testpranav@123'
gittoken="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"
my_repo = git.Repo('new_repo')

# git.Git().clone("https://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@github.com/PranavHegde99/Movie-Ticket_ReactN.git")
print("cloning is done")
# https://github.com/PranavHegde99/Movie-Ticket_ReactN.git
# git.Repo.clone_from('https://github.com/Virtual-E-Dressing/VirtualEDressing.git','Cookbook-https')
# git clone https://Test123@github.com/PranavHegde99/Movie-Ticket_ReactN.git
git.Git().clone("https://{username}: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@github.com/PranavHegde99/Movie-Ticket_ReactN.git")


