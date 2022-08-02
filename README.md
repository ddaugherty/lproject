# Looker Project Utility : lproject (installable version)

## Usage: 
### Copy Project
```
lproject copy {project_name}
```
### Copy folder and User defined dashboards
```
lproject copy --folder_name={name of folder}
```
### Combined
```
lproject copy {project_name} --folder_name={name of folder}
```

This is use a source and destination instance as defined by [Source] and [Destination] in the looker.ini config file by default. 
It will also use the default GitHub API Token and GitHub Organization as defined by GITHUB_API_TOKEN and GITHUB_ORG in the .env file.

### Flags
```
--project_id    : The ID of the project to copy, optinoal if id passed after copy command
--source        : The source Looker instance to copy from as labled in the looker.ini config file.
--destination   : The destination Looker instance to copy from as labled in the looker.ini config file.

i.e. lproject copy --project_id=customer_progect --source=Development --destination=Production 
```

### Future Enhancements: 
```
branch = "main" | "master", unless passed through --branch flag
Change project ID / Name at destination 
Chose specifc source repo branch / tag to copy 
force (overwrite destination project)
```

## Installation 

### Option 1:
 Clone this repo, run: 

```pip3 install -r requirements.txt```

### Option 2:
Copy the whl file from /dist/LookerProjectUtility*.whl to a local directory.

### 

```pip3 install -m Looker``` 


## Setup
### looker.ini 
#### Label names are arbitrary but [Source] and [Destination] will be used as defaults if included.
```
[Source]
base_url=https://
client_id=r
client_secret=
verify_ssl=True

[Destination]
base_url=https://
client_id=
client_secret=
verify_ssl=True
```

### .env
```
GITHUB_API_TOKEN= {token}
GITHUB_ORG= {GitHub Organization}
```

### Python Dependencies
- python-dotenv 
- PyGithub 
- looker-sdk 

