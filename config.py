import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://mfvwyllgqwiabj:95f8e274ebedbf79a8a83e177ca37615bc5bb8c63152d863cdf6627f8e531138@ec2-35-174-118-71.compute-1.amazonaws.com:5432/dv76fksc0gb6d
'
SQLALCHEMY_TRACK_MODIFICATIONS = False
