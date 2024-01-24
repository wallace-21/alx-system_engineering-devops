# Using Puppet, install flask from pip3

package { 'pip3'
  ensure => 'installed'
}

exec { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
