import os

# Database connection parameters
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')

# Storage options
STORAGE_TYPE = os.environ.get('STORAGE_TYPE')  # local, aws_s3, google_cloud_storage, azure_blob_storage
STORAGE_BUCKET = os.environ.get('STORAGE_BUCKET')

# Logging and notifications
LOG_LEVEL = os.environ.get('LOG_LEVEL')  # debug, info, warning, error
SLACK_NOTIFICATIONS = os.environ.get('SLACK_NOTIFICATIONS')  # True or False
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')

# Scheduling
SCHEDULE_BACKUP = os.environ.get('SCHEDULE_BACKUP')  # True or False
SCHEDULE_INTERVAL = os.environ.get('SCHEDULE_INTERVAL')  # daily, weekly, monthly

# Encryption
ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY')
