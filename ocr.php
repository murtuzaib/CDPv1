<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" type="text/css" href="css/index.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<script src="loadingOverlay.js"></script>
	<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	<title>890 Banking Cstomer Onboarding OCR</title>
	<style type="text/css">
		/*progress bar 2*/
		.container {
    		width: 100%;
    		padding-bottom: 30px;
		}
		.proBar {
			counter-reset: step;
		}
		.proBar li {
    		list-style-type: none;
    		padding-left: 8%;
    		margin-bottom: 30px;
    		float: left;
    		width: 9%;
    		position: relative;
    		text-align: center;
		}
		.proBar li:before {
			content: counter(step);
			counter-increment: step;
			width: 40px;
			height:40px;
			line-height: 40px;
			border:4px solid #ddd;
			display: block;
			text-align: center;
			margin: 0 auto 10px auto;
			border-radius: 50%;
			background-color: white;
		}
		.proBar li:after {
			content:'';
			position: absolute;
			width:100%;
			height:4px;
			background-color: #ddd;
			top:30%;
			left:-30%;
			z-index: -1;
		}
		.proBar li:first-child:after {
			content:none;
		}
		.proBar li.active {
			color: #FF4F7C;
		}
		.proBar li.active:before {
			border-color: #FF4F7C;
		}
		.proBar li.active + li:after {
			background-color: #FF4F7C;
		}

		body {
			  margin: 0;
			  font-family: sans-serif;
			  background-color: white;
			}
			/* Three image containers (use 25% for four, and 50% for two, etc) */
			.column {
			  float: left;
			
			  
			  /*border-right-style: groove;*/
			  padding-top: 5%;
			  padding-left: 15%;
			

			}
			#last-column{
				float: left;
				width: 26%;
				padding-left: 12%;
				padding-top: 8%;
				border-right-style: none;
			}
			/* Clear floats after image containers */
			.row::after {
			  content: "";
			  clear: both;
			  display: table;
			}
			.btn {
				border: none
			}
			/*loader css*/
			 .loader {
			 	border: 30px solid #f3f3f3;
				border-radius: 50%;
				border-top: 30px solid #FF4F7C;
			
				border-bottom: 30px solid #FF4F7C;

				width: 150px;
				height: 150px;
				-webkit-animation: spin 2s linear infinite;
				animation: spin 2s linear infinite;
			 }

			@keyframes spin {
			    0% { transform: rotate(0deg); }
			    100% { transform: rotate(360deg); }
			}

			.hide-loader{
			display:none;
			}
	</style>
</head>
<body>
<div class="header">
	<img src="source/890.PNG" width="92%">
	<img src="source/logo.jpg" width="7.5%">
</div>
<div class="container">
	<ul class="proBar">
		<li class="active">Select Document</li>
		<li class="active">Upload Document</li>
		<li>OCR/ICR Outcome</li>
		<li>Process text</li>
		<li>Return Result</li>
	</ul>
</div>

<div class="row">
	<div class="column" style="padding-left: 12%">
		<br>
		<br>
		<br>
		<h1>File selected: </h1>
		<h3 id="duplicater0">
		<?php
		if(!empty($_FILES['files']['name'][0])){
			$files = $_FILES['files'];
			$uploaded = array();
			$failed = array();
			$allowed = array('jpg', 'jpeg', 'png', 'pdf', 'txt');

			foreach ($files['name'] as $position => $file_name) {
				# code...
			
				$file_tmp = $files['tmp_name'][$position];
				$file_size = $files['size'][$position];
				$file_error = $files['error'][$position];

				$file_ext = explode('.', $file_name);
				$file_ext = strtolower(end($file_ext));
				

				if(in_array($file_ext, $allowed)){
					if($file_error === 0){
						if($file_size <= 10000000){
							$file_name_new = uniqid('', true).'.'.$file_ext;
							$file_destination = 'uploads/'.$file_name_new;
					
							if(move_uploaded_file($file_tmp, $file_destination)){
								$uploaded[$position] = $file_destination;
								echo $files['name'][$position], '<br>';
							} else {
								$failed[$position] = "[{$file_name}] failed to upload.";
							}
						} else {
							$failed[$position] = "[$file_name] is too large.";
						}
					} else {
						$failed[$position] ="[$file_name] errored with code {$file_error}.";
					}

				} else {
					$failed[$position] ="[{$file_name}] file extension '{$file_ext}' is not allowed.";
				}
			}
	}
		?>
		</h3>
	</div>
	<div class="column" id="" style="padding-left: 3%; padding-top:12%">
		<label for="cbutton">
	    	<img src="source/ubutton.png" width="60%" style="width:100%; padding-left: 3%"/>
	    </label>
			<input type="button" id="cbutton" style="display:none;">
			<script type="text/javascript">
				var el = document.getElementById("cbutton");
				el.addEventListener("click", function myFunction(){
					var x = document.getElementById("loader");
					x.style.display = "none";
				});
				
				el.addEventListener("click", function duplicate(){
					var i = 0;
					var original = document.getElementById('duplicater' + i);
				    var clone = original.cloneNode(true); // "deep" clone
				    // clone.id = "duplicetor" + ++i; // there can only be one element with an ID
				    clone.onclick = duplicate; // event handlers are not cloned
				    var place = document.getElementById("after_loader")
				    place.appendChild(clone);
				});
				el.addEventListener("click", function ori(){
					document.getElementById("org").src = "source/BalanceSheet2.jpg";
				});
				
			</script>
			<script type="text/javascript">
				var duplicater0content = document.getElementById('duplicater0').innerHTML;
				localStorage.setItem("duplicater0content", duplicater0content);
			</script>

	</div>
	<div class="column" id="last-column" style="padding-left:3%">
		<div id="loader">
			<div class="loader"></div>
			<h3 id="loading" style="color: #FF4F7C; padding-left: 12%;">Loading...</h3>
		</div>
		<script type="text/javascript">
			setTimeout(function(){
				$('#loader').addClass('hide-loader');
			}, 10000);
			setTimeout(function(){
				$('#loading').addClass('hide-loader');
			}, 100000);
		</script>
		<div id="after_loader" style="padding-top: 10%">
			
		</div>
		<img id="org" src="" width="800">
	</div>
		<script type="text/javascript">
			// save image into localstorage
				var localimage = document.getElementById('org');
				imgData = getBase64Image(localimage);
				localStorage.setItem("localimage", imgData);

				function getBase64Image(img) {
				    var canvas = document.createElement("canvas");
				    canvas.width = img.width;
				    canvas.height = img.height;

				    var ctx = canvas.getContext("2d");
				    ctx.drawImage(img, 0, 0);

				    var dataURL = canvas.toDataURL("image/png");

				    return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
				}
		</script>
</div>
	<div style="text-align: center">
		<!-- <input type="submit" class="dropbtn" onclick="window.location='textProcess.html'" value="submit" name="submit"> -->
		<label for="subBtn">
		    	<img src="source/subutton.png"  style="padding-top: 1%; padding-right: 12%"/>
		    </label>
			<input onclick="window.location='textProcess.html'" type="submit" id="subBtn" style="display: none">
	</div>

</body>
</html>

