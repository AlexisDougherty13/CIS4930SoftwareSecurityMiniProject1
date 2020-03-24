<!DOCTYPE html>
<html lang="en">
    <head>
        <title>A Better Dashboard</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" href="../static/stylesDash.css" media="screen">
		<link href="https://fonts.googleapis.com/css?family=Righteous&display=swap" rel="stylesheet"> 
        <!--[if lt IE 9]>
        <script src="http://html5shim.googlecode.com/svn/trunk/html5.js">
        </script>
        <![endif]-->
        <!--[if lt IE 9]>
        <script src="http://css3-mediaqueries-js.googlecode.com/svn/trunk/css3-mediaqueries.js">
        </script>
        <![endif]-->
    </head>
    <body>
        <header role="banner"> 
			<center>
			<img src="../static/cityscape_logo.png" alt="Cityscape" width="30%" height="30%">
			</center>
        </header>
        <nav role="navigation">

        </nav>
        <div class="wrapper">
        <main role="main">
		<br>
			<center>


        <!--<p>
          //<?php
	//require 'functions.php';
          
	//$str1="Hello world!<script>alert(1);</script>";

	//echo escape($str1);
	//?>
	</p>-->
			<h2>Search for a City</h2>
			<form action="{{ url_for('handle_dataB') }}" method="post"> 
			  <input type="text" id="city" name="projectFilepath" value="City Name"><br> 
			  <br>
			  <input type=submit value="Submit">
			</form>
			<br>

			<table>
			<tr>
				<th>City</th>
				<th>State</th> 
				<th>Population</th>
			</tr>
			{% for i in stash %}
			<tr>
				<th>{{ i.name }}</th>
				<th>{{ i.state }}</th> 
				<th>{{ i.population }}</th>
			</tr>
			{% endfor %}
			</table>
			<br>
			<br>
			
			<h2>Enter City Data</h2>
			<form action="{{ url_for('handle_data2B') }}" method="post" onSubmit="doStuff()"> 
			  <input type="text" id="city2" name="{{projectFilepathC | e}}" value="City Name"><br><br>
			  <input type="text" id="state2" name="projectFilepathS" value="State Name"><br><br>
			  <input type="text" id="pop2" name="projectFilepathP" value="Population"><br><br>
			  <br>
			  <input type=submit value="Submit">
			</form>
			<p id="demo"></p>
			<br>
			<br>
			
			<h2>City 1's List of Buildings</h2>
			<form action="{{ url_for('handle_data3') }}" method="post"> 
			<select name ="DropDown" id="cars">
			  <option type="hidden" value="A">Building A</option>
			  <option type="hidden" value="B">Building B</option>
			  <option type="hidden" value="C">Building C</option>
			  <option type="hidden" value="D">Building D</option>
			  <option type="hidden" value="E">Building E</option>
			</select>
			<br> 
			<br>
			<input type=submit value="Submit">
			</form>
			<br>
			<th>{{ message }}</th>
			<br>
			<br>
			<form action="{{ url_for('handle_data4') }}" method="post" > 
				<button type=submit name="adminbutton" value="ZFhObGNnPT0=">View Important Information</button>
			</form>
			
			<br>
			<th>{{ message2 }}</th>
			</center>
        </main>
        <footer role="contentinfo">
        </footer>
        </div>
    </body>
	
	 <script src="http://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
	
	<script>
		function doStuff()
		{
			var cityName = document.getElementById("city2").value;
			
			document.getElementById("demo").innerHTML = "You entered " + cityName + ".";
			
		}
	</script>
</html>
