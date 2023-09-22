#  a manifest that kills a process named killmenow
exec { 'kill_killmenow_process':
  command     => 'pkill -9 killmenow',
  path    => ['/usr/bin', '/usr/sbin'],
  returns => '',
}
