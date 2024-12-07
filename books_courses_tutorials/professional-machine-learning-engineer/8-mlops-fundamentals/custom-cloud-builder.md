# Custom Cloud Builder



Cloud Build > Doc. > Guides > [Using community-contributed builders and custom builders](https://cloud.google.com/build/docs/configuring-builds/use-community-and-custom-builders), [Creating a custom builder](https://cloud.google.com/build/docs/configuring-builds/use-community-and-custom-builders#creating_a_custom_builder)

Build your own image if you need more than 

- pre-built 
- community-contributed builders

Examples include when you need to

- download source code or packages from external locations,
- use an external tool chain,
- cache any necessary libraries,
- pre-build source (with Cloud Build responsible only for potentially packaging the build into an image).



## 1. Create a custom builder image

1-1. Create the `Dockerfile`. For example,

```dockerfile
  FROM alpine
  RUN apk add curl
  CMD curl https://httpbin.org/ip -s > myip.txt; echo "*** My IP is: $(cat myip.txt)"
```

1-2. Build and push the image

```bash
  gcloud builds submit --tag gcr.io/project-id/image-name
```

- gcr (Google Container Repository)
- `project-id` is used instead of `cloud-builders`.

## 2. Use the customer built image

Specify the builder in the `name` field of a build step:

```yaml
    steps:
    - name: 'gcr.io/project-id/image-name'
      id: Determine IP of this build worker
```



