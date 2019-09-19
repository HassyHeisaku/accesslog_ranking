#!/usr/local/bin/ruby

require 'cgi'
require 'pp'

cgi = CGI.new
result = "remote_addr: #{cgi.remote_addr}, referer: #{cgi.referer}, path_info: #{cgi.path_info}, #{cgi.params.to_s}, env.request_uri: #{ENV['REQUEST_URI']} env: #{ENV.keys}"
cgi.out({"type" => "text/html", "charset" => "utf-8"}){result}

