# System-level car-following model calibration
Simulate the traffic at corridor in SUMO and analysis the average vehicle travel time and fuel consumption.
### Data attributes for trajectory
<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" width="538" style="width:403.75pt;border-collapse:collapse;border:none">
 <tbody><tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Attribute</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Unit</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Description</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">id</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">-</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Id of vehicles</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">time</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">-</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Time in the format of YYYYMMDDHHMM.S.</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">x_pix</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">pixel</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The horizontal pixel coordinate of
  vehicle</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">y_pix</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">pixel</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The vertical pixel coordinate of vehicle</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">w_pix</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">pixel</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The width of an object in pixels.</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">h_pix</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">pixel</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The height of an object in pixels.</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">edge</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">-</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The position of edge or intersection.</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">lane</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">-</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The position of lane at given edge, If
  vehicle is in intersection, the lane is 0.</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">x_utm</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">m</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The UTM x-coordinate of vehicle</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">y_utm</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">m</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The UTM y-coordinate of vehicle</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">t_sec</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">sec</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The record time in seconds</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">v</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US" style="font-size:10.5pt;font-family:等线"><img width="25" height="21" src="Data%20attributes%20for%20trajectory_files/image001.png"></span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Speed of the vehicle</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">a</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US" style="font-size:10.5pt;font-family:等线"><img width="33" height="21" src="Data%20attributes%20for%20trajectory_files/image002.png"></span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Acceleration of the vehicle</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">pre_id</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">-</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Vehicle id of previous vehicle</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">pre_v</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US" style="font-size:10.5pt;font-family:等线"><img width="25" height="21" src="Data%20attributes%20for%20trajectory_files/image001.png"></span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Speed of previous vehicle</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">delta_d</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">m</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Distance between the outer contours of
  subject vehicle and the preceding vehicle </span></p>
  </td>
 </tr>
</tbody></table>

### Data attributes for vehicle information
<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" width="538" style="width:403.75pt;border-collapse:collapse;border:none">
 <tbody><tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><b><span lang="EN-US" style="font-size:8.0pt;font-family:
  &quot;NimbusRomNo9L-Medi&quot;,serif;color:black">Attribute</span></b></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><b><span lang="EN-US" style="font-size:8.0pt;font-family:
  &quot;NimbusRomNo9L-Medi&quot;,serif;color:black">Unit</span></b></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><b><span lang="EN-US" style="font-size:8.0pt;font-family:
  &quot;NimbusRomNo9L-Medi&quot;,serif;color:black">Description</span></b></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">id</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">-</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Id of vehicles</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">length</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">m</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Vehicle length</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span class="spelle"><span lang="EN-US">start_time</span></span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">s</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The time when vehicle enters the corridor</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span class="spelle"><span lang="EN-US">trip_time</span></span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">s</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The travel time when vehicle drives in
  the corridor</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span class="spelle"><span lang="EN-US">edge_start</span></span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">-</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The edge when vehicle enters the corridor</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span class="spelle"><span lang="EN-US">edge_end</span></span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">-</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The edge </span><span lang="EN-US">when vehicle
  enters the corridor</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">turn_I1</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">-</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The turning information of vehicle at
  intersection 1 (node1)</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">turn_I2</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">-</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The turning information of vehicle at
  intersection 2 (node2)</span></p>
  </td>
 </tr>
 <tr>
  <td width="85" valign="top" style="width:63.55pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">turn_I3</span></p>
  </td>
  <td width="66" valign="top" style="width:49.6pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">&nbsp;</span></p>
  </td>
  <td width="387" valign="top" style="width:290.6pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">The turning information of vehicle at
  intersection 3 (node3)</span></p>
  </td>
 </tr>
</tbody></table>