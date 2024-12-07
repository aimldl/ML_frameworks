* Draft: 2020-08-31 (Mon)

# Google AutoML Zero

* Paper: [AutoML-Zero: Evolving Machine Learning Algorithms From Scratch](https://arxiv.org/pdf/2003.03384.pdf)
* Github repository: [google-research/automl_zero/](https://github.com/google-research/google-research/tree/master/automl_zero#5-minute-demo-discovering-linear-regression-from-scratch)
* Blog: [AutoML-Zero: Evolving Code that Learns](https://ai.googleblog.com/2020/07/automl-zero-evolving-code-that-learns.html), 2020-07-09

[The CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html)


## Git-clone the source codes.
```bashd
(base) $ mkdir temp
(base) $ cd temp/
(base) /temp$ git clone https://github.com/google-research/google-research.git
Cloning into 'google-research'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 19378 (delta 0), reused 4 (delta 0), pack-reused 19374
Receiving objects: 100% (19378/19378), 240.29 MiB | 18.18 MiB/s, done.
Resolving deltas: 100% (9283/9283), done.
Checking out files: 100% (7090/7090), done.
(base) /temp$ ls
google-research
(base) /temp$ cd google-research/
(base) /temp/google-research$ cd automl_zero/
(base) /temp/google-research/automl_zero$ ls
algorithm.cc            evaluator_test.cc        generate_datasets.py          memory_test.cc                 run_baseline.sh                                    task_util_test.cc
algorithm.h             executor.h               generator.cc                  mutator.cc                     run_demo.sh                                        test_util.h
algorithm.proto         executor_test.cc         generator.h                   mutator.h                      run_integration_test_linear.sh                     test_util_test.cc
algorithm_test.cc       experiment_progress.png  generator.proto               mutator.proto                  run_integration_test_nonlinear.sh                  train_budget.cc
algorithm_test_util.cc  experiment.proto         generator_test.cc             mutator_test.cc                run_integration_test_projected_binary_datasets.sh  train_budget.h
algorithm_test_util.h   experiment_util.cc       generator_test_util.cc        random_generator.cc            run_integration_tests.sh                           train_budget.proto
BUILD                   experiment_util.h        generator_test_util.h         random_generator.h             run_search_experiment.cc                           train_budget_test.cc
compute_cost.cc         fec_cache.cc             initial_and_evolved_code.png  random_generator_test.cc       setup.sh                                           util.cc
compute_cost.h          fec_cache.h              instruction.cc                randomizer.cc                  task.h                                             util.h
definitions.h           fec_cache.proto          instruction.h                 randomizer.h                   task_pb2.py                                        util_test.cc
definitions_test.cc     fec_cache_test.cc        instruction.proto             README.md                      task.proto                                         WORKSPACE
eigen.BUILD             fec_hashing.cc           instruction_test.cc           regularized_evolution.cc       task_test.cc
evaluator.cc            fec_hashing.h            memory.cc                     regularized_evolution.h        task_util.cc
evaluator.h             fec_hashing_test.cc      memory.h                      regularized_evolution_test.cc  task_util.h
(base) /temp/google-research/automl_zero$
```

### Install Bazel
For details, [Installing Bazel on Ubuntu](https://docs.bazel.build/versions/master/install-ubuntu.html).

```bash
(base) $ sudo apt install curl gnupg
[sudo] password for aimldl: 
Reading package lists... Done
  ...
(base) $ curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg
(base) $ sudo mv bazel.gpg /etc/apt/trusted.gpg.d/
(base) $ echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8
(base) $ sudo apt update && sudo apt install bazel
  ...
The following NEW packages will be installed:
  bazel
  ...
Do you want to continue? [Y/n] y
  ...
Processing triggers for libc-bin (2.27-3ubuntu1.2) ...
(base) $
```

Without bazel, `run_demo.sh` will output an error message.
```bash
(base) /temp/google-research/automl_zero$ ./run_demo.sh 
./run_demo.sh: line 20: bazel: command not found
```

## Execute "run_demo.sh"
```bash
(base) /temp/google-research/automl_zero$ ./run_demo.sh 
Extracting Bazel installation...
Starting local Bazel server and connecting to it...
INFO: SHA256 (https://github.com/bazelbuild/rules_cc/archive/master.zip) = 2a34fa56d923f774409d23720e60ddf6536e88622d000e6925f7cebbad65e281
DEBUG: Rule 'rules_cc' indicated that a canonical reproducible form can be obtained by modifying arguments sha256 = "2a34fa56d923f774409d23720e60ddf6536e88622d000e6925f7cebbad65e281"
DEBUG: Repository rules_cc instantiated at:
  no stack (--record_rule_instantiation_callstack not enabled)
Repository rule http_archive defined at:
  /home/aimldl/.cache/bazel/_bazel_aimldl/e5ca135dfca5a83e9d70cecb9ee27a18/external/bazel_tools/tools/build_defs/repo/http.bzl:336:31: in <toplevel>
INFO: SHA256 (https://github.com/abseil/abseil-cpp/archive/master.zip) = 1267113dc80757646592b3b79d18c7ce4132835fba6b7e3a38961f91109314c5
DEBUG: Rule 'com_google_absl' indicated that a canonical reproducible form can be obtained by modifying arguments sha256 = "1267113dc80757646592b3b79d18c7ce4132835fba6b7e3a38961f91109314c5"
DEBUG: Repository com_google_absl instantiated at:
  no stack (--record_rule_instantiation_callstack not enabled)
Repository rule http_archive defined at:
  /home/aimldl/.cache/bazel/_bazel_aimldl/e5ca135dfca5a83e9d70cecb9ee27a18/external/bazel_tools/tools/build_defs/repo/http.bzl:336:31: in <toplevel>
INFO: SHA256 (https://github.com/google/glog/archive/master.zip) = 144f10b8c60480ec7b9913109cb6d67f9c82828664f8ccd22b15c87034c5768e
DEBUG: Rule 'com_google_glog' indicated that a canonical reproducible form can be obtained by modifying arguments sha256 = "144f10b8c60480ec7b9913109cb6d67f9c82828664f8ccd22b15c87034c5768e"
DEBUG: Repository com_google_glog instantiated at:
  no stack (--record_rule_instantiation_callstack not enabled)
Repository rule http_archive defined at:
  /home/aimldl/.cache/bazel/_bazel_aimldl/e5ca135dfca5a83e9d70cecb9ee27a18/external/bazel_tools/tools/build_defs/repo/http.bzl:336:31: in <toplevel>
INFO: SHA256 (https://github.com/google/googletest/archive/master.zip) = 498bf0cba2467e181a6736a3a85ce6ac1b1b41b97dba52aee994180e008f968c
DEBUG: Rule 'com_google_googletest' indicated that a canonical reproducible form can be obtained by modifying arguments sha256 = "498bf0cba2467e181a6736a3a85ce6ac1b1b41b97dba52aee994180e008f968c"
DEBUG: Repository com_google_googletest instantiated at:
  no stack (--record_rule_instantiation_callstack not enabled)
Repository rule http_archive defined at:
  /home/aimldl/.cache/bazel/_bazel_aimldl/e5ca135dfca5a83e9d70cecb9ee27a18/external/bazel_tools/tools/build_defs/repo/http.bzl:336:31: in <toplevel>
INFO: SHA256 (https://github.com/gflags/gflags/archive/master.zip) = 9d163253531c42ab5a13cc8201c03f68f119b399f2dcb99075beb8650668d986
DEBUG: Rule 'com_github_gflags_gflags' indicated that a canonical reproducible form can be obtained by modifying arguments sha256 = "9d163253531c42ab5a13cc8201c03f68f119b399f2dcb99075beb8650668d986"
DEBUG: Repository com_github_gflags_gflags instantiated at:
  no stack (--record_rule_instantiation_callstack not enabled)
Repository rule http_archive defined at:
  /home/aimldl/.cache/bazel/_bazel_aimldl/e5ca135dfca5a83e9d70cecb9ee27a18/external/bazel_tools/tools/build_defs/repo/http.bzl:336:31: in <toplevel>
INFO: Analyzed target //:run_search_experiment (42 packages loaded, 1520 targets configured).
INFO: Found 1 target...
INFO: From Compiling algorithm.cc:
algorithm.cc: In member function 'const std::vector<std::shared_ptr<const automl_zero::Instruction> >& automl_zero::Algorithm::ComponentFunction(automl_zero::ComponentFunctionT) const':
algorithm.cc:172:1: warning: control reaches end of non-void function [-Wreturn-type]
 }
 ^
algorithm.cc: In member function 'std::vector<std::shared_ptr<const automl_zero::Instruction> >* automl_zero::Algorithm::MutableComponentFunction(automl_zero::ComponentFunctionT)':
algorithm.cc:184:1: warning: control reaches end of non-void function [-Wreturn-type]
 }
 ^
INFO: From Compiling compute_cost.cc:
compute_cost.cc: In function 'double automl_zero::ComputeCost(const automl_zero::Instruction&)':
compute_cost.cc:173:1: warning: control reaches end of non-void function [-Wreturn-type]
 }
 ^
INFO: From Compiling fec_cache.cc:
In file included from fec_cache.h:24:0,
                 from fec_cache.cc:15:
executor.h:803:10: warning: variable templates only available with -std=c++14 or -std=gnu++14
     128> kOpIndexToExecuteFunction = {
          ^~~~~~~~~~~~~~~~~~~~~~~~~
fec_cache.cc: In member function 'void automl_zero::LRUCache::MaybeResize()':
fec_cache.cc:92:23: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
   while (list_.size() > max_size_) {
          ~~~~~~~~~~~~~^~~~~~~~~~~
INFO: From Compiling mutator.cc:
mutator.cc: In member function 'void automl_zero::Mutator::InsertInstruction(automl_zero::Algorithm*)':
mutator.cc:253:36: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
       if (algorithm->setup_.size() >= setup_size_max_ - 1) return;
           ~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~
mutator.cc:259:38: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
       if (algorithm->predict_.size() >= predict_size_max_ - 1) return;
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
mutator.cc:265:36: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
       if (algorithm->learn_.size() >= learn_size_max_ - 1) return;
           ~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~
In file included from definitions.h:34:0,
                 from instruction.h:24,
                 from algorithm.h:24,
                 from mutator.h:21,
                 from mutator.cc:15:
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h: In instantiation of 'std::__cxx11::string* google::Check_GTImpl(const T1&, const T2&, const char*) [with T1 = long unsigned int; T2 = int; std::__cxx11::string = std::__cxx11::basic_string<char>]':
mutator.cc:343:3:   required from here
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:733:32: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
 DEFINE_CHECK_OP_IMPL(Check_GT, > )
                                ^
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:148:53: note: in definition of macro 'GOOGLE_PREDICT_TRUE'
 #define GOOGLE_PREDICT_TRUE(x) (__builtin_expect(!!(x), 1))
                                                     ^
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:733:1: note: in expansion of macro 'DEFINE_CHECK_OP_IMPL'
 DEFINE_CHECK_OP_IMPL(Check_GT, > )
 ^~~~~~~~~~~~~~~~~~~~
mutator.cc: In member function 'void automl_zero::Mutator::RemoveInstruction(automl_zero::Algorithm*)':
mutator.cc:293:35: warning: 'component_function' may be used uninitialized in this function [-Wmaybe-uninitialized]
   RemoveInstructionUnconditionally(component_function);
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
mutator.cc: In member function 'void automl_zero::Mutator::InsertInstruction(automl_zero::Algorithm*)':
mutator.cc:271:35: warning: 'component_function' may be used uninitialized in this function [-Wmaybe-uninitialized]
   InsertInstructionUnconditionally(op, component_function);
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
mutator.cc:271:35: warning: 'op' may be used uninitialized in this function [-Wmaybe-uninitialized]
mutator.cc: In member function 'void automl_zero::Mutator::TradeInstruction(automl_zero::Algorithm*)':
mutator.cc:317:35: warning: 'component_function' may be used uninitialized in this function [-Wmaybe-uninitialized]
   RemoveInstructionUnconditionally(component_function);
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
mutator.cc:316:35: warning: 'op' may be used uninitialized in this function [-Wmaybe-uninitialized]
   InsertInstructionUnconditionally(op, component_function);
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
INFO: From Compiling regularized_evolution.cc:
In file included from fec_cache.h:24:0,
                 from evaluator.h:28,
                 from regularized_evolution.h:26,
                 from regularized_evolution.cc:15:
executor.h:803:10: warning: variable templates only available with -std=c++14 or -std=gnu++14
     128> kOpIndexToExecuteFunction = {
          ^~~~~~~~~~~~~~~~~~~~~~~~~
INFO: From Compiling run_search_experiment.cc:
In file included from task_util.h:26:0,
                 from run_search_experiment.cc:25:
executor.h:803:10: warning: variable templates only available with -std=c++14 or -std=gnu++14
     128> kOpIndexToExecuteFunction = {
          ^~~~~~~~~~~~~~~~~~~~~~~~~
INFO: From Compiling fec_hashing.cc:
In file included from fec_hashing.h:21:0,
                 from fec_hashing.cc:15:
executor.h:803:10: warning: variable templates only available with -std=c++14 or -std=gnu++14
     128> kOpIndexToExecuteFunction = {
          ^~~~~~~~~~~~~~~~~~~~~~~~~
INFO: From Compiling task_util.cc:
In file included from task_util.h:26:0,
                 from task_util.cc:15:
executor.h:803:10: warning: variable templates only available with -std=c++14 or -std=gnu++14
     128> kOpIndexToExecuteFunction = {
          ^~~~~~~~~~~~~~~~~~~~~~~~~
task_util.cc: In function 'void automl_zero::FillTasksFromTaskSpec(const automl_zero::TaskSpec&, std::vector<std::unique_ptr<automl_zero::TaskInterface> >*)':
task_util.cc:92:11: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
         i < first_param_seeds.size() ? first_param_seeds[i] : param_seed + 1;
         ~~^~~~~~~~~~~~~~~~~~~~~~~~~~
task_util.cc:94:11: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
         i < first_data_seeds.size() ? first_data_seeds[i] : data_seed + 1;
         ~~^~~~~~~~~~~~~~~~~~~~~~~~~
In file included from task_util.cc:15:0:
task_util.h: In instantiation of 'static void automl_zero::ProjectedBinaryClassificationTaskCreator<F>::Create(automl_zero::EvalType, const automl_zero::ProjectedBinaryClassificationTask&, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::TaskBuffer<F>*) [with int F = 2; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]':
task_util.h:484:58:   required from 'std::unique_ptr<automl_zero::Task<F> > automl_zero::CreateTask(automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::RandomSeedT, const automl_zero::TaskSpec&) [with int F = 2; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]'
task_util.cc:100:73:   required from here
task_util.h:228:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     for (IntegerT k = 0; k < buffer->train_features_.size(); ++k)  {
task_util.h:241:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     for (IntegerT k = 0; k < buffer->valid_features_.size(); ++k)  {
In file included from definitions.h:34:0,
                 from task.h:27,
                 from task_util.h:23,
                 from task_util.cc:15:
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h: In instantiation of 'std::__cxx11::string* google::Check_EQImpl(const T1&, const T2&, const char*) [with T1 = long unsigned int; T2 = int; std::__cxx11::string = std::__cxx11::basic_string<char>]':
task_util.h:529:3:   required from 'std::unique_ptr<automl_zero::Task<F> > automl_zero::CreateTask(automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::RandomSeedT, const automl_zero::TaskSpec&) [with int F = 2; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]'
task_util.cc:100:73:   required from here
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:728:32: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
 DEFINE_CHECK_OP_IMPL(Check_EQ, ==)  // Compilation error with CHECK_EQ(NULL, x)?
                                ^
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:148:53: note: in definition of macro 'GOOGLE_PREDICT_TRUE'
 #define GOOGLE_PREDICT_TRUE(x) (__builtin_expect(!!(x), 1))
                                                     ^
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:728:1: note: in expansion of macro 'DEFINE_CHECK_OP_IMPL'
 DEFINE_CHECK_OP_IMPL(Check_EQ, ==)  // Compilation error with CHECK_EQ(NULL, x)?
 ^~~~~~~~~~~~~~~~~~~~
In file included from task_util.cc:15:0:
task_util.h: In instantiation of 'static void automl_zero::ProjectedBinaryClassificationTaskCreator<F>::Create(automl_zero::EvalType, const automl_zero::ProjectedBinaryClassificationTask&, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::TaskBuffer<F>*) [with int F = 4; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]':
task_util.h:484:58:   required from 'std::unique_ptr<automl_zero::Task<F> > automl_zero::CreateTask(automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::RandomSeedT, const automl_zero::TaskSpec&) [with int F = 4; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]'
task_util.cc:104:73:   required from here
task_util.h:228:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     for (IntegerT k = 0; k < buffer->train_features_.size(); ++k)  {
task_util.h:241:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     for (IntegerT k = 0; k < buffer->valid_features_.size(); ++k)  {
task_util.h: In instantiation of 'static void automl_zero::ProjectedBinaryClassificationTaskCreator<F>::Create(automl_zero::EvalType, const automl_zero::ProjectedBinaryClassificationTask&, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::TaskBuffer<F>*) [with int F = 8; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]':
task_util.h:484:58:   required from 'std::unique_ptr<automl_zero::Task<F> > automl_zero::CreateTask(automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::RandomSeedT, const automl_zero::TaskSpec&) [with int F = 8; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]'
task_util.cc:108:73:   required from here
task_util.h:228:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     for (IntegerT k = 0; k < buffer->train_features_.size(); ++k)  {
task_util.h:241:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     for (IntegerT k = 0; k < buffer->valid_features_.size(); ++k)  {
task_util.h: In instantiation of 'static void automl_zero::ProjectedBinaryClassificationTaskCreator<F>::Create(automl_zero::EvalType, const automl_zero::ProjectedBinaryClassificationTask&, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::TaskBuffer<F>*) [with int F = 16; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]':
task_util.h:484:58:   required from 'std::unique_ptr<automl_zero::Task<F> > automl_zero::CreateTask(automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::RandomSeedT, const automl_zero::TaskSpec&) [with int F = 16; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]'
task_util.cc:112:74:   required from here
task_util.h:228:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     for (IntegerT k = 0; k < buffer->train_features_.size(); ++k)  {
task_util.h:241:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     for (IntegerT k = 0; k < buffer->valid_features_.size(); ++k)  {
task_util.h: In instantiation of 'static void automl_zero::ProjectedBinaryClassificationTaskCreator<F>::Create(automl_zero::EvalType, const automl_zero::ProjectedBinaryClassificationTask&, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::TaskBuffer<F>*) [with int F = 32; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]':
task_util.h:484:58:   required from 'std::unique_ptr<automl_zero::Task<F> > automl_zero::CreateTask(automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::RandomSeedT, const automl_zero::TaskSpec&) [with int F = 32; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]'
task_util.cc:116:74:   required from here
task_util.h:228:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     for (IntegerT k = 0; k < buffer->train_features_.size(); ++k)  {
task_util.h:241:28: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     for (IntegerT k = 0; k < buffer->valid_features_.size(); ++k)  {
In file included from definitions.h:34:0,
                 from task.h:27,
                 from task_util.h:23,
                 from task_util.cc:15:
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h: In instantiation of 'std::__cxx11::string* google::Check_GEImpl(const T1&, const T2&, const char*) [with T1 = int; T2 = long unsigned int; std::__cxx11::string = std::__cxx11::basic_string<char>]':
task_util.h:218:5:   required from 'static void automl_zero::ProjectedBinaryClassificationTaskCreator<F>::Create(automl_zero::EvalType, const automl_zero::ProjectedBinaryClassificationTask&, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::TaskBuffer<F>*) [with int F = 2; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]'
task_util.h:484:58:   required from 'std::unique_ptr<automl_zero::Task<F> > automl_zero::CreateTask(automl_zero::IntegerT, automl_zero::RandomSeedT, automl_zero::RandomSeedT, const automl_zero::TaskSpec&) [with int F = 2; automl_zero::IntegerT = long int; automl_zero::RandomSeedT = unsigned int]'
task_util.cc:100:73:   required from here
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:732:32: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
 DEFINE_CHECK_OP_IMPL(Check_GE, >=)
                                ^
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:148:53: note: in definition of macro 'GOOGLE_PREDICT_TRUE'
 #define GOOGLE_PREDICT_TRUE(x) (__builtin_expect(!!(x), 1))
                                                     ^
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:732:1: note: in expansion of macro 'DEFINE_CHECK_OP_IMPL'
 DEFINE_CHECK_OP_IMPL(Check_GE, >=)
 ^~~~~~~~~~~~~~~~~~~~
task_util.cc:94:37: warning: 'data_seed' may be used uninitialized in this function [-Wmaybe-uninitialized]
         i < first_data_seeds.size() ? first_data_seeds[i] : data_seed + 1;
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
task_util.cc:92:38: warning: 'param_seed' may be used uninitialized in this function [-Wmaybe-uninitialized]
         i < first_param_seeds.size() ? first_param_seeds[i] : param_seed + 1;
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INFO: From Compiling evaluator.cc:
In file included from fec_cache.h:24:0,
                 from evaluator.h:28,
                 from evaluator.cc:15:
executor.h:803:10: warning: variable templates only available with -std=c++14 or -std=gnu++14
     128> kOpIndexToExecuteFunction = {
          ^~~~~~~~~~~~~~~~~~~~~~~~~
evaluator.cc: In member function 'double automl_zero::Evaluator::Evaluate(const automl_zero::Algorithm&)':
evaluator.cc:89:26: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
   for (IntegerT i = 0; i < tasks_.size(); ++i) {
                        ~~^~~~~~~~~~~~~~~
In file included from definitions.h:34:0,
                 from instruction.h:24,
                 from algorithm.h:24,
                 from evaluator.h:23,
                 from evaluator.cc:15:
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h: In instantiation of 'std::__cxx11::string* google::Check_GTImpl(const T1&, const T2&, const char*) [with T1 = long unsigned int; T2 = int; std::__cxx11::string = std::__cxx11::basic_string<char>]':
evaluator.cc:78:3:   required from here
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:733:32: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
 DEFINE_CHECK_OP_IMPL(Check_GT, > )
                                ^
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:148:53: note: in definition of macro 'GOOGLE_PREDICT_TRUE'
 #define GOOGLE_PREDICT_TRUE(x) (__builtin_expect(!!(x), 1))
                                                     ^
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:733:1: note: in expansion of macro 'DEFINE_CHECK_OP_IMPL'
 DEFINE_CHECK_OP_IMPL(Check_GT, > )
 ^~~~~~~~~~~~~~~~~~~~
In file included from evaluator.h:24:0,
                 from evaluator.cc:15:
task.h: In instantiation of 'void automl_zero::TaskIterator<F>::Next() [with int F = 2]':
executor.h:1300:5:   required from 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 2]'
executor.h:1027:44:   required from 'double automl_zero::Executor<F>::Execute(std::vector<double>*, std::vector<double>*) [with int F = 2]'
evaluator.cc:159:5:   required from 'double automl_zero::Evaluator::ExecuteImpl(const automl_zero::Task<F>&, automl_zero::IntegerT, const automl_zero::Algorithm&) [with int F = 2; automl_zero::IntegerT = long int]'
evaluator.cc:118:75:   required from here
task.h:317:26: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     if (current_example_ >= features_->size()) {
task.h: In instantiation of 'bool automl_zero::TaskIterator<F>::Done() const [with int F = 2]':
executor.h:1301:5:   required from 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 2]'
executor.h:1027:44:   required from 'double automl_zero::Executor<F>::Execute(std::vector<double>*, std::vector<double>*) [with int F = 2]'
evaluator.cc:159:5:   required from 'double automl_zero::Evaluator::ExecuteImpl(const automl_zero::Task<F>&, automl_zero::IntegerT, const automl_zero::Algorithm&) [with int F = 2; automl_zero::IntegerT = long int]'
evaluator.cc:118:75:   required from here
task.h:311:27: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     return current_epoch_ >= epochs_->size();
            ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~
task.h: In instantiation of 'void automl_zero::TaskIterator<F>::Next() [with int F = 4]':
executor.h:1300:5:   required from 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 4]'
executor.h:1027:44:   required from 'double automl_zero::Executor<F>::Execute(std::vector<double>*, std::vector<double>*) [with int F = 4]'
evaluator.cc:159:5:   required from 'double automl_zero::Evaluator::ExecuteImpl(const automl_zero::Task<F>&, automl_zero::IntegerT, const automl_zero::Algorithm&) [with int F = 4; automl_zero::IntegerT = long int]'
evaluator.cc:122:75:   required from here
task.h:317:26: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     if (current_example_ >= features_->size()) {
task.h: In instantiation of 'bool automl_zero::TaskIterator<F>::Done() const [with int F = 4]':
executor.h:1301:5:   required from 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 4]'
executor.h:1027:44:   required from 'double automl_zero::Executor<F>::Execute(std::vector<double>*, std::vector<double>*) [with int F = 4]'
evaluator.cc:159:5:   required from 'double automl_zero::Evaluator::ExecuteImpl(const automl_zero::Task<F>&, automl_zero::IntegerT, const automl_zero::Algorithm&) [with int F = 4; automl_zero::IntegerT = long int]'
evaluator.cc:122:75:   required from here
task.h:311:27: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     return current_epoch_ >= epochs_->size();
            ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~
task.h: In instantiation of 'void automl_zero::TaskIterator<F>::Next() [with int F = 8]':
executor.h:1300:5:   required from 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 8]'
executor.h:1027:44:   required from 'double automl_zero::Executor<F>::Execute(std::vector<double>*, std::vector<double>*) [with int F = 8]'
evaluator.cc:159:5:   required from 'double automl_zero::Evaluator::ExecuteImpl(const automl_zero::Task<F>&, automl_zero::IntegerT, const automl_zero::Algorithm&) [with int F = 8; automl_zero::IntegerT = long int]'
evaluator.cc:126:75:   required from here
task.h:317:26: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     if (current_example_ >= features_->size()) {
task.h: In instantiation of 'bool automl_zero::TaskIterator<F>::Done() const [with int F = 8]':
executor.h:1301:5:   required from 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 8]'
executor.h:1027:44:   required from 'double automl_zero::Executor<F>::Execute(std::vector<double>*, std::vector<double>*) [with int F = 8]'
evaluator.cc:159:5:   required from 'double automl_zero::Evaluator::ExecuteImpl(const automl_zero::Task<F>&, automl_zero::IntegerT, const automl_zero::Algorithm&) [with int F = 8; automl_zero::IntegerT = long int]'
evaluator.cc:126:75:   required from here
task.h:311:27: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     return current_epoch_ >= epochs_->size();
            ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~
task.h: In instantiation of 'void automl_zero::TaskIterator<F>::Next() [with int F = 16]':
executor.h:1300:5:   required from 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 16]'
executor.h:1027:44:   required from 'double automl_zero::Executor<F>::Execute(std::vector<double>*, std::vector<double>*) [with int F = 16]'
evaluator.cc:159:5:   required from 'double automl_zero::Evaluator::ExecuteImpl(const automl_zero::Task<F>&, automl_zero::IntegerT, const automl_zero::Algorithm&) [with int F = 16; automl_zero::IntegerT = long int]'
evaluator.cc:130:76:   required from here
task.h:317:26: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     if (current_example_ >= features_->size()) {
task.h: In instantiation of 'bool automl_zero::TaskIterator<F>::Done() const [with int F = 16]':
executor.h:1301:5:   required from 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 16]'
executor.h:1027:44:   required from 'double automl_zero::Executor<F>::Execute(std::vector<double>*, std::vector<double>*) [with int F = 16]'
evaluator.cc:159:5:   required from 'double automl_zero::Evaluator::ExecuteImpl(const automl_zero::Task<F>&, automl_zero::IntegerT, const automl_zero::Algorithm&) [with int F = 16; automl_zero::IntegerT = long int]'
evaluator.cc:130:76:   required from here
task.h:311:27: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     return current_epoch_ >= epochs_->size();
            ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~
task.h: In instantiation of 'void automl_zero::TaskIterator<F>::Next() [with int F = 32]':
executor.h:1300:5:   required from 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 32]'
executor.h:1027:44:   required from 'double automl_zero::Executor<F>::Execute(std::vector<double>*, std::vector<double>*) [with int F = 32]'
evaluator.cc:159:5:   required from 'double automl_zero::Evaluator::ExecuteImpl(const automl_zero::Task<F>&, automl_zero::IntegerT, const automl_zero::Algorithm&) [with int F = 32; automl_zero::IntegerT = long int]'
evaluator.cc:134:76:   required from here
task.h:317:26: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     if (current_example_ >= features_->size()) {
task.h: In instantiation of 'bool automl_zero::TaskIterator<F>::Done() const [with int F = 32]':
executor.h:1301:5:   required from 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 32]'
executor.h:1027:44:   required from 'double automl_zero::Executor<F>::Execute(std::vector<double>*, std::vector<double>*) [with int F = 32]'
evaluator.cc:159:5:   required from 'double automl_zero::Evaluator::ExecuteImpl(const automl_zero::Task<F>&, automl_zero::IntegerT, const automl_zero::Algorithm&) [with int F = 32; automl_zero::IntegerT = long int]'
evaluator.cc:134:76:   required from here
task.h:311:27: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     return current_epoch_ >= epochs_->size();
            ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~
In file included from definitions.h:34:0,
                 from instruction.h:24,
                 from algorithm.h:24,
                 from evaluator.h:23,
                 from evaluator.cc:15:
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h: In instantiation of 'std::__cxx11::string* google::Check_LEImpl(const T1&, const T2&, const char*) [with T1 = long int; T2 = long unsigned int; std::__cxx11::string = std::__cxx11::basic_string<char>]':
task.h:315:5:   required from 'void automl_zero::TaskIterator<F>::Next() [with int F = 2]'
executor.h:1300:5:   required from 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 2]'
executor.h:1027:44:   required from 'double automl_zero::Executor<F>::Execute(std::vector<double>*, std::vector<double>*) [with int F = 2]'
evaluator.cc:159:5:   required from 'double automl_zero::Evaluator::ExecuteImpl(const automl_zero::Task<F>&, automl_zero::IntegerT, const automl_zero::Algorithm&) [with int F = 2; automl_zero::IntegerT = long int]'
evaluator.cc:118:75:   required from here
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:730:32: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
 DEFINE_CHECK_OP_IMPL(Check_LE, <=)
                                ^
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:148:53: note: in definition of macro 'GOOGLE_PREDICT_TRUE'
 #define GOOGLE_PREDICT_TRUE(x) (__builtin_expect(!!(x), 1))
                                                     ^
bazel-out/k8-opt/bin/external/com_google_glog/_virtual_includes/default_glog_headers/glog/logging.h:730:1: note: in expansion of macro 'DEFINE_CHECK_OP_IMPL'
 DEFINE_CHECK_OP_IMPL(Check_LE, <=)
 ^~~~~~~~~~~~~~~~~~~~
In file included from fec_cache.h:24:0,
                 from evaluator.h:28,
                 from evaluator.cc:15:
executor.h: In member function 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 2]':
executor.h:1307:10: warning: 'fitness' may be used uninitialized in this function [-Wmaybe-uninitialized]
   double fitness;
          ^~~~~~~
executor.h: In member function 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 4]':
executor.h:1307:10: warning: 'fitness' may be used uninitialized in this function [-Wmaybe-uninitialized]
executor.h: In member function 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 32]':
executor.h:1307:10: warning: 'fitness' may be used uninitialized in this function [-Wmaybe-uninitialized]
executor.h: In member function 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 8]':
executor.h:1307:10: warning: 'fitness' may be used uninitialized in this function [-Wmaybe-uninitialized]
executor.h: In member function 'double automl_zero::Executor<F>::Validate(std::vector<double>*) [with int F = 16]':
executor.h:1307:10: warning: 'fitness' may be used uninitialized in this function [-Wmaybe-uninitialized]
Target //:run_search_experiment up-to-date:
  bazel-bin/run_search_experiment
INFO: Elapsed time: 214.700s, Critical Path: 40.38s
INFO: 421 processes: 421 linux-sandbox.
INFO: Build completed successfully, 440 total actions
INFO: Running command line: bazel-bin/run_search_experiment '--search_experiment_spec=     search_tasks {       tasks {         scalar_linear_regression_task {}         features_size: 4         num_train_examples: 100         num_valid_examples: 100         num_tasks: 10         eval_type: RMS_ERROR       }     }     setup_ops: [SCALAR_CONST_SET_OP, VECTOR_INNER_PRODUCT_OP, SCALAR_DIFF_OP, SCALAR_PRODUCT_OP, SCALAR_VECTOR_PRODUCT_OP, VECTOR_SUM_OP]     predict_ops: [SCALAR_CONST_SET_OP, VECTOR_INNER_PRODUCT_OP, SCALAR_DIFF_OP, SCALAR_PRODUCT_OP, SCALAR_VECTOR_PRODUCT_OP, VECTOR_SUM_OP]     learn_ops: [SCALAR_CONST_SET_OP, VECTOR_INNER_PRODUCT_OP, SCALAR_DIFF_OP, SCALAR_PRODUCT_OP, SCALAR_VECTOR_PRODUCT_OP, VECTOR_SUM_OP]     learn_size_init: 8     setup_size_init: 10     predict_size_init: 2     fec {num_train_examples: 10 num_valid_examples: 10}     fitness_combination_mode: MEAN_FITNESS_COMBINATION     population_size: 1000     tournament_size: 10     initial_population: RANDOM_ALGORITHM     max_train_steps: 200000000     allowed_mutation_types {
      mutation_types: [ALTER_PARAM_MUTATION_TYPE, RANDOMIZE_INSTRUCTION_MUTATION_TYPE, RANDOMIZE_COMPONENT_FUNCTION_MUTATION_TYPE]     }     mutate_prob: 0.9     progress_every: 10000     ' '--final_tasks=     tasks {       scalar_linear_regression_task {}       features_size: 4       num_train_examples: 1000       num_valid_examples: 100       num_tasks: 100       eval_type: RMS_ERROR       data_seeds: [1000000]       param_seeds: [2000000]     }     ' '--max_experiments=0' --randomize_task_seeds '--select_tasks=     tasks {       scalar_linear_regression_task {}       features_size: 4       num_train_examples: 1000       num_valid_examples: 100       num_tasks: 100       eval_type: RMS_ERROR     }     ' '--sufficient_fitness=0.9INFO: Build completed successfully, 440 total actions
Random seed = 3912513528
Running evolution experiment (on the T_search tasks)...
indivs=1000, elapsed_secs=0, mean=0.253500, stdev=0.093856, best fit=0.307071,
indivs=11000, elapsed_secs=0, mean=0.293926, stdev=0.070764, best fit=0.328042,
indivs=21000, elapsed_secs=1, mean=0.312743, stdev=0.124780, best fit=0.461296,
indivs=31000, elapsed_secs=1, mean=0.421586, stdev=0.229371, best fit=0.637646,
indivs=41000, elapsed_secs=1, mean=0.423225, stdev=0.229585, best fit=0.663748,
indivs=51000, elapsed_secs=2, mean=0.444942, stdev=0.229910, best fit=0.663930,
indivs=61000, elapsed_secs=2, mean=0.437564, stdev=0.234877, best fit=0.663930,
indivs=71000, elapsed_secs=2, mean=0.438180, stdev=0.234864, best fit=0.663930,
indivs=81000, elapsed_secs=3, mean=0.439715, stdev=0.231616, best fit=0.663930,
indivs=91000, elapsed_secs=3, mean=0.441246, stdev=0.236480, best fit=0.663930,
indivs=101000, elapsed_secs=4, mean=0.428594, stdev=0.240837, best fit=0.676886,
indivs=111000, elapsed_secs=4, mean=0.422798, stdev=0.258081, best fit=0.679160,
indivs=121000, elapsed_secs=4, mean=0.424811, stdev=0.253641, best fit=0.679161,
indivs=131000, elapsed_secs=5, mean=0.415612, stdev=0.250985, best fit=0.683319,
indivs=141000, elapsed_secs=5, mean=0.411837, stdev=0.243969, best fit=0.683332,
indivs=151000, elapsed_secs=6, mean=0.417271, stdev=0.242535, best fit=0.683332,
indivs=161000, elapsed_secs=6, mean=0.422083, stdev=0.253617, best fit=0.683332,
indivs=171000, elapsed_secs=6, mean=0.434448, stdev=0.245975, best fit=0.683332,
indivs=181000, elapsed_secs=7, mean=0.426648, stdev=0.250516, best fit=0.683332,
indivs=191000, elapsed_secs=7, mean=0.431460, stdev=0.250547, best fit=0.683332,
indivs=201000, elapsed_secs=7, mean=0.425624, stdev=0.247771, best fit=0.683332,
indivs=211000, elapsed_secs=8, mean=0.434085, stdev=0.247494, best fit=0.683332,
indivs=221000, elapsed_secs=8, mean=0.426943, stdev=0.250001, best fit=0.683332,
indivs=231000, elapsed_secs=8, mean=0.414979, stdev=0.254752, best fit=0.683332,
indivs=241000, elapsed_secs=9, mean=0.432920, stdev=0.245772, best fit=0.683332,
indivs=251000, elapsed_secs=9, mean=0.429932, stdev=0.247263, best fit=0.683332,
indivs=261000, elapsed_secs=10, mean=0.433125, stdev=0.241555, best fit=0.683332,
indivs=271000, elapsed_secs=10, mean=0.432156, stdev=0.247396, best fit=0.697125,
indivs=281000, elapsed_secs=10, mean=0.429567, stdev=0.252230, best fit=0.697814,
indivs=291000, elapsed_secs=11, mean=0.423938, stdev=0.253529, best fit=0.697988,
indivs=301000, elapsed_secs=11, mean=0.433630, stdev=0.248117, best fit=0.697988,
indivs=311000, elapsed_secs=11, mean=0.428271, stdev=0.248011, best fit=0.697988,
indivs=321000, elapsed_secs=12, mean=0.442167, stdev=0.250122, best fit=0.697989,
indivs=331000, elapsed_secs=12, mean=0.430533, stdev=0.256002, best fit=0.697989,
indivs=341000, elapsed_secs=13, mean=0.434074, stdev=0.248665, best fit=0.697989,
indivs=351000, elapsed_secs=13, mean=0.427247, stdev=0.248637, best fit=0.697989,
indivs=361000, elapsed_secs=13, mean=0.425690, stdev=0.244972, best fit=0.697990,
indivs=371000, elapsed_secs=14, mean=0.422004, stdev=0.254019, best fit=0.697990,
indivs=381000, elapsed_secs=14, mean=0.419987, stdev=0.241141, best fit=0.697990,
indivs=391000, elapsed_secs=14, mean=0.431110, stdev=0.244636, best fit=0.697990,
indivs=401000, elapsed_secs=15, mean=0.440440, stdev=0.248025, best fit=0.697990,
indivs=411000, elapsed_secs=15, mean=0.430473, stdev=0.239745, best fit=0.697990,
indivs=421000, elapsed_secs=15, mean=0.426519, stdev=0.250610, best fit=0.697990,
indivs=431000, elapsed_secs=16, mean=0.433115, stdev=0.253164, best fit=0.697990,
indivs=441000, elapsed_secs=16, mean=0.438556, stdev=0.245539, best fit=0.697990,
indivs=451000, elapsed_secs=16, mean=0.445789, stdev=0.249472, best fit=0.697990,
indivs=461000, elapsed_secs=17, mean=0.433184, stdev=0.248464, best fit=0.697990,
indivs=471000, elapsed_secs=17, mean=0.433951, stdev=0.247937, best fit=0.697990,
indivs=481000, elapsed_secs=18, mean=0.428769, stdev=0.250987, best fit=0.697990,
indivs=491000, elapsed_secs=18, mean=0.424236, stdev=0.247085, best fit=0.697990,
indivs=501000, elapsed_secs=18, mean=0.437875, stdev=0.249816, best fit=0.697990,
indivs=511000, elapsed_secs=19, mean=0.429439, stdev=0.246840, best fit=0.697990,
indivs=521000, elapsed_secs=19, mean=0.435046, stdev=0.246285, best fit=0.697990,
indivs=531000, elapsed_secs=19, mean=0.437056, stdev=0.247616, best fit=0.697990,
indivs=541000, elapsed_secs=20, mean=0.430361, stdev=0.247535, best fit=0.697990,
indivs=551000, elapsed_secs=20, mean=0.413965, stdev=0.248032, best fit=0.697990,
indivs=561000, elapsed_secs=20, mean=0.431665, stdev=0.248043, best fit=0.697990,
indivs=571000, elapsed_secs=21, mean=0.429747, stdev=0.248837, best fit=0.697990,
indivs=581000, elapsed_secs=21, mean=0.428235, stdev=0.251678, best fit=0.697990,
indivs=591000, elapsed_secs=21, mean=0.435072, stdev=0.243084, best fit=0.697990,
indivs=601000, elapsed_secs=22, mean=0.434695, stdev=0.242854, best fit=0.697990,
indivs=611000, elapsed_secs=22, mean=0.418784, stdev=0.249084, best fit=0.697990,
indivs=621000, elapsed_secs=23, mean=0.426587, stdev=0.242467, best fit=0.697990,
indivs=631000, elapsed_secs=23, mean=0.437114, stdev=0.247143, best fit=0.697990,
indivs=641000, elapsed_secs=23, mean=0.419897, stdev=0.246285, best fit=0.697990,
indivs=651000, elapsed_secs=24, mean=0.416014, stdev=0.246650, best fit=0.697990,
indivs=661000, elapsed_secs=24, mean=0.436094, stdev=0.250597, best fit=0.697990,
indivs=671000, elapsed_secs=24, mean=0.431421, stdev=0.245642, best fit=0.697990,
indivs=681000, elapsed_secs=25, mean=0.437087, stdev=0.248116, best fit=0.697990,
indivs=691000, elapsed_secs=25, mean=0.432236, stdev=0.250286, best fit=0.697990,
indivs=701000, elapsed_secs=25, mean=0.425789, stdev=0.248945, best fit=0.697990,
indivs=711000, elapsed_secs=26, mean=0.416446, stdev=0.250869, best fit=0.697990,
indivs=721000, elapsed_secs=26, mean=0.442066, stdev=0.246922, best fit=0.697990,
indivs=731000, elapsed_secs=26, mean=0.441123, stdev=0.245489, best fit=0.697990,
indivs=741000, elapsed_secs=27, mean=0.438011, stdev=0.252467, best fit=0.697990,
indivs=751000, elapsed_secs=27, mean=0.414915, stdev=0.252197, best fit=0.697990,
indivs=761000, elapsed_secs=28, mean=0.435332, stdev=0.247455, best fit=0.697990,
indivs=771000, elapsed_secs=28, mean=0.437713, stdev=0.247692, best fit=0.697990,
indivs=781000, elapsed_secs=28, mean=0.426048, stdev=0.250686, best fit=0.697990,
indivs=791000, elapsed_secs=29, mean=0.410665, stdev=0.255198, best fit=0.697990,
indivs=801000, elapsed_secs=29, mean=0.428639, stdev=0.247447, best fit=0.697990,
indivs=811000, elapsed_secs=29, mean=0.428810, stdev=0.247383, best fit=0.697990,
indivs=821000, elapsed_secs=30, mean=0.429469, stdev=0.245769, best fit=0.697990,
indivs=831000, elapsed_secs=30, mean=0.434143, stdev=0.248265, best fit=0.697990,
indivs=841000, elapsed_secs=30, mean=0.443190, stdev=0.245729, best fit=0.697990,
indivs=851000, elapsed_secs=31, mean=0.446337, stdev=0.244944, best fit=0.697990,
indivs=861000, elapsed_secs=31, mean=0.425893, stdev=0.255638, best fit=0.697990,
indivs=871000, elapsed_secs=32, mean=0.450698, stdev=0.240530, best fit=0.697990,
indivs=881000, elapsed_secs=32, mean=0.422116, stdev=0.248147, best fit=0.697990,
indivs=891000, elapsed_secs=32, mean=0.430879, stdev=0.250518, best fit=0.697990,
indivs=901000, elapsed_secs=33, mean=0.421632, stdev=0.248938, best fit=0.697990,
indivs=911000, elapsed_secs=33, mean=0.421452, stdev=0.245654, best fit=0.697990,
indivs=921000, elapsed_secs=33, mean=0.436302, stdev=0.245892, best fit=0.697990,
indivs=931000, elapsed_secs=34, mean=0.416161, stdev=0.249274, best fit=0.697990,
indivs=941000, elapsed_secs=34, mean=0.429618, stdev=0.248300, best fit=0.697990,
indivs=951000, elapsed_secs=34, mean=0.430299, stdev=0.249529, best fit=0.697990,
indivs=961000, elapsed_secs=35, mean=0.426844, stdev=0.245078, best fit=0.697990,
indivs=971000, elapsed_secs=35, mean=0.434567, stdev=0.243715, best fit=0.697990,
indivs=981000, elapsed_secs=35, mean=0.418741, stdev=0.246898, best fit=0.697990,
indivs=991000, elapsed_secs=36, mean=0.420944, stdev=0.253214, best fit=0.697990,
indivs=1001000, elapsed_secs=36, mean=0.433014, stdev=0.248065, best fit=0.697990,
indivs=1011000, elapsed_secs=36, mean=0.432430, stdev=0.248214, best fit=0.697990,
Experiment done. Retrieving candidate algorithm.
Search fitness for candidate algorithm = 0.697990
Evaluating candidate algorithm from experiment (on T_select tasks)... 
Select fitness for candidate algorithm = 0.682651
Select fitness is the best so far. 
Running evolution experiment (on the T_search tasks)...
indivs=1000, elapsed_secs=0, mean=0.273501, stdev=0.102520, best fit=0.329653,
indivs=11000, elapsed_secs=0, mean=0.293758, stdev=0.083697, best fit=0.329871,
indivs=21000, elapsed_secs=0, mean=0.302863, stdev=0.068086, best fit=0.329922,
indivs=31000, elapsed_secs=1, mean=0.303633, stdev=0.066756, best fit=0.330232,
indivs=41000, elapsed_secs=1, mean=0.278158, stdev=0.085858, best fit=0.330249,
indivs=51000, elapsed_secs=2, mean=0.283012, stdev=0.089434, best fit=0.330256,
indivs=61000, elapsed_secs=2, mean=0.289249, stdev=0.081268, best fit=0.330257,
indivs=71000, elapsed_secs=2, mean=0.284562, stdev=0.087508, best fit=0.330257,
indivs=81000, elapsed_secs=3, mean=0.285494, stdev=0.086026, best fit=0.330257,
indivs=91000, elapsed_secs=3, mean=0.282499, stdev=0.089352, best fit=0.330257,
indivs=101000, elapsed_secs=4, mean=0.280445, stdev=0.090416, best fit=0.330257,
indivs=111000, elapsed_secs=4, mean=0.281236, stdev=0.092451, best fit=0.330257,
indivs=121000, elapsed_secs=4, mean=0.280004, stdev=0.090474, best fit=0.330257,
indivs=131000, elapsed_secs=5, mean=0.285378, stdev=0.088466, best fit=0.330257,
indivs=141000, elapsed_secs=5, mean=0.279464, stdev=0.091593, best fit=0.330257,
indivs=151000, elapsed_secs=6, mean=0.286861, stdev=0.091078, best fit=0.330338,
indivs=161000, elapsed_secs=6, mean=0.287600, stdev=0.090699, best fit=0.330339,
indivs=171000, elapsed_secs=6, mean=0.289373, stdev=0.091222, best fit=0.330339,
indivs=181000, elapsed_secs=7, mean=0.289371, stdev=0.092227, best fit=0.330339,
indivs=191000, elapsed_secs=7, mean=0.285893, stdev=0.093169, best fit=0.330339,
indivs=201000, elapsed_secs=8, mean=0.289457, stdev=0.091414, best fit=0.330339,
indivs=211000, elapsed_secs=8, mean=0.286394, stdev=0.092041, best fit=0.330339,
indivs=221000, elapsed_secs=8, mean=0.313088, stdev=0.091760, best fit=0.367801,
indivs=231000, elapsed_secs=9, mean=0.328450, stdev=0.069642, best fit=0.367896,
indivs=241000, elapsed_secs=9, mean=0.335750, stdev=0.071052, best fit=0.379372,
indivs=251000, elapsed_secs=9, mean=0.342536, stdev=0.076012, best fit=0.381086,
indivs=261000, elapsed_secs=10, mean=0.345572, stdev=0.070348, best fit=0.381142,
indivs=271000, elapsed_secs=10, mean=0.345008, stdev=0.076506, best fit=0.381154,
indivs=281000, elapsed_secs=10, mean=0.342362, stdev=0.076303, best fit=0.381154,
indivs=291000, elapsed_secs=11, mean=0.338636, stdev=0.084004, best fit=0.381154,
indivs=301000, elapsed_secs=11, mean=0.346650, stdev=0.068148, best fit=0.384047,
indivs=311000, elapsed_secs=12, mean=0.340841, stdev=0.079965, best fit=0.384256,
indivs=321000, elapsed_secs=12, mean=0.338757, stdev=0.081897, best fit=0.384318,
indivs=331000, elapsed_secs=12, mean=0.339039, stdev=0.078218, best fit=0.384318,
indivs=341000, elapsed_secs=13, mean=0.346024, stdev=0.066867, best fit=0.384422,
indivs=351000, elapsed_secs=13, mean=0.341995, stdev=0.074072, best fit=0.384455,
indivs=361000, elapsed_secs=13, mean=0.324488, stdev=0.112796, best fit=0.384506,
indivs=371000, elapsed_secs=14, mean=0.346743, stdev=0.066131, best fit=0.384522,
indivs=381000, elapsed_secs=14, mean=0.338459, stdev=0.090191, best fit=0.384522,
indivs=391000, elapsed_secs=14, mean=0.325522, stdev=0.107809, best fit=0.384522,
indivs=401000, elapsed_secs=15, mean=0.328984, stdev=0.099473, best fit=0.384546,
indivs=411000, elapsed_secs=15, mean=0.327062, stdev=0.099031, best fit=0.384546,
indivs=421000, elapsed_secs=16, mean=0.331641, stdev=0.094305, best fit=0.384546,
indivs=431000, elapsed_secs=16, mean=0.337441, stdev=0.084802, best fit=0.384546,
indivs=441000, elapsed_secs=16, mean=0.327686, stdev=0.085832, best fit=0.386239,
indivs=451000, elapsed_secs=17, mean=0.326919, stdev=0.082766, best fit=0.386247,
indivs=461000, elapsed_secs=17, mean=0.327363, stdev=0.083632, best fit=0.386247,
indivs=471000, elapsed_secs=17, mean=0.331667, stdev=0.077647, best fit=0.386247,
indivs=481000, elapsed_secs=18, mean=0.344326, stdev=0.081488, best fit=0.396796,
indivs=491000, elapsed_secs=18, mean=0.375019, stdev=0.113473, best fit=0.464209,
indivs=501000, elapsed_secs=19, mean=0.377210, stdev=0.120660, best fit=0.473238,
indivs=511000, elapsed_secs=19, mean=0.382143, stdev=0.113369, best fit=0.475072,
indivs=521000, elapsed_secs=19, mean=0.374074, stdev=0.127072, best fit=0.475072,
indivs=531000, elapsed_secs=20, mean=0.364777, stdev=0.132749, best fit=0.475072,
indivs=541000, elapsed_secs=20, mean=0.359069, stdev=0.138801, best fit=0.475072,
indivs=551000, elapsed_secs=20, mean=0.376870, stdev=0.122059, best fit=0.475263,
indivs=561000, elapsed_secs=21, mean=0.377673, stdev=0.123387, best fit=0.475282,
indivs=571000, elapsed_secs=21, mean=0.376200, stdev=0.122936, best fit=0.475305,
indivs=581000, elapsed_secs=22, mean=0.373584, stdev=0.129529, best fit=0.485775,
indivs=591000, elapsed_secs=22, mean=0.381262, stdev=0.129691, best fit=0.487174,
indivs=601000, elapsed_secs=22, mean=0.388374, stdev=0.124707, best fit=0.487201,
indivs=611000, elapsed_secs=23, mean=0.391087, stdev=0.136438, best fit=0.499088,
indivs=621000, elapsed_secs=23, mean=0.380497, stdev=0.140882, best fit=0.499685,
indivs=631000, elapsed_secs=24, mean=0.374382, stdev=0.136928, best fit=0.508418,
indivs=641000, elapsed_secs=24, mean=0.398370, stdev=0.161389, best fit=0.568013,
indivs=651000, elapsed_secs=24, mean=0.394867, stdev=0.218484, best fit=0.647933,
indivs=661000, elapsed_secs=25, mean=0.397439, stdev=0.214456, best fit=0.652027,
indivs=671000, elapsed_secs=25, mean=0.398256, stdev=0.210098, best fit=0.652948,
indivs=681000, elapsed_secs=25, mean=0.410926, stdev=0.207219, best fit=0.655448,
indivs=691000, elapsed_secs=26, mean=0.397664, stdev=0.217312, best fit=0.658730,
indivs=701000, elapsed_secs=26, mean=0.401629, stdev=0.214817, best fit=0.658730,
indivs=711000, elapsed_secs=27, mean=0.405718, stdev=0.214607, best fit=0.664148,
indivs=721000, elapsed_secs=27, mean=0.385328, stdev=0.227353, best fit=0.672343,
indivs=731000, elapsed_secs=27, mean=0.446050, stdev=0.240946, best fit=0.673055,
indivs=741000, elapsed_secs=28, mean=0.435591, stdev=0.246435, best fit=0.673736,
indivs=751000, elapsed_secs=28, mean=0.449229, stdev=0.235534, best fit=0.673736,
indivs=761000, elapsed_secs=29, mean=0.410699, stdev=0.231671, best fit=0.677619,
indivs=771000, elapsed_secs=29, mean=0.424003, stdev=0.211824, best fit=0.677795,
indivs=781000, elapsed_secs=29, mean=0.426065, stdev=0.213344, best fit=0.679139,
indivs=791000, elapsed_secs=30, mean=0.429335, stdev=0.218884, best fit=0.679240,
indivs=801000, elapsed_secs=30, mean=0.433894, stdev=0.210859, best fit=0.679259,
indivs=811000, elapsed_secs=30, mean=0.437614, stdev=0.215133, best fit=0.682204,
Experiment done. Retrieving candidate algorithm.
Search fitness for candidate algorithm = 0.682954
Evaluating candidate algorithm from experiment (on T_select tasks)... 
Select fitness for candidate algorithm = 0.610470
Running evolution experiment (on the T_search tasks)...
indivs=1000, elapsed_secs=0, mean=0.279217, stdev=0.107552, best fit=0.341742,
indivs=11000, elapsed_secs=0, mean=0.326150, stdev=0.052521, best fit=0.342878,
indivs=21000, elapsed_secs=1, mean=0.319613, stdev=0.070396, best fit=0.342907,
indivs=31000, elapsed_secs=1, mean=0.326009, stdev=0.057117, best fit=0.342923,
indivs=41000, elapsed_secs=1, mean=0.330372, stdev=0.050190, best fit=0.343191,
indivs=51000, elapsed_secs=2, mean=0.325273, stdev=0.061018, best fit=0.343193,
indivs=61000, elapsed_secs=2, mean=0.326890, stdev=0.060745, best fit=0.343193,
indivs=71000, elapsed_secs=3, mean=0.322492, stdev=0.067881, best fit=0.343193,
indivs=81000, elapsed_secs=3, mean=0.322338, stdev=0.068038, best fit=0.343194,
indivs=91000, elapsed_secs=3, mean=0.326753, stdev=0.060577, best fit=0.343194,
indivs=101000, elapsed_secs=4, mean=0.363412, stdev=0.074320, best fit=0.408776,
indivs=111000, elapsed_secs=4, mean=0.359057, stdev=0.081459, best fit=0.408780,
indivs=121000, elapsed_secs=4, mean=0.357616, stdev=0.086931, best fit=0.408780,
indivs=131000, elapsed_secs=5, mean=0.356420, stdev=0.086323, best fit=0.408780,
indivs=141000, elapsed_secs=5, mean=0.353501, stdev=0.090837, best fit=0.408780,
indivs=151000, elapsed_secs=6, mean=0.364242, stdev=0.071862, best fit=0.408781,
indivs=161000, elapsed_secs=6, mean=0.364218, stdev=0.075320, best fit=0.408781,
indivs=171000, elapsed_secs=6, mean=0.354516, stdev=0.088699, best fit=0.423961,
indivs=181000, elapsed_secs=7, mean=0.352525, stdev=0.093247, best fit=0.424157,
indivs=191000, elapsed_secs=7, mean=0.354503, stdev=0.100104, best fit=0.424160,
indivs=201000, elapsed_secs=8, mean=0.361058, stdev=0.089053, best fit=0.424216,
indivs=211000, elapsed_secs=8, mean=0.367392, stdev=0.083708, best fit=0.424221,
indivs=221000, elapsed_secs=8, mean=0.366376, stdev=0.083855, best fit=0.424221,
indivs=231000, elapsed_secs=9, mean=0.361535, stdev=0.089054, best fit=0.424221,
indivs=241000, elapsed_secs=9, mean=0.374374, stdev=0.076014, best fit=0.424223,
indivs=251000, elapsed_secs=10, mean=0.365021, stdev=0.089142, best fit=0.424223,
indivs=261000, elapsed_secs=10, mean=0.354262, stdev=0.098487, best fit=0.424223,
indivs=271000, elapsed_secs=10, mean=0.358766, stdev=0.092871, best fit=0.424223,
indivs=281000, elapsed_secs=11, mean=0.360084, stdev=0.092709, best fit=0.424223,
indivs=291000, elapsed_secs=11, mean=0.359626, stdev=0.089467, best fit=0.424223,
indivs=301000, elapsed_secs=12, mean=0.358849, stdev=0.090696, best fit=0.424223,
indivs=311000, elapsed_secs=12, mean=0.359794, stdev=0.090041, best fit=0.424223,
indivs=321000, elapsed_secs=12, mean=0.360796, stdev=0.093713, best fit=0.424223,
indivs=331000, elapsed_secs=13, mean=0.357796, stdev=0.091953, best fit=0.424223,
indivs=341000, elapsed_secs=13, mean=0.342775, stdev=0.099469, best fit=0.424223,
indivs=351000, elapsed_secs=14, mean=0.340670, stdev=0.097373, best fit=0.424223,
indivs=361000, elapsed_secs=14, mean=0.350337, stdev=0.091620, best fit=0.424223,
indivs=371000, elapsed_secs=14, mean=0.340004, stdev=0.098201, best fit=0.424223,
indivs=381000, elapsed_secs=15, mean=0.344576, stdev=0.094289, best fit=0.424223,
indivs=391000, elapsed_secs=15, mean=0.350390, stdev=0.089689, best fit=0.424223,
indivs=401000, elapsed_secs=15, mean=0.348234, stdev=0.089152, best fit=0.424223,
indivs=411000, elapsed_secs=16, mean=0.342775, stdev=0.095629, best fit=0.424223,
indivs=421000, elapsed_secs=16, mean=0.345114, stdev=0.092284, best fit=0.424223,
indivs=431000, elapsed_secs=17, mean=0.346728, stdev=0.088179, best fit=0.424223,
indivs=441000, elapsed_secs=17, mean=0.346513, stdev=0.090870, best fit=0.424223,
indivs=451000, elapsed_secs=17, mean=0.341285, stdev=0.101206, best fit=0.424223,
indivs=461000, elapsed_secs=18, mean=0.340940, stdev=0.098997, best fit=0.424223,
indivs=471000, elapsed_secs=18, mean=0.349904, stdev=0.086191, best fit=0.424223,
indivs=481000, elapsed_secs=19, mean=0.348643, stdev=0.089105, best fit=0.424223,
indivs=491000, elapsed_secs=19, mean=0.349868, stdev=0.084177, best fit=0.424223,
indivs=501000, elapsed_secs=19, mean=0.347760, stdev=0.090110, best fit=0.424223,
indivs=511000, elapsed_secs=20, mean=0.346982, stdev=0.089263, best fit=0.424223,
indivs=521000, elapsed_secs=20, mean=0.351759, stdev=0.092029, best fit=0.424223,
indivs=531000, elapsed_secs=21, mean=0.345931, stdev=0.092409, best fit=0.428451,
indivs=541000, elapsed_secs=21, mean=0.336502, stdev=0.109134, best fit=0.433196,
indivs=551000, elapsed_secs=21, mean=0.342609, stdev=0.097381, best fit=0.433304,
indivs=561000, elapsed_secs=22, mean=0.356089, stdev=0.093859, best fit=0.433352,
indivs=571000, elapsed_secs=22, mean=0.349330, stdev=0.097085, best fit=0.433434,
indivs=581000, elapsed_secs=23, mean=0.497720, stdev=0.362466, best fit=0.961436,
indivs=591000, elapsed_secs=23, mean=0.488862, stdev=0.368599, best fit=0.961436,
indivs=601000, elapsed_secs=23, mean=0.482718, stdev=0.356863, best fit=0.961436,
indivs=611000, elapsed_secs=24, mean=0.488638, stdev=0.366786, best fit=0.961436,
indivs=621000, elapsed_secs=24, mean=0.467693, stdev=0.364106, best fit=0.961436,
indivs=631000, elapsed_secs=24, mean=0.491078, stdev=0.371909, best fit=0.961436,
indivs=641000, elapsed_secs=25, mean=0.485679, stdev=0.352349, best fit=0.968031,
indivs=651000, elapsed_secs=25, mean=0.470825, stdev=0.357773, best fit=0.968031,
indivs=661000, elapsed_secs=25, mean=0.460537, stdev=0.375495, best fit=0.996217,
indivs=671000, elapsed_secs=26, mean=0.474407, stdev=0.378265, best fit=0.996217,
indivs=681000, elapsed_secs=26, mean=0.453406, stdev=0.369909, best fit=0.996217,
indivs=691000, elapsed_secs=27, mean=0.449588, stdev=0.367627, best fit=0.996217,
indivs=701000, elapsed_secs=27, mean=0.472152, stdev=0.376050, best fit=0.996217,
indivs=711000, elapsed_secs=27, mean=0.473441, stdev=0.370132, best fit=0.996217,
indivs=721000, elapsed_secs=28, mean=0.466033, stdev=0.371160, best fit=0.996217,
indivs=731000, elapsed_secs=28, mean=0.471096, stdev=0.385937, best fit=0.996217,
indivs=741000, elapsed_secs=28, mean=0.459221, stdev=0.372071, best fit=0.996217,
indivs=751000, elapsed_secs=29, mean=0.451739, stdev=0.369293, best fit=0.996217,
indivs=761000, elapsed_secs=29, mean=0.469650, stdev=0.382288, best fit=0.996217,
indivs=771000, elapsed_secs=29, mean=0.443571, stdev=0.366318, best fit=0.996217,
indivs=781000, elapsed_secs=30, mean=0.456721, stdev=0.374963, best fit=0.996217,
indivs=791000, elapsed_secs=30, mean=0.468292, stdev=0.374695, best fit=0.996217,
indivs=801000, elapsed_secs=30, mean=0.480075, stdev=0.374380, best fit=0.996217,
indivs=811000, elapsed_secs=31, mean=0.456947, stdev=0.373313, best fit=0.996235,
indivs=821000, elapsed_secs=31, mean=0.449275, stdev=0.371610, best fit=0.996526,
Experiment done. Retrieving candidate algorithm.
Search fitness for candidate algorithm = 0.998831
Evaluating candidate algorithm from experiment (on T_select tasks)... 
Select fitness for candidate algorithm = 0.969144
Select fitness is the best so far. 
Running evolution experiment (on the T_search tasks)...
indivs=1000, elapsed_secs=1, mean=0.266589, stdev=0.107598, best fit=0.329833,
indivs=11000, elapsed_secs=1, mean=0.358246, stdev=0.090098, best fit=0.414497,
indivs=21000, elapsed_secs=1, mean=0.363782, stdev=0.086992, best fit=0.414586,
indivs=31000, elapsed_secs=2, mean=0.348190, stdev=0.100841, best fit=0.416322,
indivs=41000, elapsed_secs=2, mean=0.351244, stdev=0.095111, best fit=0.439265,
indivs=51000, elapsed_secs=2, mean=0.358834, stdev=0.093643, best fit=0.444449,
indivs=61000, elapsed_secs=3, mean=0.358120, stdev=0.101359, best fit=0.446120,
indivs=71000, elapsed_secs=3, mean=0.362309, stdev=0.096736, best fit=0.446367,
indivs=81000, elapsed_secs=4, mean=0.358423, stdev=0.098525, best fit=0.446464,
indivs=91000, elapsed_secs=4, mean=0.355168, stdev=0.102574, best fit=0.446548,
indivs=101000, elapsed_secs=4, mean=0.354809, stdev=0.103934, best fit=0.446553,
indivs=111000, elapsed_secs=5, mean=0.355764, stdev=0.101071, best fit=0.446553,
indivs=121000, elapsed_secs=5, mean=0.354300, stdev=0.103186, best fit=0.446553,
indivs=131000, elapsed_secs=5, mean=0.350190, stdev=0.107216, best fit=0.446553,
indivs=141000, elapsed_secs=6, mean=0.357526, stdev=0.098782, best fit=0.446553,
indivs=151000, elapsed_secs=6, mean=0.356170, stdev=0.102856, best fit=0.446553,
indivs=161000, elapsed_secs=7, mean=0.351510, stdev=0.105284, best fit=0.446554,
indivs=171000, elapsed_secs=7, mean=0.350141, stdev=0.116781, best fit=0.446555,
indivs=181000, elapsed_secs=7, mean=0.347934, stdev=0.110340, best fit=0.446555,
indivs=191000, elapsed_secs=8, mean=0.344743, stdev=0.112652, best fit=0.446555,
indivs=201000, elapsed_secs=8, mean=0.357771, stdev=0.098709, best fit=0.446556,
indivs=211000, elapsed_secs=8, mean=0.360505, stdev=0.103303, best fit=0.446556,
indivs=221000, elapsed_secs=9, mean=0.359022, stdev=0.104391, best fit=0.446556,
indivs=231000, elapsed_secs=9, mean=0.357172, stdev=0.103960, best fit=0.446556,
indivs=241000, elapsed_secs=10, mean=0.351766, stdev=0.108601, best fit=0.446556,
indivs=251000, elapsed_secs=10, mean=0.353515, stdev=0.106363, best fit=0.446556,
indivs=261000, elapsed_secs=10, mean=0.350662, stdev=0.115105, best fit=0.446556,
indivs=271000, elapsed_secs=11, mean=0.358932, stdev=0.103187, best fit=0.446556,
indivs=281000, elapsed_secs=11, mean=0.355975, stdev=0.105136, best fit=0.446556,
indivs=291000, elapsed_secs=11, mean=0.359234, stdev=0.101799, best fit=0.446556,
indivs=301000, elapsed_secs=12, mean=0.352114, stdev=0.109038, best fit=0.446556,
indivs=311000, elapsed_secs=12, mean=0.339029, stdev=0.131068, best fit=0.454130,
indivs=321000, elapsed_secs=13, mean=0.327318, stdev=0.136123, best fit=0.454688,
indivs=331000, elapsed_secs=13, mean=0.336182, stdev=0.131610, best fit=0.454689,
indivs=341000, elapsed_secs=13, mean=0.341541, stdev=0.126657, best fit=0.454689,
indivs=351000, elapsed_secs=14, mean=0.345309, stdev=0.120599, best fit=0.456957,
indivs=361000, elapsed_secs=14, mean=0.344698, stdev=0.122905, best fit=0.458849,
indivs=371000, elapsed_secs=14, mean=0.351585, stdev=0.116699, best fit=0.459833,
indivs=381000, elapsed_secs=15, mean=0.348213, stdev=0.121716, best fit=0.459940,
indivs=391000, elapsed_secs=15, mean=0.348913, stdev=0.116930, best fit=0.459994,
indivs=401000, elapsed_secs=16, mean=0.345930, stdev=0.121538, best fit=0.460033,
indivs=411000, elapsed_secs=16, mean=0.346912, stdev=0.117131, best fit=0.460074,
indivs=421000, elapsed_secs=16, mean=0.354771, stdev=0.113953, best fit=0.460095,
indivs=431000, elapsed_secs=17, mean=0.345322, stdev=0.117250, best fit=0.460203,
indivs=441000, elapsed_secs=17, mean=0.349849, stdev=0.118466, best fit=0.460207,
indivs=451000, elapsed_secs=17, mean=0.349125, stdev=0.114366, best fit=0.460209,
indivs=461000, elapsed_secs=18, mean=0.348233, stdev=0.121111, best fit=0.460209,
indivs=471000, elapsed_secs=18, mean=0.338047, stdev=0.126026, best fit=0.460209,
indivs=481000, elapsed_secs=19, mean=0.354041, stdev=0.115141, best fit=0.460209,
indivs=491000, elapsed_secs=19, mean=0.353019, stdev=0.118684, best fit=0.460209,
indivs=501000, elapsed_secs=19, mean=0.342629, stdev=0.117601, best fit=0.460209,
indivs=511000, elapsed_secs=20, mean=0.352283, stdev=0.118170, best fit=0.460209,
indivs=521000, elapsed_secs=20, mean=0.358059, stdev=0.112713, best fit=0.460209,
indivs=531000, elapsed_secs=20, mean=0.344160, stdev=0.124107, best fit=0.460209,
indivs=541000, elapsed_secs=21, mean=0.347078, stdev=0.117259, best fit=0.460209,
indivs=551000, elapsed_secs=21, mean=0.345372, stdev=0.119973, best fit=0.460210,
indivs=561000, elapsed_secs=22, mean=0.345897, stdev=0.116839, best fit=0.460210,
indivs=571000, elapsed_secs=22, mean=0.345339, stdev=0.115775, best fit=0.460210,
indivs=581000, elapsed_secs=22, mean=0.346770, stdev=0.117337, best fit=0.460210,
indivs=591000, elapsed_secs=23, mean=0.347494, stdev=0.120041, best fit=0.460211,
indivs=601000, elapsed_secs=23, mean=0.348073, stdev=0.114567, best fit=0.460218,
indivs=611000, elapsed_secs=23, mean=0.348321, stdev=0.120924, best fit=0.460230,
indivs=621000, elapsed_secs=24, mean=0.346381, stdev=0.118899, best fit=0.460230,
indivs=631000, elapsed_secs=24, mean=0.343616, stdev=0.122084, best fit=0.460231,
indivs=641000, elapsed_secs=24, mean=0.350158, stdev=0.117598, best fit=0.460231,
indivs=651000, elapsed_secs=25, mean=0.343265, stdev=0.121362, best fit=0.460231,
indivs=661000, elapsed_secs=25, mean=0.351345, stdev=0.114866, best fit=0.460231,
indivs=671000, elapsed_secs=26, mean=0.349531, stdev=0.122235, best fit=0.460231,
indivs=681000, elapsed_secs=26, mean=0.350389, stdev=0.118477, best fit=0.460231,
indivs=691000, elapsed_secs=26, mean=0.355269, stdev=0.116292, best fit=0.460231,
indivs=701000, elapsed_secs=27, mean=0.347990, stdev=0.116183, best fit=0.460231,
indivs=711000, elapsed_secs=27, mean=0.350525, stdev=0.116504, best fit=0.460231,
indivs=721000, elapsed_secs=27, mean=0.339330, stdev=0.125282, best fit=0.460231,
indivs=731000, elapsed_secs=28, mean=0.348399, stdev=0.116194, best fit=0.460231,
indivs=741000, elapsed_secs=28, mean=0.343992, stdev=0.118038, best fit=0.460231,
indivs=751000, elapsed_secs=29, mean=0.344736, stdev=0.122141, best fit=0.460231,
indivs=761000, elapsed_secs=29, mean=0.344619, stdev=0.126298, best fit=0.460231,
indivs=771000, elapsed_secs=29, mean=0.349354, stdev=0.114590, best fit=0.460231,
indivs=781000, elapsed_secs=30, mean=0.341881, stdev=0.120935, best fit=0.460231,
indivs=791000, elapsed_secs=30, mean=0.346399, stdev=0.119147, best fit=0.460231,
indivs=801000, elapsed_secs=30, mean=0.349932, stdev=0.113979, best fit=0.460231,
indivs=811000, elapsed_secs=31, mean=0.348255, stdev=0.120694, best fit=0.460231,
indivs=821000, elapsed_secs=31, mean=0.348786, stdev=0.116926, best fit=0.460231,
indivs=831000, elapsed_secs=31, mean=0.347806, stdev=0.113500, best fit=0.460231,
indivs=841000, elapsed_secs=32, mean=0.348296, stdev=0.119739, best fit=0.460231,
indivs=851000, elapsed_secs=32, mean=0.343311, stdev=0.121498, best fit=0.460231,
indivs=861000, elapsed_secs=33, mean=0.341207, stdev=0.125232, best fit=0.460231,
indivs=871000, elapsed_secs=33, mean=0.348822, stdev=0.116150, best fit=0.460231,
indivs=881000, elapsed_secs=33, mean=0.352557, stdev=0.113053, best fit=0.460231,
Experiment done. Retrieving candidate algorithm.
Search fitness for candidate algorithm = 0.460231
Evaluating candidate algorithm from experiment (on T_select tasks)... 
Select fitness for candidate algorithm = 0.264674
Running evolution experiment (on the T_search tasks)...
indivs=1000, elapsed_secs=0, mean=0.265130, stdev=0.102708, best fit=0.326707,
indivs=11000, elapsed_secs=1, mean=0.304724, stdev=0.069362, best fit=0.327372,
indivs=21000, elapsed_secs=1, mean=0.300816, stdev=0.078347, best fit=0.330369,
indivs=31000, elapsed_secs=2, mean=0.333734, stdev=0.095502, best fit=0.388003,
indivs=41000, elapsed_secs=2, mean=0.328035, stdev=0.104647, best fit=0.388003,
indivs=51000, elapsed_secs=2, mean=0.314716, stdev=0.111725, best fit=0.388020,
indivs=61000, elapsed_secs=3, mean=0.315451, stdev=0.113140, best fit=0.388020,
indivs=71000, elapsed_secs=3, mean=0.450257, stdev=0.298689, best fit=0.819700,
indivs=81000, elapsed_secs=3, mean=0.433697, stdev=0.292536, best fit=0.820489,
indivs=91000, elapsed_secs=4, mean=0.424412, stdev=0.291247, best fit=0.820491,
indivs=101000, elapsed_secs=4, mean=0.422556, stdev=0.293506, best fit=0.820491,
indivs=111000, elapsed_secs=5, mean=0.454851, stdev=0.303315, best fit=0.820491,
indivs=121000, elapsed_secs=5, mean=0.437618, stdev=0.293087, best fit=0.820705,
indivs=131000, elapsed_secs=5, mean=0.447501, stdev=0.307220, best fit=0.820721,
indivs=141000, elapsed_secs=6, mean=0.467883, stdev=0.297090, best fit=0.820724,
indivs=151000, elapsed_secs=6, mean=0.457378, stdev=0.304348, best fit=0.821290,
indivs=161000, elapsed_secs=6, mean=0.454647, stdev=0.300763, best fit=0.823938,
indivs=171000, elapsed_secs=7, mean=0.454375, stdev=0.313766, best fit=0.824351,
indivs=181000, elapsed_secs=7, mean=0.439183, stdev=0.306518, best fit=0.824832,
indivs=191000, elapsed_secs=8, mean=0.457509, stdev=0.307028, best fit=0.824842,
indivs=201000, elapsed_secs=8, mean=0.457775, stdev=0.302529, best fit=0.824842,
indivs=211000, elapsed_secs=8, mean=0.435590, stdev=0.304285, best fit=0.824859,
indivs=221000, elapsed_secs=9, mean=0.456213, stdev=0.308134, best fit=0.824859,
indivs=231000, elapsed_secs=9, mean=0.450570, stdev=0.299828, best fit=0.824863,
indivs=241000, elapsed_secs=9, mean=0.449128, stdev=0.304295, best fit=0.824863,
indivs=251000, elapsed_secs=10, mean=0.446662, stdev=0.306211, best fit=0.824863,
indivs=261000, elapsed_secs=10, mean=0.477221, stdev=0.304371, best fit=0.824863,
indivs=271000, elapsed_secs=10, mean=0.460462, stdev=0.305275, best fit=0.824863,
indivs=281000, elapsed_secs=11, mean=0.436531, stdev=0.298395, best fit=0.824863,
indivs=291000, elapsed_secs=11, mean=0.443546, stdev=0.300794, best fit=0.824863,
indivs=301000, elapsed_secs=12, mean=0.464540, stdev=0.299095, best fit=0.824863,
indivs=311000, elapsed_secs=12, mean=0.457976, stdev=0.303333, best fit=0.824863,
indivs=321000, elapsed_secs=12, mean=0.450342, stdev=0.303158, best fit=0.824863,
indivs=331000, elapsed_secs=13, mean=0.461520, stdev=0.305794, best fit=0.824863,
indivs=341000, elapsed_secs=13, mean=0.440852, stdev=0.301230, best fit=0.824863,
indivs=351000, elapsed_secs=13, mean=0.457664, stdev=0.306883, best fit=0.824863,
indivs=361000, elapsed_secs=14, mean=0.458917, stdev=0.309316, best fit=0.824863,
indivs=371000, elapsed_secs=14, mean=0.447306, stdev=0.301188, best fit=0.824863,
indivs=381000, elapsed_secs=14, mean=0.447302, stdev=0.302844, best fit=0.824863,
indivs=391000, elapsed_secs=15, mean=0.457107, stdev=0.301119, best fit=0.824863,
indivs=401000, elapsed_secs=15, mean=0.461978, stdev=0.307047, best fit=0.824863,
indivs=411000, elapsed_secs=15, mean=0.454138, stdev=0.305566, best fit=0.824863,
indivs=421000, elapsed_secs=16, mean=0.443070, stdev=0.303012, best fit=0.824863,
indivs=431000, elapsed_secs=16, mean=0.444482, stdev=0.305300, best fit=0.824863,
indivs=441000, elapsed_secs=16, mean=0.444528, stdev=0.298729, best fit=0.824863,
indivs=451000, elapsed_secs=17, mean=0.517962, stdev=0.420029, best fit=0.999830,
indivs=461000, elapsed_secs=17, mean=0.537095, stdev=0.403668, best fit=0.999830,
indivs=471000, elapsed_secs=18, mean=0.517984, stdev=0.395025, best fit=0.999966,
indivs=481000, elapsed_secs=18, mean=0.510667, stdev=0.397123, best fit=0.999968,
indivs=491000, elapsed_secs=18, mean=0.608532, stdev=0.408412, best fit=0.999970,
indivs=501000, elapsed_secs=19, mean=0.569817, stdev=0.400297, best fit=0.999970,
indivs=511000, elapsed_secs=19, mean=0.527256, stdev=0.398867, best fit=0.999970,
indivs=521000, elapsed_secs=19, mean=0.529269, stdev=0.390504, best fit=0.999970,
indivs=531000, elapsed_secs=20, mean=0.521161, stdev=0.390918, best fit=0.999970,
indivs=541000, elapsed_secs=20, mean=0.512286, stdev=0.385592, best fit=0.999970,
indivs=551000, elapsed_secs=20, mean=0.536913, stdev=0.383727, best fit=0.999970,
indivs=561000, elapsed_secs=21, mean=0.542555, stdev=0.397490, best fit=0.999970,
indivs=571000, elapsed_secs=21, mean=0.533884, stdev=0.388057, best fit=0.999970,
indivs=581000, elapsed_secs=22, mean=0.553980, stdev=0.398825, best fit=0.999970,
indivs=591000, elapsed_secs=22, mean=0.537822, stdev=0.402300, best fit=0.999970,
indivs=601000, elapsed_secs=22, mean=0.526511, stdev=0.390519, best fit=0.999970,
indivs=611000, elapsed_secs=23, mean=0.526896, stdev=0.387481, best fit=0.999970,
indivs=621000, elapsed_secs=23, mean=0.523595, stdev=0.389021, best fit=0.999970,
indivs=631000, elapsed_secs=23, mean=0.515459, stdev=0.390479, best fit=0.999970,
indivs=641000, elapsed_secs=24, mean=0.529991, stdev=0.391319, best fit=0.999970,
indivs=651000, elapsed_secs=24, mean=0.532380, stdev=0.393890, best fit=0.999970,
indivs=661000, elapsed_secs=24, mean=0.534259, stdev=0.390291, best fit=0.999970,
indivs=671000, elapsed_secs=25, mean=0.547763, stdev=0.393774, best fit=0.999970,
indivs=681000, elapsed_secs=25, mean=0.554850, stdev=0.401123, best fit=0.999970,
indivs=691000, elapsed_secs=25, mean=0.549968, stdev=0.400554, best fit=0.999970,
indivs=701000, elapsed_secs=26, mean=0.554613, stdev=0.398461, best fit=0.999970,
indivs=711000, elapsed_secs=26, mean=0.563232, stdev=0.392786, best fit=0.999970,
indivs=721000, elapsed_secs=27, mean=0.528150, stdev=0.391215, best fit=0.999970,
indivs=731000, elapsed_secs=27, mean=0.546819, stdev=0.399176, best fit=0.999970,
indivs=741000, elapsed_secs=27, mean=0.548712, stdev=0.396098, best fit=0.999970,
indivs=751000, elapsed_secs=28, mean=0.535943, stdev=0.389320, best fit=0.999970,
indivs=761000, elapsed_secs=28, mean=0.523597, stdev=0.391677, best fit=0.999970,
indivs=771000, elapsed_secs=28, mean=0.546528, stdev=0.391486, best fit=0.999970,
indivs=781000, elapsed_secs=29, mean=0.533011, stdev=0.399756, best fit=0.999970,
indivs=791000, elapsed_secs=29, mean=0.544726, stdev=0.397214, best fit=0.999970,
indivs=801000, elapsed_secs=29, mean=0.533881, stdev=0.393359, best fit=0.999970,
indivs=811000, elapsed_secs=30, mean=0.558203, stdev=0.392046, best fit=0.999970,
indivs=821000, elapsed_secs=30, mean=0.557329, stdev=0.394391, best fit=0.999970,
indivs=831000, elapsed_secs=31, mean=0.518744, stdev=0.391582, best fit=0.999970,
indivs=841000, elapsed_secs=31, mean=0.549726, stdev=0.393328, best fit=0.999970,
indivs=851000, elapsed_secs=31, mean=0.554975, stdev=0.393543, best fit=0.999970,
indivs=861000, elapsed_secs=32, mean=0.549428, stdev=0.390896, best fit=0.999970,
indivs=871000, elapsed_secs=32, mean=0.573971, stdev=0.402585, best fit=0.999970,
indivs=881000, elapsed_secs=32, mean=0.546848, stdev=0.399546, best fit=0.999970,
indivs=891000, elapsed_secs=33, mean=0.534126, stdev=0.392123, best fit=0.999970,
indivs=901000, elapsed_secs=33, mean=0.538195, stdev=0.398802, best fit=0.999970,
indivs=911000, elapsed_secs=33, mean=0.554080, stdev=0.396342, best fit=0.999970,
indivs=921000, elapsed_secs=34, mean=0.529548, stdev=0.396660, best fit=0.999970,
indivs=931000, elapsed_secs=34, mean=0.534628, stdev=0.394360, best fit=0.999970,
indivs=941000, elapsed_secs=35, mean=0.521202, stdev=0.395851, best fit=0.999970,
Experiment done. Retrieving candidate algorithm.
Search fitness for candidate algorithm = 0.999970
Evaluating candidate algorithm from experiment (on T_select tasks)... 
Select fitness for candidate algorithm = 1.000000
Select fitness is the best so far. 

Final evaluation of best algorithm (on unseen tasks)...
Final evaluation fitness (on unseen data) = 1.000000
Algorithm found: 
def Setup():
  v2 = s2 * v0
  v2 = s0 * v1
  s3 = dot(v1, v0)
  s1 = 0.987982
  v1 = s1 * v1
  s1 = dot(v1, v2)
  s3 = 0.422194
  v1 = s1 * v0
  s2 = -0.156025
  s1 = s1 - s1
def Predict():
  s1 = dot(v0, v2)
  s1 = dot(v1, v0)
def Learn():
  v2 = s2 * v2
  s2 = -0.29745
  s2 = dot(v0, v2)
  s1 = s0 - s1
  s1 = s1 - s2
  v1 = v2 + v1
  s2 = s3 * s1
  v2 = s3 * v0

(base) /temp/google-research/automl_zero$ 
```
