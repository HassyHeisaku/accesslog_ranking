require 'webrick'

server = WEBrick::HTTPServer.new({ 
	:DocumentRoot => './',
	:BindAddress => '127.0.0.1',
  :CGIInterpreter => 'ruby path'
	:Port => 1313
})
server.start
