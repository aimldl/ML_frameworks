* Draft: 2020-04-16 (Thu)
* References: [Set Up Your Notebooks](https://www.kubeflow.org/docs/notebooks/setup/)
* TODO: Document the reference to this .md file.

# Using Jupyter Notebooks with Kubeflow



When you bundle Jupyter notebooks in Kubeflow, you can use the Fairing  library to submit training jobs using TFJob. The training job can run  single node or distributed on the same Kubernetes cluster, but not  inside the notebook pod itself. 

Your Kubeflow deployment includes services for spawning and managing Jupyter notebooks.

You can set up multiple *notebook servers* per Kubeflow deployment. Each notebook server can include multiple *notebooks*. Each notebook server belongs to a single *namespace*, which corresponds to the project group or team for that server.



## How to set up a notebook server

1. Follow the [Kubeflow getting-started guide](https://www.kubeflow.org/docs/started/getting-started/) to set up your Kubeflow deployment and open the Kubeflow UI.
2. Click **Notebook Servers** in the left-hand panel of the Kubeflow UI.
3. Choose the **namespace** corresponding to your Kubeflow profile.
4. Click **NEW SERVER** to create a notebook server.
5. When the notebook server provisioning is complete, click **CONNECT**.
6. Click **Upload** to upload an existing notebook, or click **New** to create an empty notebook.

