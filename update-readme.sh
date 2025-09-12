#!/bin/bash
# Update README.md with current project statistics

echo "🔄 Updating README.md statistics..."

# Count tools and resources
TOOLS=$(grep -c "@mcp.tool()" mcp_demo/*.py | awk -F: '{sum += $2} END {print sum}')
RESOURCES=$(grep -c "@mcp.resource" mcp_demo/*.py | awk -F: '{sum += $2} END {print sum}')

echo "📊 Found $TOOLS tools and $RESOURCES resources"

# Update README
python3 << EOF
import re

# Read README.
with open('README.md', 'r') as f:
    content = f.read()

# Update statistics.
content = re.sub(
    r'\*\*Mathematical operations\*\*: \d+ tools',
    f'**Mathematical operations**: $TOOLS tools',
    content
)

content = re.sub(
    r'\*\*Dynamic resources\*\*: \d+ resources',
    f'**Dynamic resources**: $RESOURCES resources',
    content
)

# Write back
with open('README.md', 'w') as f:
    f.write(content)

print("✅ README.md updated successfully")
EOF
