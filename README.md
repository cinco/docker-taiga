# What is Taiga?

Taiga is a project management platform for startups and agile developers & designers who want a simple, beautiful tool that makes work truly enjoyable.

> [taiga.io](https://taiga.io)

# How to use this image

There is an example project available at [benhutchins/docker-taiga-example](https://github.com/benhutchins/docker-taiga-example) that provides base configuration files available for you to modify and allows you to easily install plugins. I recommend you clone this repo and modify the files, then use it's provided scripts to get started quickly.

    git clone https://github.com/benhutchins/docker-taiga-example.git mytaiga && cd mytaiga
    vi local.py # configuration for taiga-back
    vi conf.json # configuration for taiga-front
    TAIGA_HOSTNAME=taiga.mycompany.com ./start.sh
    # docker-compose up # There is a provided docker configuration file as well

Or to use this container directly, run:

    docker run -it --link some-postgres:postgres -p 80:80 -d benhutchins/taiga

Partial explanation of arguments:

- `--link` specifies the database container. See `Configure Database` below for more details.

Once your container is running, use the default administrator account to login: username is `admin`, and the password is `123123`.

If you're having trouble connecting, make sure you've configured your `TAIGA_HOSTNAME`. It will default to `localhost`, which almost certainly is not what you want to use.

## Extra configuration options

Use the following environmental variables to generate a `local.py` for [taiga-back](https://github.com/taigaio/taiga-back).

  - `-e TAIGA_HOSTNAME=` (**required** set this to the server host like `taiga.mycompany.com`)
  - `-e TAIGA_SSL=True` (set this to `True` if you want to enable SSL support within the container)
  - `-e TAIGA_SECRET_KEY` (set this to a random string to configures `SECRET_KEY`; defaults to an insecure random string)

## Configure Database

The above example uses `--link` to connect Taiga with a running [postgres](https://registry.hub.docker.com/_/postgres/) container. This is probably not the best idea for use in production, keeping data in docker containers can be dangerous.

### Using Docker container

If you want to run your database within a docker container, simply start your database server before starting your Taiga container. Here is a simple example pulled from [postgres](https://registry.hub.docker.com/_/postgres/)'s guide.

    docker run --name taiga-postgres -e POSTGRES_PASSWORD=mypassword -d postgres

### Using Database server

You can use the following environment variables for connecting to another database server:

 - `-e TAIGA_DB_NAME=...` (defaults to `postgres`)
 - `-e TAIGA_DB_HOST=...` (defaults to the address of a linked `postgres` container)
 - `-e TAIGA_DB_USER=...` (defaults to `postgres)`)
 - `-e TAIGA_DB_PASSWORD=...` (defaults to the password of the linked `postgres` container)

If the `TAIGA_DB_NAME` specified does not already exist on the provided PostgreSQL server, it will be automatically created the the Taiga's installation scripts will run to generate the required tables and default demo data.

An example `docker run` command using an external database:

    docker run \
      --name mytaiga \
      -e TAIGA_DB_HOST=10.0.0.1 \
      -e TAIGA_DB_USER=taiga \
      -e TAIGA_DB_PASSWORD=mypassword \
      -d \
      benhutchins/taiga