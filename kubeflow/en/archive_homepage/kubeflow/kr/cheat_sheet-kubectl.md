* Draft: 2020-07-28 (Tue)
# Cheat Sheet: Kubectl
TODO: add more example commands below.

## `kubectl get pods`

### The `-n` or `--namespace` option
#### `kubectl get pods -n kube-system`
#### `kubectl get pods --namespace=kube-system`
The output is same with the `-n` and `--namespace` options.

```bash
$ kubectl get pods -n kube-system
NAME                                                    READY   STATUS    RESTARTS   AGE
calico-kube-controllers-65f8bc95db-94mwb                1/1     Running   2          21h
   ...
kube-scheduler-k8smaster-alienware-aurora-r6            1/1     Running   2          21h
$
```
The full version is below.
```bash
$ kubectl get pods --namespace=kube-system
NAME                                                    READY   STATUS    RESTARTS   AGE
calico-kube-controllers-65f8bc95db-94mwb                1/1     Running   2          21h
calico-node-27z8b                                       1/1     Running   1          20h
calico-node-bqbcw                                       1/1     Running   1          21h
calico-node-mc6sh                                       1/1     Running   2          21h
coredns-66bff467f8-hb9rx                                1/1     Running   2          21h
coredns-66bff467f8-x5xnq                                1/1     Running   2          21h
etcd-k8smaster-alienware-aurora-r6                      1/1     Running   4          21h
kube-apiserver-k8smaster-alienware-aurora-r6            1/1     Running   4          21h
kube-controller-manager-k8smaster-alienware-aurora-r6   1/1     Running   2          21h
kube-proxy-4lplg                                        1/1     Running   3          21h
kube-proxy-7gns9                                        1/1     Running   1          20h
kube-proxy-pm428                                        1/1     Running   1          21h
kube-scheduler-k8smaster-alienware-aurora-r6            1/1     Running   2          21h
$
```

### The `-o` option
The IP address of the machine is 123.456.7.890 in this example. The pods with this IP address are shown except the first line.
```bash
$ kubectl get pods -n kube-system -o wide
NAME                                                    READY   STATUS    RESTARTS   AGE   IP              NODE                            NOMINATED NODE   READINESS GATES
calico-kube-controllers-65f8bc95db-94mwb                1/1     Running   2          21h   234.56.789.01   k8smaster-alienware-aurora-r6   <none>           <none>
  ...
calico-node-mc6sh                                       1/1     Running   2          21h   123.456.7.890   k8smaster-alienware-aurora-r6   <none>           <none>
  ...
etcd-k8smaster-alienware-aurora-r6                      1/1     Running   4          21h   123.456.7.890   k8smaster-alienware-aurora-r6   <none>           <none>
kube-apiserver-k8smaster-alienware-aurora-r6            1/1     Running   4          21h   123.456.7.890   k8smaster-alienware-aurora-r6   <none>           <none>
kube-controller-manager-k8smaster-alienware-aurora-r6   1/1     Running   2          21h   123.456.7.890   k8smaster-alienware-aurora-r6   <none>           <none>
kube-proxy-4lplg                                        1/1     Running   3          21h   123.456.7.890   k8smaster-alienware-aurora-r6   <none>           <none>
  ...
kube-scheduler-k8smaster-alienware-aurora-r6            1/1     Running   2          21h   123.456.7.890   k8smaster-alienware-aurora-r6   <none>           <none>
$
```
