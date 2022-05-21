from git import Repo
import os
import shutil

count = 0
TOKEN = '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'
# URL = 'PranavHegde99/Movie-Ticket_ReactN'

with open("Reponame.txt", "r") as a_file:
  for line in a_file:
    URL = line.strip()
    REMOTE_URL = 'https://{0}:x-oauth-basic@github.com/{1}'.format((TOKEN),(URL)) 
    count +=1
    #   print(count)
    print(URL)
    print("Repo{}_cloned".format(count))
    DEST_NAME = 'Repository_{}'.format(count)
    cloned_repo = Repo.clone_from(REMOTE_URL, DEST_NAME)
    repo = Repo.init('Repository_{}'.format(count))
    
with open('Repository_{}\Reponame.txt'.format(count), 'w') as f:
    f.write('Created a new text file!')
    repo.index.add(['Reponame.txt'])
    repo.index.commit('commit_done.') #commiting
    origin = repo.remote(name='origin')
    origin.push()
    print("Push to origin")
    
    print("Total_Repos:{}".format(count))
# Pull request
    print("Pull Request")
    origin.pull()
    my_new_branch = repo.create_head('my_new_branch_Testing')
    my_new_branch.checkout()
    print(my_new_branch)
    
    
    
    # THis is comiting/push for git branch
# repo = Repo.init('Repository_{}'.format(count))
# with open('Repository_{}\Reponame2.txt'.format(count), 'w') as f:
#     f.write('Create a new text file!123')
#     repo.index.add(['Reponame.txt'])
#     # Provide a commit message
#     repo.index.commit('Initial commit_done.123')
#     origin = repo.remote(name='origin')
#     origin.push()
    
print("Value defined")

