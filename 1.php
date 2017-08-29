<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dialogue System</title>
<link href="bootstrap/css/bootstrap.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="1.css" media="screen" />
<link rel="stylesheet" type="text/css" href="2.css" media="screen" />
<script src="jquery.min.js"></script>
<script src="bootstrap/js/bootstrap.js"></script>
</head>
<body>

<ul id="menu-bar">
 <li ><a href="#">Home</a></li>
 <li><a href="#">Help</a>
  <ul>
   <li><a href="test.pdf">Trains List</a></li>
<li><a  class="" data-toggle="modal" data-target="#Queries">
  Query Templates
</a></li>
  </ul>
 </li>
 <li>
<!-- Button trigger modal -->
<a  class="" data-toggle="modal" data-target="#myModal">
  About
</a>
</li>
</i>
<li><a  class="" data-toggle="modal" data-target="#contribute">
  Contribute
</a></li>
<li>
<a  class="" data-toggle="modal" data-target="#contact">
Contact Us</a></li>
</ul>
<div class="row">
<div class="col-md-4"></div>
<div class="col-md-4" style="margin-top:200px;">
<body background="Train.jpg"> 
<form method=post>
<div class="row">
<div class="col-md-10">
<input class="form-control" type="text" name="sentence" size="40"></div>
<div class="col-md-2">
<input type="submit" value="Submit" class="btn btn-info">
</div>
</div>
</form>
</div>
<div class="col-md-4"></div>
</div>

<div class="row">
<div class="col-md-4"></div>
<!-- Modal -->
<div class="modal fade" id="Queries" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title" id="myModalLabel"><b>Templates</b></h4>
      </div>
      <div class="modal-body">
<b><i> Any combinations of the below types work<br /></i></b>
<b>From-To type :</b><br />
When is the next train from lucknow to guwahati?
<br />
<b>Between type :</b><br />
Trains between lucknow to guwahati?
<br />
<b>Time related :</b><br />
 Train from lucknow to guwahati after 15:00?
<br />
Train from lucknow to guwahati before 12:00?
<br />
<b>Via type :</b><br />
What are the trains between lucknow and guwahati via katihar?
<br />
<b>Search on Train Number</b><br />
When does train 12236 arrive at lucknow?
<br />

      </div>
      <div class="modal-footer">
      </div>
    </div>
  </div>
</div>
<div class="modal fade" id="contribute" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title" id="myModalLabel">A Fellow Developer?</h4>
      </div>
      <div class="modal-body">
	Want to Contribute? Then why wait? Pull the code from the repository and start right now!
	
      </div>
      <div class="modal-footer">
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title" id="myModalLabel">Disclaimer</h4>
      </div>
      <div class="modal-body">
	This is a template based query system for railways domain.This was aimed at making the railways query system more interactive.It operates on a limited set of templates that answer a range of queries. This has a built in spell-checker that automatically corrects the words.For more information regarding the usage,Please click the help button.
      </div>
      <div class="modal-footer">
      </div>
    </div>
  </div>
</div>
<div class="modal fade" id="contact" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <div style="text-align:center"><h4 class="modal-title" id="myModalLabel"><b>Feedback</b></h4></div>
      </div>
      <div class="modal-body">
	 <i><a href="mailto:radhika.mamidi@iiit.ac.in?Subject=BTP%20Feedback" target="_top">Radhika Mamidi</a></i><br />
	<i><a href="mailto:chinni.abhishek@students.iiit.ac.in?Subject=BTP%20Feedback" target="_top">Abhishek Chinni</a></i><br />
	<i><a href="mailto:vssantoshkumar.vadrevu@students.iiit.ac.in?Subject=BTP%20Feedback" target="_top">Santosh Kumar V</a></i><br />
	 <i><a href="mailto:lalit.medarametla@students.iiit.ac.in?Subject=BTP%20Feedback" target="_top">Lalit Kumar M</a></i><br />

      </div>
      <div class="modal-footer">

<div style="text-align:center">Copyright &copy; 2014. IIIT Hyderabad. All rights reserved.</div>
</div>
    </div>
  </div>
</div>
<div class="col-md-4">

<body><pre><b></b><br /><br /><script>window.scrollTo(0,99999);</script>
</div>
<div class="col-md-4"></div>

</div>
</body>
</html>
