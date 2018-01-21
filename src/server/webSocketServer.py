#import sys
#sys.path.insert(0,'../packages/websocket_server/')


from websocket_server import WebsocketServer
import json

class WebServer(WebsocketServer):
	"""docstring for WebServer"""
	def __init__(self, port):
		if port is None:
			print("Port is None, Returning None")
			return None
		self.port_number = port	
		self.listen_func = None
		#super(WebsocketServer, self).__init__(self,self.port_number)
		super().__init__(port)
		
		self.set_fn_new_client(self.new_client)
		self.set_fn_client_left(self.client_left)
		self.set_fn_message_received(self.message_received)
	
	def new_client(self,client, server):
		pass
		#print("New client connected and was given id %d" % client['id'])
		#server.send_message_to_all("Hey all, a new client has joined us")


	def client_left(self,client, server):
		""" Called for every client disconnecting"""
		pass
		#print("Client(%d) disconnected" % client['id'])


	def message_received(self,client, server, message):
		""" Called when a client sends a message"""
		#Don't Need this, keeping commented for future reference
		#if len(message) > 200:
		#	message = message[:200]
		url_obj=json.loads(message)
		#print(url_obj['url'])
		print(url_obj)
		if self.listen_func:
			self.listen_func(url_obj)
			return
			
		with open('link','a+') as file:
			file.write(url_obj['url']+'\n')
			file.close()
			

	def run(self):
		self.run_forever()

	def addListener(self,func):
		self.listen_func = func

if __name__ == '__main__':
	server = WebServer(9999)
	server.run()	

#server = WebsocketServer(PORT)
#server.set_fn_new_client(new_client)
#server.set_fn_client_left(client_left)
#server.run_forever()
