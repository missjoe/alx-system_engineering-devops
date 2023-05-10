class webserver {
  package { 'apache2':
    ensure => installed,
  }

  file { '/etc/apache2/ports.conf':
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
    content => "Listen 8080\n",
    require => Package['apache2'],
  }

  service { 'apache2':
    ensure  => running,
    enable  => true,
    require => File['/etc/apache2/ports.conf'],
  }
}
