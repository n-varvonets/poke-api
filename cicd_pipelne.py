"""We need"""
# 1. AWS IAM User AWS Access Key and AWS Key with privileges:
#       - S3 Full Access
#       - Elastic Beanstalk Full Access
# 2. AWS S3 Bucket for storage Deployment Packages
# 3. AWS Elastic Beanstalk Application and Environment
"""Our pipeline"""
# Django local -> git remote repo -> github actions -> AWS : |
#                                                            - make package(build)
#                                                            - deploy this build to aws server(ElasticBeanstalk )



