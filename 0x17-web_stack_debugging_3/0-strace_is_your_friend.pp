 # Fix Apache 500 error using strace
 
 exec { 'fix-wordpress':
   command => '/usr/sbin/service apache2 restart',
   path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
   onlyif  => 'curl -sI 127.0.0.1:80 | grep "HTTP/1.0 500"',
 }
