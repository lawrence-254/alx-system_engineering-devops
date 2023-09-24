#!/usr/bin/env bash
# can connect to a server without typing a password.

file_line { 'set_ssh_private_key':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}

file_line { 'disable_password_authentication':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}
