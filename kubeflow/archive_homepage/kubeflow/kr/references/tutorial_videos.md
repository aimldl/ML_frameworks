* Draft: 2020-07-10 (Fri)



Youtube search: kubernetes production



---------

[Introduction to Microservices, Docker, and Kubernetes](https://youtu.be/1xo-0gCVhTU), 2017-11-07, James Quigley

Learn the basics of Microservices, Docker, and Kubernetes. Code demo starts at [18:45](https://www.youtube.com/watch?v=1xo-0gCVhTU&t=1125s). I mess up the terminal for the first few minutes, but I fix it by [21:50](https://www.youtube.com/watch?v=1xo-0gCVhTU&t=1310s). Audio gets echoey a few times, but it goes away quickly. Sorry about that! 

Deployment YAML: [https://pastebin.com/rZa9Dm1w](https://www.youtube.com/redirect?q=https%3A%2F%2Fpastebin.com%2FrZa9Dm1w&event=video_description&v=1xo-0gCVhTU&redir_token=QUFFLUhqbkdKcFpEajViTjVtMHlzdUxGR2MxMWVUbjJkZ3xBQ3Jtc0trWXJSbTVhbVM0ajRFNC1LNzViQTZ0aEJXOG9MdXBxUzg2cTRNd0lUTmJsaGZ5eW5EWnZWVHNlelNiVFBGODFnVkM4akw0MjlINDAyUHJSZm9xVUNweTBzWjdOQ3lBYkF2VUhJSVJJeG5VTnZBSzZUNA%3D%3D) 

Dockerfile: [https://pastebin.com/SZA26rbg](https://www.youtube.com/redirect?q=https%3A%2F%2Fpastebin.com%2FSZA26rbg&event=video_description&v=1xo-0gCVhTU&redir_token=QUFFLUhqbllPMHQ5SGVjR2Naekh6dmxJX2dqd3dJY2ZTZ3xBQ3Jtc0tuTzRuajJpSm5sY2NEeVlCUmZPZ081Qm1wQkN6WFJoM1N6SGc2d1NwelpFendSODA3N2pxTkdFOXpPQWxtZlJrTkpYUnBWSC1UbWMxd1NxWjNXS2VCeGdiMWhQRDk4cngwOG5kbDViTjkySG4wbHFIVQ%3D%3D) 

How to Containerize a Node App: [https://nodejs.org/en/docs/guides/nod...](https://www.youtube.com/redirect?q=https%3A%2F%2Fnodejs.org%2Fen%2Fdocs%2Fguides%2Fnodejs-docker-webapp%2F&event=video_description&v=1xo-0gCVhTU&redir_token=QUFFLUhqbEhxajZKejVWSTBVQ3hBaG5GYXVwZFZYNmhUZ3xBQ3Jtc0tsT2NUd1drcDdObzEwQ2pZTmdtUTltRUFzNmVqUTZ5LVU1cm5USkt5TGhyaGtnR1pnNVV0T2hnTzVtRzFPUF83LWZBNGM3ZGlxVDJUYl9RUWp1ZmJPOHM4cDl0NGZ4NFpBUEZONEhmX3Q5YWJ6Q2l6MA%3D%3D) 

Package-lock Blog Post: [https://medium.com/@Quigley_Ja/everyt...](https://www.youtube.com/redirect?q=https%3A%2F%2Fmedium.com%2F%40Quigley_Ja%2Feverything-you-wanted-to-know-about-package-lock-json-b81911aa8ab8&event=video_description&v=1xo-0gCVhTU&redir_token=QUFFLUhqbnpaZjRhTVpwbm5IQUdjYWs0REtfQkZvOXpUd3xBQ3Jtc0ttY3k2ZEliNlpHRTNWS3FwY0cyTWxyY0ppU2hpT2FnX0ExN05NYTkzRlExQV83OG9seFk2VEEteF90cXJTU3BvZG1pVTA1VmhqVUlPVWV1amNMOGJtZEhkb1o2OGFNOXRtYmhDeEs3ZFNqQThDaHhXZw%3D%3D)

-------

[What Does “Production Ready” Really Mean for a Kubernetes Cluster? - Lucas Käldström](https://youtu.be/EjSiZgGdRqk) [34:34], 2018-05-06, CNCF [Cloud Native Computing Foundation]

How would you describe and set up a “production ready” Kubernetes cluster? How are the buzzword terms “production ready” and “highly available” defined anyway? Can a cluster be created so that it’s end-to-end secured, has no single points of failure, is upgradable without control plane downtime and is conformant? If you have access to automated infrastructure, e.g. via a Cluster API controller, you should be able to do CI testing of your cluster, as well as CD of new configuration and versions. Some call this pattern “GitOps”; to write the desired cluster state declaratively and let a controller reconcile the cluster state. By the end of this talk, you should be able to tell: - What you may consider a “production ready” cluster to be and identify the moving parts - How to secure cluster component traffic - How to minimize failure points - How to manage clusters using the Cluster API

--------

