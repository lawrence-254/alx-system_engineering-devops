#find the reason for error 500
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => template('your_module/wp-settings.php.erb'),
  notify  => Exec['fix-wordpress'],
}
exec { 'fix-wordpress':
  command     => '/bin/true',
  refreshonly => true,
}
