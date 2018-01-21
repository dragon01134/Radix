//Make it compatible to run on different browser 
window.browser = (function () {
  return window.msBrowser ||
    window.browser ||
    window.chrome;
})();

browser.contextMenus.create({
    id: "download_link",
    title: "Download this link video",
    contexts: ["link"],
});

browser.contextMenus.onClicked.addListener((info, tab) => {
		 if (info.menuItemId === "download_link") {
  		 	console.log("URL is "+info.linkUrl);
	   	 	sendlink(info.linkUrl);
   		}
});

browser.browserAction.onClicked.addListener((tab) => {
   console.log("URL is "+tab.url);
   sendlink(tab.url);
});

function sendlink(link) 
{
	var entry={};
	entry.url = link;
	entry.type = 'Normal';
	console.log(entry);
	WebSocketSend(entry)
}

function WebSocketSend(entry)
{
	port=9999
	server="ws://localhost:"
	if ("WebSocket" in window)
    	{
               
               // Let us open a web socket
               var ws = new WebSocket(server+port);
				
               ws.onopen = function()
               {
                  // Web Socket is connected, send data using send()
                  ws.send(JSON.stringify(entry));
               //   alert("Message is sent...");
                  ws.close();
               };
				
               ws.onmessage = function (evt) 
               { 
                  var received_msg = evt.data;
                  //alert("Message is received...");
               };
				
               ws.onclose = function()
               { 
                  // websocket is closed.
                  //alert("Connection is closed..."); 
               };
         }
            
        else
        {
               // The browser doesn't support WebSocket
               alert("WebSocket NOT supported by your Browser!");
        }
}
