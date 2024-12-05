<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/IDv2YZ5p7QHF5SxYZBMGdQ" title="Async IO in Python: A Complete Walkthrough" target="_blank">Async IO in Python: A Complete Walkthrough</a></li>
<li><a href="/rltoken/1neoNd8gRS_mn52IQd5WTQ" title="asyncio - Asynchronous I/O" target="_blank">asyncio - Asynchronous I/O</a></li>
<li><a href="/rltoken/XTxPUx9tDxZ51zhIUrSvPw" title="random.uniform" target="_blank">random.uniform</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/tPcivo9_iizt6VTAvNcqow" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li><code>async</code> and <code>await</code> syntax</li>
<li>How to execute an async program with <code>asyncio</code></li>
<li>How to run concurrent coroutines</li>
<li>How to create <code>asyncio</code> tasks</li>
<li>How to use the <code>random</code> module</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.9)</li>
<li>All your files should end with a new line</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5.x)</li>
<li>All your functions and coroutines must be type-annotated.</li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your functions should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code></li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

  </div>
</div>
        </div>
        <div role="tabpanel" class="tab-pane " id="concepts">
            <div class="panel panel-default">
    <div class="panel-body">
      <p>
        <em>For this project, we expect you to look at these concepts:</em>
      </p>

      <ul>
          <li>
            <a href="/concepts/1173">Python - Asynchronous execution</a>
          </li>
          <li>
            <a href="/concepts/1174">Python - Asynchronous Programming</a>
          </li>
      </ul>
    </div>
  </div>

        </div>
      </div>
    </div>

        <h2 id="task-container" class="gap">Tasks</h2>

  <div class="col-sm-12 col-md-12 col-lg-8 xol-xl-9">
      <div data-role="task21447" data-position="1" id="task-num-0">
        <div class="panel panel-default task-card " id="task-21447">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. The basics of async
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write an asynchronous coroutine that takes in an integer argument (<code>max_delay</code>, with a default value of 10) named <code>wait_random</code> that waits for a random delay between 0 and <code>max_delay</code> (included and float value) seconds and eventually returns it.</p>

<p>Use the <code>random</code> module.</p>

<pre><code>bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__(&#39;0-basic_async_syntax&#39;).wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
            <li>Directory: <code>python_async_function</code></li>
            <li>File: <code>0-basic_async_syntax.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="21447" data-batch-id="843" data-toggle="modal" data-target="#task-21447-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-21447-users-done-modal" data-task-id="21447" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "0. The basics of async"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="21447" data-toggle="modal" data-target="#task-test-correction-21447-correction-modal" id="task-num-0-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-21447-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "0. The basics of async"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="21447">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="21447">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="21447">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4 text-right">
            <strong class="text-primary">
              <span id="task-21447-score-info-score">0</span>/5
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task21448" data-position="2" id="task-num-1">
        <div class="panel panel-default task-card " id="task-21448">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Let&#39;s execute multiple coroutines at the same time with async
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Import <code>wait_random</code> from the previous python file that you&rsquo;ve written and write an async routine called <code>wait_n</code> that takes in 2 int arguments (in this order): <code>n</code> and <code>max_delay</code>. You will spawn <code>wait_random</code> <code>n</code> times with the specified <code>max_delay</code>.</p>

<p><code>wait_n</code> should return the list of all the delays (float values). The list of the delays should be in ascending order without using <code>sort()</code> because of concurrency.</p>

<pre><code>bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
&#39;&#39;&#39;
Test file for printing the correct output of the wait_n coroutine
&#39;&#39;&#39;
import asyncio

wait_n = __import__(&#39;1-concurrent_coroutines&#39;).wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
</code></pre>

<p>The output for your answers might look a little different and that&rsquo;s okay.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
            <li>Directory: <code>python_async_function</code></li>
            <li>File: <code>1-concurrent_coroutines.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="21448" data-batch-id="843" data-toggle="modal" data-target="#task-21448-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-21448-users-done-modal" data-task-id="21448" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "1. Let&#39;s execute multiple coroutines at the same time with async"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="21448" data-toggle="modal" data-target="#task-test-correction-21448-correction-modal" id="task-num-1-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-21448-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "1. Let&#39;s execute multiple coroutines at the same time with async"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="21448">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="21448">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="21448">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4 text-right">
            <strong class="text-primary">
              <span id="task-21448-score-info-score">0</span>/7
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task21449" data-position="3" id="task-num-2">
        <div class="panel panel-default task-card " id="task-21449">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Measure the runtime
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>From the previous file, import <code>wait_n</code> into <code>2-measure_runtime.py</code>.</p>

<p>Create a <code>measure_time</code> function with integers <code>n</code> and <code>max_delay</code> as arguments that measures the total execution time for <code>wait_n(n, max_delay)</code>, and returns <code>total_time / n</code>.  Your function should return a float.</p>

<p>Use the <code>time</code> module to measure an approximate elapsed time.</p>

<pre><code>bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

measure_time = __import__(&#39;2-measure_runtime&#39;).measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

bob@dylan:~$ ./2-main.py
1.759705400466919
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
            <li>Directory: <code>python_async_function</code></li>
            <li>File: <code>2-measure_runtime.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="21449" data-batch-id="843" data-toggle="modal" data-target="#task-21449-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-21449-users-done-modal" data-task-id="21449" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "2. Measure the runtime"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="21449" data-toggle="modal" data-target="#task-test-correction-21449-correction-modal" id="task-num-2-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-21449-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "2. Measure the runtime"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="21449">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="21449">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="21449">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4 text-right">
            <strong class="text-primary">
              <span id="task-21449-score-info-score">0</span>/4
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task21450" data-position="4" id="task-num-3">
        <div class="panel panel-default task-card " id="task-21450">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Tasks
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Import <code>wait_random</code> from <code>0-basic_async_syntax</code>.</p>

<p>Write a function (do not create an async function, use the regular function syntax to do this) <code>task_wait_random</code> that takes an integer <code>max_delay</code> and returns a <code>asyncio.Task</code>.</p>

<pre><code>bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__(&#39;3-tasks&#39;).task_wait_random


async def test(max_delay: int) -&gt; float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

bob@dylan:~$ ./3-main.py
&lt;class &#39;_asyncio.Task&#39;&gt;
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
            <li>Directory: <code>python_async_function</code></li>
            <li>File: <code>3-tasks.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="21450" data-batch-id="843" data-toggle="modal" data-target="#task-21450-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-21450-users-done-modal" data-task-id="21450" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "3. Tasks"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="21450" data-toggle="modal" data-target="#task-test-correction-21450-correction-modal" id="task-num-3-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-21450-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "3. Tasks"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="21450">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="21450">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="21450">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4 text-right">
            <strong class="text-primary">
              <span id="task-21450-score-info-score">0</span>/4
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task21451" data-position="4" id="task-num-4">
        <div class="panel panel-default task-card " id="task-21451">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Tasks
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Take the code from <code>wait_n</code> and alter it into a new function <code>task_wait_n</code>.  The code is nearly identical to <code>wait_n</code> except <code>task_wait_random</code> is being called.</p>

<pre><code>bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__(&#39;4-tasks&#39;).task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

bob@dylan:~$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
            <li>Directory: <code>python_async_function</code></li>
            <li>File: <code>4-tasks.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="21451" data-batch-id="843" data-toggle="modal" data-target="#task-21451-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-21451-users-done-modal" data-task-id="21451" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "4. Tasks"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="21451" data-toggle="modal" data-target="#task-test-correction-21451-correction-modal" id="task-num-4-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-21451-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "4. Tasks"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="21451">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="21451">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="21451">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4 text-right">
            <strong class="text-primary">
              <span id="task-21451-score-info-score">0</span>/7
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>


      <div class="panel panel-default">
        <div class="panel-body">
          <div class="d-flex justify-content-around">
              <div>
                <a data-toggle="tooltip" title="Python - Variable Annotations" class="btn btn-primary" role="button" href="/projects/2342">
                  <span class="glyphicon glyphicon-arrow-left" aria-hidden="true"></span> Previous project
</a>              </div>
              <form action=/corrections/1131031/skip method="post">
                <input
                  name="authenticity_token"
                  type="hidden"
                  value=IdieTAlF3Piu3NjtOLkDCPxhdc8kxiTI2PJmIUagxldY5BMK_dBw9MdeQMnX6cYR00m5kUdsmlk88GbON8XjVQ
                />
                <button class="btn btn-warning" type="submit">
                  Next project <span class="glyphicon glyphicon-arrow-right" aria-hidden="true"></span>
                </button>
              </form>
          </div>
        </div>
      </div>
  </div>

    <div class="col-sm-12 col-md-12 hidden-lg">
        <div data-react-class="projects/ProjectReview" data-react-props="{&quot;style&quot;:&quot;line&quot;,&quot;correction&quot;:{&quot;statusURI&quot;:&quot;/corrections/1131031/status_self_paced.json&quot;,&quot;startReviewURI&quot;:&quot;/corrections/1131031/start_auto_review_self_paced.json&quot;},&quot;csrfToken&quot;:&quot;EPq4gYPji4NlhcpKXf-q3CK4Qdk7V-vEFKyHgbAn6EBpxjXHd3YnjwwHUm6yr2_FDZCNh1j9VVXwroduwULNQg&quot;,&quot;nextProject&quot;:{&quot;details&quot;:{&quot;curriculum_completed&quot;:false,&quot;message&quot;:&quot;Next project: Python - Async Comprehension&quot;,&quot;uri&quot;:&quot;/projects/2344&quot;},&quot;fetchURI&quot;:&quot;/projects/2343/next&quot;},&quot;pollingInterval&quot;:10000,&quot;progress&quot;:{&quot;auto_review&quot;:{&quot;can_execute&quot;:true,&quot;completion&quot;:{&quot;count&quot;:0,&quot;is_completed&quot;:false,&quot;percentage&quot;:0.0},&quot;inability_to_execute_reason&quot;:null},&quot;tasks&quot;:[{&quot;id&quot;:21447,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:5,&quot;score&quot;:0}},{&quot;id&quot;:21448,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:7,&quot;score&quot;:0}},{&quot;id&quot;:21449,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:4,&quot;score&quot;:0}},{&quot;id&quot;:21450,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:4,&quot;score&quot;:0}},{&quot;id&quot;:21451,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:7,&quot;score&quot;:0}}],&quot;summary&quot;:{&quot;completion&quot;:0.0,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null}},&quot;can_skip&quot;:true,&quot;can_start_peer_review&quot;:false},&quot;peerReview&quot;:null,&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:2343,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/006_color-21d9dd12a952c0dcfa9471902c922dde2a053f71943f7645391458f701eeec29.png&quot;,&quot;name&quot;:&quot;Python - Async&quot;,&quot;score&quot;:{&quot;mandatory&quot;:0.0,&quot;optional&quot;:0.0},&quot;tasksCount&quot;:0},&quot;skipURI&quot;:&quot;/corrections/1131031/skip&quot;,&quot;taskLevelReviewTypeHumanized&quot;:&quot;Your score will be updated as you progress.&quot;}" data-react-cache-id="projects/ProjectReview-0"></div>

    </div>

  <div class="col-xl-3 col-lg-4 hidden-xs hidden-sm hidden-md sticky-nav">
          <div data-react-class="projects/ProjectReview" data-react-props="{&quot;style&quot;:&quot;column&quot;,&quot;correction&quot;:{&quot;statusURI&quot;:&quot;/corrections/1131031/status_self_paced.json&quot;,&quot;startReviewURI&quot;:&quot;/corrections/1131031/start_auto_review_self_paced.json&quot;},&quot;csrfToken&quot;:&quot;CiKngYGTqiSTz2q_GUsqX2NAYCruRROKf5atUgLtvGRzHirHdQYGKPpN8pv2G-9GTGisdI3vrRublK29c4iZZg&quot;,&quot;nextProject&quot;:{&quot;details&quot;:{&quot;curriculum_completed&quot;:false,&quot;message&quot;:&quot;Next project: Python - Async Comprehension&quot;,&quot;uri&quot;:&quot;/projects/2344&quot;},&quot;fetchURI&quot;:&quot;/projects/2343/next&quot;},&quot;pollingInterval&quot;:10000,&quot;progress&quot;:{&quot;auto_review&quot;:{&quot;can_execute&quot;:true,&quot;completion&quot;:{&quot;count&quot;:0,&quot;is_completed&quot;:false,&quot;percentage&quot;:0.0},&quot;inability_to_execute_reason&quot;:null},&quot;tasks&quot;:[{&quot;id&quot;:21447,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:5,&quot;score&quot;:0}},{&quot;id&quot;:21448,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:7,&quot;score&quot;:0}},{&quot;id&quot;:21449,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:4,&quot;score&quot;:0}},{&quot;id&quot;:21450,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:4,&quot;score&quot;:0}},{&quot;id&quot;:21451,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:7,&quot;score&quot;:0}}],&quot;summary&quot;:{&quot;completion&quot;:0.0,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null}},&quot;can_skip&quot;:true,&quot;can_start_peer_review&quot;:false},&quot;peerReview&quot;:null,&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:2343,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/006_color-21d9dd12a952c0dcfa9471902c922dde2a053f71943f7645391458f701eeec29.png&quot;,&quot;name&quot;:&quot;Python - Async&quot;,&quot;score&quot;:{&quot;mandatory&quot;:0.0,&quot;optional&quot;:0.0},&quot;tasksCount&quot;:0},&quot;skipURI&quot;:&quot;/corrections/1131031/skip&quot;,&quot;taskLevelReviewTypeHumanized&quot;:&quot;Your score will be updated as you progress.&quot;}" data-react-cache-id="projects/ProjectReview-0"></div>


    <div class="panel panel-default task-card " id="task-18584">
      <span id="user_id" data-id="2303"></span>
      <div class="panel-heading panel-heading-actions">
        <h3 class="panel-title">
          Tasks list
        </h3>
      </div>
      <div class="panel-body task-list">
          <ul class="nav nav-pills nav-justified" role="tablist">
              <li class="active"><a href="#mandatory" role="tab" data-toggle="tab">Mandatory</a></li>
              <li><a href="#advanced" role="tab" data-toggle="tab">Advanced</a></li>
          </ul>
          <div class="tab-content mt-4">
            <div role="tabpanel" class="tab-pane active" id="mandatory">
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="0" id="heading-0">
                    <div class="task-title-list">0. <code>The basics of async</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='21447'></strong>
                  </div>
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="1" id="heading-1">
                    <div class="task-title-list">1. <code>Let&#39;s execute multiple coroutines at the same time with async</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='21448'></strong>
                  </div>
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="2" id="heading-2">
                    <div class="task-title-list">2. <code>Measure the runtime</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='21449'></strong>
                  </div>
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="3" id="heading-3">
                    <div class="task-title-list">3. <code>Tasks</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='21450'></strong>
                  </div>
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="4" id="heading-4">
                    <div class="task-title-list">4. <code>Tasks</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='21451'></strong>
                  </div>
            </div>
            <div role="tabpanel" class="tab-pane" id="advanced">
            </div>
          </div>
      </div>
    </div>
  </div>


<script src="/assets/javascripts/application/custom/project_tasks.js"></script>


        <div class="modal fade" id="container-specs-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandbox</h4></div><div class="modal-body"><div data-react-class="user_containers/ContainerSpecs" data-react-props="{&quot;containerModelName&quot;:&quot;Sandbox&quot;,&quot;containerSpecs&quot;:[{&quot;description&quot;:&quot;\u003cp\u003eUbuntu 18.04 with Python 3.7\u003c/p\u003e\n&quot;,&quot;id&quot;:23,&quot;name&quot;:&quot;Ubuntu 18.04 - Python 3.7&quot;,&quot;online&quot;:true}],&quot;containersLimit&quot;:3,&quot;csrfToken&quot;:&quot;HhLfY1OYtfoBHX4NNEoLfZLzJA5ZPTO4531U0_bfqKpnLlIlpw0Z9mif5inbGs5kvdvoUDqXjSkDf1Q8h7qNqA&quot;,&quot;startStatusURI&quot;:&quot;/user_containers/start_status.json&quot;,&quot;startURI&quot;:&quot;/user_containers/start.json&quot;}" data-react-cache-id="user_containers/ContainerSpecs-0"></div></div></div></div></div>

        <div class="modal fade" id="sandboxes-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandboxes</h4></div><div class="modal-body"><div data-react-class="user_sandboxes/Sandboxes" data-react-props="{&quot;images&quot;:[{&quot;id&quot;:16,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;US East (N. Virginia)\t&quot;},{&quot;id&quot;:17,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;South America (São Paulo)&quot;},{&quot;id&quot;:14,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;Europe (Paris)&quot;},{&quot;id&quot;:18,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;Asia Pacific (Sydney)&quot;}],&quot;sandboxesUri&quot;:&quot;/user_sandboxes&quot;,&quot;csrfToken&quot;:&quot;I30OseDJXXPoTvMT-BghiNJBMtYE-g-W6gIqa48rURJaQYP3FFzxf4HMazcXSOSR_Wn-iGdQsQcOACqE_k50EA&quot;,&quot;maxNumberOfContainers&quot;:2}" data-react-cache-id="user_sandboxes/Sandboxes-0"></div></div></div></div></div>
</div>

<script src="/assets/javascripts/applications/custom/project.js"></script>
      </article>
    </main>
      <div class="modal fade" id="search-modal" tabindex="-1" role="dialog" aria-labelledby="search-modal-label">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <div id="search-bar-container">
    <input id="search-bar"
            type="text"
            name="hbtn-search-bar"
            placeholder="✨Start search by typing in this field✨">
</div>

            </div>
            <div class="modal-body">
                <div id="modal-spinner" class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div id="search-results-container">
</div>

            </div>
        </div>
    </div>
</div>

