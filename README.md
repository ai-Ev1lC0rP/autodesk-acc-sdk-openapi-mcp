# Autodesk ACC SDK MCP

This repository hosts Autodesk Platform Services OpenAPI specifications and provides a Python-based Model Context Protocol (MCP) client that dynamically exposes every API endpoint.

## Setup

Follow the detailed [setup instructions](docs/claude_setup.md) to install dependencies and instantiate the client.

## Endpoint Checklist
### authentication

- [ ] `GET /.well-known/openid-configuration`
- [ ] `GET /authentication/v2/authorize`
- [ ] `GET /authentication/v2/keys`
- [ ] `GET /authentication/v2/logout`
- [ ] `GET /userinfo`
- [ ] `POST /authentication/v2/introspect`
- [ ] `POST /authentication/v2/revoke`
- [ ] `POST /authentication/v2/token`

### construction/accountadmin

- [ ] `DELETE /construction/admin/v1/projects/{projectId}/users/{userId}`
- [ ] `GET /construction/admin/v1/accounts/{accountId}/companies`
- [ ] `GET /construction/admin/v1/accounts/{accountId}/projects`
- [ ] `GET /construction/admin/v1/accounts/{accountId}/users/{userId}/projects`
- [ ] `GET /construction/admin/v1/projects/{projectId}`
- [ ] `GET /construction/admin/v1/projects/{projectId}/users`
- [ ] `GET /construction/admin/v1/projects/{projectId}/users/{userId}`
- [ ] `GET /hq/v1/accounts/{account_id}/business_units_structure`
- [ ] `GET /hq/v1/accounts/{account_id}/companies`
- [ ] `GET /hq/v1/accounts/{account_id}/companies/search`
- [ ] `GET /hq/v1/accounts/{account_id}/companies/{company_id}`
- [ ] `GET /hq/v1/accounts/{account_id}/projects/{project_id}/companies`
- [ ] `GET /hq/v1/accounts/{account_id}/users`
- [ ] `GET /hq/v1/accounts/{account_id}/users/search`
- [ ] `GET /hq/v1/accounts/{account_id}/users/{user_id}`
- [ ] `PATCH /construction/admin/v1/projects/{projectId}/users/{userId}`
- [ ] `PATCH /hq/v1/accounts/{account_id}/companies/{company_id}`
- [ ] `PATCH /hq/v1/accounts/{account_id}/companies/{company_id}/image`
- [ ] `PATCH /hq/v1/accounts/{account_id}/projects/{project_id}/image`
- [ ] `PATCH /hq/v1/accounts/{account_id}/users/{user_id}`
- [ ] `POST /construction/admin/v1/accounts/{accountId}/projects`
- [ ] `POST /construction/admin/v1/projects/{projectId}/users`
- [ ] `POST /construction/admin/v2/projects/{projectId}/users:import`
- [ ] `POST /hq/v1/accounts/{account_id}/companies`
- [ ] `POST /hq/v1/accounts/{account_id}/companies/import`
- [ ] `POST /hq/v1/accounts/{account_id}/users`
- [ ] `POST /hq/v1/accounts/{account_id}/users/import`
- [ ] `PUT /hq/v1/accounts/{account_id}/business_units_structure`

### construction/issues

- [ ] `GET /construction/issues/v1/projects/{projectId}/issue-attribute-definitions`
- [ ] `GET /construction/issues/v1/projects/{projectId}/issue-attribute-mappings`
- [ ] `GET /construction/issues/v1/projects/{projectId}/issue-root-cause-categories`
- [ ] `GET /construction/issues/v1/projects/{projectId}/issue-types`
- [ ] `GET /construction/issues/v1/projects/{projectId}/issues`
- [ ] `GET /construction/issues/v1/projects/{projectId}/issues/{issueId}`
- [ ] `GET /construction/issues/v1/projects/{projectId}/issues/{issueId}/comments`
- [ ] `GET /construction/issues/v1/projects/{projectId}/users/me`
- [ ] `PATCH /construction/issues/v1/projects/{projectId}/issues/{issueId}`
- [ ] `POST /construction/issues/v1/projects/{projectId}/issues`
- [ ] `POST /construction/issues/v1/projects/{projectId}/issues/{issueId}/comments`

### datamanagement

- [ ] `GET /data/v1/projects/{project_id}/downloads/{download_id}`
- [ ] `GET /data/v1/projects/{project_id}/folders/{folder_id}`
- [ ] `GET /data/v1/projects/{project_id}/folders/{folder_id}/contents`
- [ ] `GET /data/v1/projects/{project_id}/folders/{folder_id}/parent`
- [ ] `GET /data/v1/projects/{project_id}/folders/{folder_id}/refs`
- [ ] `GET /data/v1/projects/{project_id}/folders/{folder_id}/relationships/links`
- [ ] `GET /data/v1/projects/{project_id}/folders/{folder_id}/relationships/refs`
- [ ] `GET /data/v1/projects/{project_id}/folders/{folder_id}/search`
- [ ] `GET /data/v1/projects/{project_id}/items/{item_id}`
- [ ] `GET /data/v1/projects/{project_id}/items/{item_id}/parent`
- [ ] `GET /data/v1/projects/{project_id}/items/{item_id}/refs`
- [ ] `GET /data/v1/projects/{project_id}/items/{item_id}/relationships/links`
- [ ] `GET /data/v1/projects/{project_id}/items/{item_id}/relationships/refs`
- [ ] `GET /data/v1/projects/{project_id}/items/{item_id}/tip`
- [ ] `GET /data/v1/projects/{project_id}/items/{item_id}/versions`
- [ ] `GET /data/v1/projects/{project_id}/jobs/{job_id}`
- [ ] `GET /data/v1/projects/{project_id}/versions/{version_id}`
- [ ] `GET /data/v1/projects/{project_id}/versions/{version_id}/downloadFormats`
- [ ] `GET /data/v1/projects/{project_id}/versions/{version_id}/downloads`
- [ ] `GET /data/v1/projects/{project_id}/versions/{version_id}/item`
- [ ] `GET /data/v1/projects/{project_id}/versions/{version_id}/refs`
- [ ] `GET /data/v1/projects/{project_id}/versions/{version_id}/relationships/refs`
- [ ] `GET /project/v1/hubs`
- [ ] `GET /project/v1/hubs/{hub_id}`
- [ ] `GET /project/v1/hubs/{hub_id}/projects`
- [ ] `GET /project/v1/hubs/{hub_id}/projects/{project_id}`
- [ ] `GET /project/v1/hubs/{hub_id}/projects/{project_id}/hub`
- [ ] `GET /project/v1/hubs/{hub_id}/projects/{project_id}/topFolders`
- [ ] `GET /projects/{project_id}/versions/{version_id}/relationships/links`
- [ ] `PATCH /data/v1/projects/{project_id}/folders/{folder_id}`
- [ ] `PATCH /data/v1/projects/{project_id}/items/{item_id}`
- [ ] `PATCH /data/v1/projects/{project_id}/versions/{version_id}`
- [ ] `POST /data/v1/projects/{project_id}/commands`
- [ ] `POST /data/v1/projects/{project_id}/downloads`
- [ ] `POST /data/v1/projects/{project_id}/folders`
- [ ] `POST /data/v1/projects/{project_id}/folders/{folder_id}/relationships/refs`
- [ ] `POST /data/v1/projects/{project_id}/items`
- [ ] `POST /data/v1/projects/{project_id}/items/{item_id}/relationships/refs`
- [ ] `POST /data/v1/projects/{project_id}/storage`
- [ ] `POST /data/v1/projects/{project_id}/versions`
- [ ] `POST /data/v1/projects/{project_id}/versions/{version_id}/relationships/refs`

### modelderivative

- [ ] `DELETE /modelderivative/v2/designdata/{urn}/manifest`
- [ ] `GET /modelderivative/v2/designdata/formats`
- [ ] `GET /modelderivative/v2/designdata/{urn}/manifest`
- [ ] `GET /modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}/signedcookies`
- [ ] `GET /modelderivative/v2/designdata/{urn}/metadata`
- [ ] `GET /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}`
- [ ] `GET /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties`
- [ ] `GET /modelderivative/v2/designdata/{urn}/thumbnail`
- [ ] `HEAD /modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}`
- [ ] `POST /modelderivative/v2/designdata/job`
- [ ] `POST /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties:query`
- [ ] `POST /modelderivative/v2/designdata/{urn}/references`

### oss

- [ ] `DELETE /oss/v2/buckets/{bucketKey}`
- [ ] `DELETE /oss/v2/buckets/{bucketKey}/objects/{objectKey}`
- [ ] `DELETE /oss/v2/signedresources/{hash}`
- [ ] `GET /oss/v2/buckets`
- [ ] `GET /oss/v2/buckets/{bucketKey}/details`
- [ ] `GET /oss/v2/buckets/{bucketKey}/objects`
- [ ] `GET /oss/v2/buckets/{bucketKey}/objects/{objectKey}/details`
- [ ] `GET /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3download`
- [ ] `GET /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3upload`
- [ ] `GET /oss/v2/signedresources/{hash}`
- [ ] `POST /oss/v2/buckets`
- [ ] `POST /oss/v2/buckets/{bucketKey}/objects/batchcompleteupload`
- [ ] `POST /oss/v2/buckets/{bucketKey}/objects/batchsigneds3download`
- [ ] `POST /oss/v2/buckets/{bucketKey}/objects/batchsigneds3upload`
- [ ] `POST /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signed`
- [ ] `POST /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3upload`
- [ ] `PUT /oss/v2/buckets/{bucketKey}/objects/{objectKey}/copyto/{newObjKey}`
- [ ] `PUT /oss/v2/signedresources/{hash}`
- [ ] `PUT /oss/v2/signedresources/{hash}/resumable`

### webhooks

- [ ] `DELETE /webhooks/v1/systems/{system}/events/{event}/hooks/{hook_id}`
- [ ] `DELETE /webhooks/v1/tokens/@me`
- [ ] `GET /webhooks/v1/app/hooks`
- [ ] `GET /webhooks/v1/hooks`
- [ ] `GET /webhooks/v1/systems/{system}/events/{event}/hooks`
- [ ] `GET /webhooks/v1/systems/{system}/events/{event}/hooks/{hook_id}`
- [ ] `GET /webhooks/v1/systems/{system}/hooks`
- [ ] `PATCH /webhooks/v1/systems/{system}/events/{event}/hooks/{hook_id}`
- [ ] `POST /webhooks/v1/systems/{system}/events/{event}/hooks`
- [ ] `POST /webhooks/v1/systems/{system}/hooks`
- [ ] `POST /webhooks/v1/tokens`
- [ ] `PUT /webhooks/v1/tokens/@me`

## License

Licensed under the [Apache License](LICENSE).
