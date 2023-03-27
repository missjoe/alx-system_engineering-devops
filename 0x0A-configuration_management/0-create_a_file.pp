# Creating file in /tmp.


file {'school':
name    => '/tmp/school',
mode    => '0744',
content => 'I love Puppet',
group   => 'www-data',
owner   => 'www-data',
}
