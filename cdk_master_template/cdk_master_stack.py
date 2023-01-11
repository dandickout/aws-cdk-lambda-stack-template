from constructs import Construct
import os
from pathlib import Path
from dotenv import load_dotenv
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_ec2 as ec2,
    RemovalPolicy as RemovalPolicy,
)


#get the current working path for the .env should be in
dotenv_path = Path(os.getcwd() + '/.env')
load_dotenv(dotenv_path=dotenv_path)

#Get the MongoDB connection string from the .env file
MONGODB_URI = os.getenv('MONGODB_URI')
DECIMAL_PLACES = os.getenv('DECIMAL_PLACES')

class CDKMasterStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Define the layers we want to include
        
        #to install packages in the layer folder run:
        #pip install boto3 --target 'PATH\layer-python\python\'
        
        #CURRENT LIST OF INSTALLED PACKAGES:
        # boto3
        # pymongo
        # jinja2
        # pdfkit
        # haversine
        # wkhtmltopdf
 
        python_layer = _lambda.LayerVersion(
            self, 
            'layer-python-core', 
            code= _lambda.Code.from_asset("layer-python"),
            description='boto3, pymongo, jinja2, pdfkit, haversine, wkhtmltopdf',
            compatible_runtimes=[
                _lambda.Runtime.PYTHON_3_6,
                _lambda.Runtime.PYTHON_3_7,
                _lambda.Runtime.PYTHON_3_8,
                _lambda.Runtime.PYTHON_3_9
                ],
            layer_version_name='layer-python-core',
            removal_policy=RemovalPolicy.DESTROY,
        )

        #Get the role for the lambda functions
        app_method_service_role = iam.Role.from_role_arn(
            self, 
            'app-method-service-role',
            'arn:aws:iam::YOUR_ACCOUNT:role/app-method-service-role')
        
        #Get the VPC and Security Groups for the lambda functions
        mongo_vpc = ec2.Vpc.from_lookup(
            self, 
            id='Mongo Peering', 
            vpc_id='VPC_ID',)
        
        mongo_sec_groups = [
            ec2.SecurityGroup.from_security_group_id(
                self, 
                'mongodb-sg',
                security_group_id='SECURITYGROUP_ID'),
            ec2.SecurityGroup.from_security_group_id(
                self, 
                'lambda-sg',
                security_group_id='SECURITYGROUP_ID'),
            ]

        #Set the environment variables for the lambda functions
        env_vars = {
            "MONGO_URL": MONGODB_URI,
            "MONGODB": "app_sources",
            "DECIMAL_PLACES": DECIMAL_PLACES}


        #=======================================================================================
        #-----------------------------Python METHODS--------------------------------------------
        #=======================================================================================

        #method_1
        method_1 = _lambda.Function(
            self, 'method_1',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambdas-python/method_1'),
            handler='method_1.lambda_handler',
            function_name='method_1',
            layers=[python_layer],
            environment=env_vars,
            role=app_method_service_role,
            allow_public_subnet=True,
            vpc=mongo_vpc,
            security_groups=mongo_sec_groups
        )
        
        #method_2
        method_2 = _lambda.Function(
            self, 'method_2',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambdas-python/method_2'),
            handler='method_2.lambda_handler',
            function_name='method_2',
            layers=[python_layer],
            environment=env_vars,
            role=app_method_service_role,
            allow_public_subnet=True,
            vpc=mongo_vpc,
            security_groups=mongo_sec_groups
        )

        #=======================================================================================
        #-----------------------------NodeJS APIs-----------------------------------------------
        #=======================================================================================

        
