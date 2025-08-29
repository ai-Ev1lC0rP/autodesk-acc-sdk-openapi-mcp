# Autodesk ACC SDK MCP

This repository hosts Autodesk Platform Services OpenAPI specifications and provides a Python-based Model Context Protocol (MCP) client that dynamically exposes every API endpoint.

## Setup

Follow the detailed [setup instructions](docs/claude_setup.md) to install dependencies and instantiate the client.

## Endpoint Checklist
Run `python scripts/update_readme_checklist.py` to refresh these statuses from the OpenAPI specs.
### authentication

- [x] `GET /.well-known/openid-configuration`
- [x] `GET /authentication/v2/authorize`
- [x] `GET /authentication/v2/keys`
- [x] `GET /authentication/v2/logout`
- [x] `GET /userinfo`
- [x] `POST /authentication/v2/introspect`
- [x] `POST /authentication/v2/revoke`
- [x] `POST /authentication/v2/token`

### construction/accountadmin

- [x] `DELETE /construction/admin/v1/projects/{projectId}/users/{userId}`
- [x] `GET /construction/admin/v1/accounts/{accountId}/companies`
- [x] `GET /construction/admin/v1/accounts/{accountId}/projects`
- [x] `GET /construction/admin/v1/accounts/{accountId}/users/{userId}/projects`
- [x] `GET /construction/admin/v1/projects/{projectId}`
- [x] `GET /construction/admin/v1/projects/{projectId}/users`
- [x] `GET /construction/admin/v1/projects/{projectId}/users/{userId}`
- [x] `GET /hq/v1/accounts/{account_id}/business_units_structure`
- [x] `GET /hq/v1/accounts/{account_id}/companies`
- [x] `GET /hq/v1/accounts/{account_id}/companies/search`
- [x] `GET /hq/v1/accounts/{account_id}/companies/{company_id}`
- [x] `GET /hq/v1/accounts/{account_id}/projects/{project_id}/companies`
- [x] `GET /hq/v1/accounts/{account_id}/users`
- [x] `GET /hq/v1/accounts/{account_id}/users/search`
- [x] `GET /hq/v1/accounts/{account_id}/users/{user_id}`
- [x] `PATCH /construction/admin/v1/projects/{projectId}/users/{userId}`
- [x] `PATCH /hq/v1/accounts/{account_id}/companies/{company_id}`
- [x] `PATCH /hq/v1/accounts/{account_id}/companies/{company_id}/image`
- [x] `PATCH /hq/v1/accounts/{account_id}/projects/{project_id}/image`
- [x] `PATCH /hq/v1/accounts/{account_id}/users/{user_id}`
- [x] `POST /construction/admin/v1/accounts/{accountId}/projects`
- [x] `POST /construction/admin/v1/projects/{projectId}/users`
- [x] `POST /construction/admin/v2/projects/{projectId}/users:import`
- [x] `POST /hq/v1/accounts/{account_id}/companies`
- [x] `POST /hq/v1/accounts/{account_id}/companies/import`
- [x] `POST /hq/v1/accounts/{account_id}/users`
- [x] `POST /hq/v1/accounts/{account_id}/users/import`
- [x] `PUT /hq/v1/accounts/{account_id}/business_units_structure`

### construction/issues

- [x] `GET /construction/issues/v1/projects/{projectId}/issue-attribute-definitions`
- [x] `GET /construction/issues/v1/projects/{projectId}/issue-attribute-mappings`
- [x] `GET /construction/issues/v1/projects/{projectId}/issue-root-cause-categories`
- [x] `GET /construction/issues/v1/projects/{projectId}/issue-types`
- [x] `GET /construction/issues/v1/projects/{projectId}/issues`
- [x] `GET /construction/issues/v1/projects/{projectId}/issues/{issueId}`
- [x] `GET /construction/issues/v1/projects/{projectId}/issues/{issueId}/comments`
- [x] `GET /construction/issues/v1/projects/{projectId}/users/me`
- [x] `PATCH /construction/issues/v1/projects/{projectId}/issues/{issueId}`
- [x] `POST /construction/issues/v1/projects/{projectId}/issues`
- [x] `POST /construction/issues/v1/projects/{projectId}/issues/{issueId}/comments`

### datamanagement

- [x] `GET /data/v1/projects/{project_id}/downloads/{download_id}`
- [x] `GET /data/v1/projects/{project_id}/folders/{folder_id}`
- [x] `GET /data/v1/projects/{project_id}/folders/{folder_id}/contents`
- [x] `GET /data/v1/projects/{project_id}/folders/{folder_id}/parent`
- [x] `GET /data/v1/projects/{project_id}/folders/{folder_id}/refs`
- [x] `GET /data/v1/projects/{project_id}/folders/{folder_id}/relationships/links`
- [x] `GET /data/v1/projects/{project_id}/folders/{folder_id}/relationships/refs`
- [x] `GET /data/v1/projects/{project_id}/folders/{folder_id}/search`
- [x] `GET /data/v1/projects/{project_id}/items/{item_id}`
- [x] `GET /data/v1/projects/{project_id}/items/{item_id}/parent`
- [x] `GET /data/v1/projects/{project_id}/items/{item_id}/refs`
- [x] `GET /data/v1/projects/{project_id}/items/{item_id}/relationships/links`
- [x] `GET /data/v1/projects/{project_id}/items/{item_id}/relationships/refs`
- [x] `GET /data/v1/projects/{project_id}/items/{item_id}/tip`
- [x] `GET /data/v1/projects/{project_id}/items/{item_id}/versions`
- [x] `GET /data/v1/projects/{project_id}/jobs/{job_id}`
- [x] `GET /data/v1/projects/{project_id}/versions/{version_id}`
- [x] `GET /data/v1/projects/{project_id}/versions/{version_id}/downloadFormats`
- [x] `GET /data/v1/projects/{project_id}/versions/{version_id}/downloads`
- [x] `GET /data/v1/projects/{project_id}/versions/{version_id}/item`
- [x] `GET /data/v1/projects/{project_id}/versions/{version_id}/refs`
- [x] `GET /data/v1/projects/{project_id}/versions/{version_id}/relationships/refs`
- [x] `GET /project/v1/hubs`
- [x] `GET /project/v1/hubs/{hub_id}`
- [x] `GET /project/v1/hubs/{hub_id}/projects`
- [x] `GET /project/v1/hubs/{hub_id}/projects/{project_id}`
- [x] `GET /project/v1/hubs/{hub_id}/projects/{project_id}/hub`
- [x] `GET /project/v1/hubs/{hub_id}/projects/{project_id}/topFolders`
- [x] `GET /projects/{project_id}/versions/{version_id}/relationships/links`
- [x] `PATCH /data/v1/projects/{project_id}/folders/{folder_id}`
- [x] `PATCH /data/v1/projects/{project_id}/items/{item_id}`
- [x] `PATCH /data/v1/projects/{project_id}/versions/{version_id}`
- [x] `POST /data/v1/projects/{project_id}/commands`
- [x] `POST /data/v1/projects/{project_id}/downloads`
- [x] `POST /data/v1/projects/{project_id}/folders`
- [x] `POST /data/v1/projects/{project_id}/folders/{folder_id}/relationships/refs`
- [x] `POST /data/v1/projects/{project_id}/items`
- [x] `POST /data/v1/projects/{project_id}/items/{item_id}/relationships/refs`
- [x] `POST /data/v1/projects/{project_id}/storage`
- [x] `POST /data/v1/projects/{project_id}/versions`
- [x] `POST /data/v1/projects/{project_id}/versions/{version_id}/relationships/refs`

### modelderivative

- [x] `DELETE /modelderivative/v2/designdata/{urn}/manifest`
- [x] `GET /modelderivative/v2/designdata/formats`
- [x] `GET /modelderivative/v2/designdata/{urn}/manifest`
- [x] `GET /modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}/signedcookies`
- [x] `GET /modelderivative/v2/designdata/{urn}/metadata`
- [x] `GET /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}`
- [x] `GET /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties`
- [x] `GET /modelderivative/v2/designdata/{urn}/thumbnail`
- [x] `HEAD /modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}`
- [x] `POST /modelderivative/v2/designdata/job`
- [x] `POST /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties:query`
- [x] `POST /modelderivative/v2/designdata/{urn}/references`

### oss

- [x] `DELETE /oss/v2/buckets/{bucketKey}`
- [x] `DELETE /oss/v2/buckets/{bucketKey}/objects/{objectKey}`
- [x] `DELETE /oss/v2/signedresources/{hash}`
- [x] `GET /oss/v2/buckets`
- [x] `GET /oss/v2/buckets/{bucketKey}/details`
- [x] `GET /oss/v2/buckets/{bucketKey}/objects`
- [x] `GET /oss/v2/buckets/{bucketKey}/objects/{objectKey}/details`
- [x] `GET /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3download`
- [x] `GET /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3upload`
- [x] `GET /oss/v2/signedresources/{hash}`
- [x] `POST /oss/v2/buckets`
- [x] `POST /oss/v2/buckets/{bucketKey}/objects/batchcompleteupload`
- [x] `POST /oss/v2/buckets/{bucketKey}/objects/batchsigneds3download`
- [x] `POST /oss/v2/buckets/{bucketKey}/objects/batchsigneds3upload`
- [x] `POST /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signed`
- [x] `POST /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3upload`
- [x] `PUT /oss/v2/buckets/{bucketKey}/objects/{objectKey}/copyto/{newObjKey}`
- [x] `PUT /oss/v2/signedresources/{hash}`
- [x] `PUT /oss/v2/signedresources/{hash}/resumable`

### webhooks

- [x] `DELETE /webhooks/v1/systems/{system}/events/{event}/hooks/{hook_id}`
- [x] `DELETE /webhooks/v1/tokens/@me`
- [x] `GET /webhooks/v1/app/hooks`
- [x] `GET /webhooks/v1/hooks`
- [x] `GET /webhooks/v1/systems/{system}/events/{event}/hooks`
- [x] `GET /webhooks/v1/systems/{system}/events/{event}/hooks/{hook_id}`
- [x] `GET /webhooks/v1/systems/{system}/hooks`
- [x] `PATCH /webhooks/v1/systems/{system}/events/{event}/hooks/{hook_id}`
- [x] `POST /webhooks/v1/systems/{system}/events/{event}/hooks`
- [x] `POST /webhooks/v1/systems/{system}/hooks`
- [x] `POST /webhooks/v1/tokens`
- [x] `PUT /webhooks/v1/tokens/@me`

## License

Licensed under the [Apache License](LICENSE).
