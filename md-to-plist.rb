#!/usr/bin/env ruby
# frozen_string_literal: true

# a small helper to generate the plist from Markdown

skans = []
File.foreach('README.md') do |line|
  next unless line.start_with?('|[')

  values = line.split('|')
  skans << [values[1][/\[(.*)\]/, 1], values[2]]
end

def entry(name, id)
  <<-EOF
    <dict>
        <!--- #{name} --->
        <key>SKAdNetworkIdentifier</key>
        <string>#{id}.skadnetwork</string>
    </dict>
  EOF
end

content = <<~EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>SKAdNetworkItems</key>
    <array>
#{skans.map { |v| entry(*v) }.join}    </array>
</dict>
</plist>
EOF

File.write('ad-network-ids.plist', content)
