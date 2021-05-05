# Flask_CI-CD

## File Structure

- Create src directory consisting of all application code
- Create test directory consisting of all the tests
- create requirements file consisting of all the requirements



## CI

- Create .github/workflows/python-app.yml file with CI/CD code
- the code in the yml file can have multiple jobs and for each job there are multiple tasks
- We will have once job and the tasks are
- - deep clone our repository from github to the ubuntu machine,
  - download and setup python on the machine, 
  - install the requirements.txt packages on the machine
  -  install pytest; export our src directory to python path; run the tests

## CD

- we can chose a cloud platform, (Heroku in this case) make sure it supports infrastructure as code
- Get the api keys to interact with the cloud account through code
- create an app on the cloud platform
- Upload the name of the app and the secret key in GitHub secrets
- in yml file
  - set environment variables of our secret key and heroku app name
  - If the status up and until the above process is true and the branch is main perform the below actions
  - Add link of the github repo of the heroku app as remote link to our project
  - push the code from main branch of our repo to main branch of heroku repo, Forcefully 







## Errors

- Make sure to remove linting checks if not required

