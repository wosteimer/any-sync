#!/bin/bash

mc alias set minio $MINIO_URL $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD
mc mb minio/$MINIO_BUCKET
mc admin accesskey create               \
   minio                                \
   --access-key $AWS_ACCESS_KEY_ID      \
   --secret-key $AWS_SECRET_ACCESS_KEY  \


printf "[default]\naws_access_key_id=${AWS_ACCESS_KEY_ID}\naws_secret_access_key=${AWS_SECRET_ACCESS_KEY}\n" > \
       /aws/credentials
