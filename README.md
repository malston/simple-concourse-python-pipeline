# Simple Concourse Python Pipeline

## Tutorial

Install `fly`

```sh
curl 'http://localhost:8080/api/v1/cli?arch=amd64&platform=darwin' -o fly
./fly --version
chmod +x ./fly
./fly --version
sudo mv ./fly /usr/local/bin/
```

Login

```sh
fly -t tutorial login -c http://localhost:8080 -u test -p test
```

Check workers

```sh
fly -t tutorial workers
```

Test python script

```sh
fly -t tutorial execute -c ci/tasks/hello-world.yml -i repo=.
```

Run pipeline

```sh
fly -t tutorial set-pipeline -p hello-world -c ci/hello-world.yml
fly -t tutorial unpause-pipeline -p hello-world
fly -t tutorial trigger-job --job hello-world/hello-world-job --watch
```

## Simple Python Pipeline

Execute python script

```sh
fly -t tutorial execute -c ci/simple-python-pipeline/task.yml -i repo=.
```
