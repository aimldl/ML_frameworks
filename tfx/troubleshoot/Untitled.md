



```bash
$

  ...
  Attempting uninstall: mock
    Found existing installation: mock 4.0.2
    Uninstalling mock-4.0.2:
      Successfully uninstalled mock-4.0.2
  Attempting uninstall: joblib
    Found existing installation: joblib 0.17.0
    Uninstalling joblib-0.17.0:
      Successfully uninstalled joblib-0.17.0
ERROR: After October 2020 you may experience errors when installing or updating packages. This is because pip will change the way that it resolves dependency conflicts.

We recommend you use --use-feature=2020-resolver to test your packages with the new resolver before it becomes the default.

tensorflow 2.3.2 requires numpy<1.19.0,>=1.16.0, but you'll have numpy 1.19.2 which is incompatible.
apache-beam 2.25.0 requires httplib2<0.18.0,>=0.8, but you'll have httplib2 0.18.1 which is incompatible.
  ...
$
```

ERROR
	We recommend you use --use-feature=2020-resolver to test your packages with the new resolver before it becomes the default
	tensorflow 2.3.2 requires numpy<1.19.0,>=1.16.0, but you'll have numpy 1.19.2 which is incompatible.
		->
			downgrade
				the version
	apache-beam 2.25.0 requires httplib2<0.18.0,>=0.8, but you'll have httplib2 0.18.1 which is incompatible.
		->
			downgrade
				the version