# fix wordpress settings by replacing phpp with php
exec { 'fix-wordpress':
  command => '/bin/sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php',
}
