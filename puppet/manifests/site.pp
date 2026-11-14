# site.pp — Puppet Manifest
# Project: Automated Cloud Infrastructure Provisioning and Configuration Management
# Author : Kushagra (Roll No. 63) | INT333 – DevOps Advance Configuration Management
# Description: Installs and configures Apache Web Server on Ubuntu

node default {

  # 1. Install the apache2 package
  package { 'apache2':
    ensure => installed,
  }

  # 2. Ensure the apache2 service is running and starts on boot
  service { 'apache2':
    ensure  => running,
    enable  => true,
    require => Package['apache2'],
  }

  # 3. Deploy a custom HTML page (idempotent — only changes if content differs)
  file { '/var/www/html/index.html':
    ensure  => file,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0644',
    content => "<html>
  <head>
    <title>Puppet Managed Server</title>
    <style>
      body { font-family: Arial, sans-serif; text-align: center; margin-top: 80px; background: #f4f4f4; }
      h1   { color: #2c3e50; }
      .box { background: white; display: inline-block; padding: 40px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
      .badge { background: #e74c3c; color: white; padding: 4px 10px; border-radius: 4px; font-size: 0.85em; }
    </style>
  </head>
  <body>
    <div class=\"box\">
      <h1>&#9989; Automated Web Server - Configured by Puppet</h1>
      <p>This server was <strong>provisioned</strong> by <span class=\"badge\">Terraform</span> and
         <strong>configured</strong> by <span class=\"badge\" style=\"background:#3498db\">Puppet</span>.</p>
      <hr/>
      <p><strong>Project:</strong> INT333 &ndash; DevOps Advance Configuration Management</p>
      <p><strong>Author:</strong> Kushagra &nbsp;|&nbsp; Roll No. 63</p>
      <p><strong>Institution:</strong> Lovely Professional University</p>
    </div>
  </body>
</html>
",
    require => Package['apache2'],
    notify  => Service['apache2'],
  }

}

