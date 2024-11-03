# onebite_pizza_scraper

From here if you want to upload this to a lambda layer, zip lambda_function.py as well as pizzareview. 

You should be able to run this in the lambda after setting up the layer.

You should also download the necessary requirements for your Lambda to run from requirements.txt

Run the following docker command, and then zip the python file and upload it as a layer in Lambda.

```
docker run -v $(pwd):/var/task --entrypoint pip3 public.ecr.aws/lambda/python:3.12 \
    install --target ./python/lib/python3.12/site-packages \
    scrapy lxml cryptography --platform manylinux2014_x86_64 \
    --only-binary=:all: --no-cache-dir
```

Then run:

```
zip -r python.zip python/
```

Don't forget to change the timeout to ~1 minute, that's approximately how long it takes for the scraper to run.
