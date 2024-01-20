# create a manifest that kills a process named killmenow
exec { 'kill_killmenow':
  command => 'pkill killmenow',
  path    => '/alx-system_engineering-devops/0x0A-configuration_management/2-execute_a_command'
}
