#Trying to increse the number of requests taken

  exec { 'Trying_to_increase_requests':
    command => '/bin/sed -i "s/15/4096" /etc/nginx/default/nginx'.
    path    => 'usr/local/bin/:/bin/'
}

  exec {'Restart_ngunx':
    command => '/etc/init.d/nginx restart',
    path    => '/etc/init.d',
}
