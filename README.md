# Simple Concourse Python Pipeline

## Tutorial

Login to Concourse

```sh
fly -t tutorial login -c http://localhost:8080 -u test -p test
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
