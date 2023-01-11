# NOTE: 
This code was all copied from production code I wrote but it has been obfuscated to protect IP so please excuse any errors or omissions

# This is a template master project for AWS CDK built lambda functions!

This stack (`cdk_master_stack`) creates a number of NodeJS APIs and Python calculation methods.

It also includes;

 * any python layers needed by the methods
 * connection to Mongo Atlas Peering VPC
    * along with the security groups and subnets associated with that VPC
 * environmental variables like the MongoDB name and connection string (from a .env file)
 * connection to the service roles associated with the lambdas

 Still to be done is to;
 
 * create and own the service role from within the project (currently just using an existing one)
 * add secrets management to the project to handle MongoDB connection string to remove dependancy on .env file
 * consolidate lambda configuration params into a single object to cut down code length
 * add dynamic logging and reporting (ie, datadog)
 * automate the s**t out of it ;)
    * automatically add new lambdas based on new methods being added to the spreadsheet
    * automate creation of Confluence pages
    * automate commit and push to bitbucket
        

# CDK usage instructions

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
