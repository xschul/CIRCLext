function pycirclean() {
	var content = document.getElementById("content");
	var text = content.contentDocument.activeElement.innerText;
	
	var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", "http://localhost:5000/sanitize/", false ); // false for synchronous request
    xmlHttp.send(text);
    var response = xmlHttp.responseText;
    if(response.includes("dangerous"))
    	window.alert("dangerous")
    else
    	window.alert("safe")
}