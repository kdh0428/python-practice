#!/usr/bin/python

print "Content-Type: text/html"
print

print """\
<!DOCTYPE HTML>
<html>
  <head><title>PythonCGI_Chat_Room</title>
  <script>
      var xmlhttp;
    

    window.onload = function(){ //load this javascript when page load
      Chat_history();
      }

    
    function loadXMLDoc(){
      if(window.XMLHttpRequest){ // IE>6 or Chrome Safari FireFox
        xmlhttp = new XMLHttpRequest();
      }
      else{ //IE<=6
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
      }
    }
    
    
    function Chat_history(){
      loadXMLDoc();

      xmlhttp.open("GET","Chat_history.cgi",true);

      xmlhttp.onreadystatechange = function(){
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
         document.getElementById("Chat_history").innerHTML = xmlhttp.responseText;

          var Chat_Scroll = document.getElementById("Chat_history"); 
         Chat_Scroll.scrollTop = Chat_Scroll.scrollHeight; //textarea's ScrollDown to the End          
          }
      }
      xmlhttp.send();
      
      setTimeout(Chat_history,1000); // Load Chat_history in every 1 second
      return false;

    }
    
    
    function Empty_Check(Nickname,Chat){
      if( !Nickname || !Chat){
        alert("Don't Empty Anything");
        return false;
      }
      return true;
    }
    
    
    function Send(Nickname,Chat){
      if(!Empty_Check(Nickname,Chat));

      else{
        loadXMLDoc();
               xmlhttp.onreadystatechange = function(){
//          if(xmlhttp.readyState ==  4 && xmlhttp.status == 200){
//           Chat_history();
//      }
        }
         xmlhttp.open("POST","Chat.cgi",true);
         xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
         xmlhttp.send(Nickname+" "+Chat);
      }
    }


  </script>
  </head>
  
  
  <body>
    <textarea id="Chat_history" cols=50 rows=20 disabled></textarea>
    <form action="">
      Nickname : <input type="text" id="Nickname" maxlength="15" />  <textarea id="Chat" maxlength="250"></textarea> <button type="button" onclick="Send(Nickname.value,Chat.value)">Send</button>
    </form>
  </body>
</html>
"""

