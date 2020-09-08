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
  <array>
  #{skans.map { |v| entry(*v) }.join}
  </array>
EOF

File.write('ad-network-ids.plist', content)
