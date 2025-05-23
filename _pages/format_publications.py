import re

def format_publications(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    formatted = []
    in_frontmatter = False
    frontmatter_done = False

    for line in lines:
        raw_line = line
        line = line.strip()

        # Handle YAML frontmatter block
        if line == "---":
            if not in_frontmatter:
                in_frontmatter = True
                formatted.append(line)
                continue
            elif in_frontmatter and not frontmatter_done:
                frontmatter_done = True
                formatted.append(line + "\n")  # end of YAML
                continue

        # If still in frontmatter, keep lines as-is
        if in_frontmatter and not frontmatter_done:
            formatted.append(line)
            continue

        # Skip empty lines
        if not line:
            continue

        # Preserve '### 1990–1999' as is, but change ### to ###
        if line.startswith("### "):
            formatted.append("\n### " + line[4:].strip() + "\n")
            continue

        # Treat standalone 4-digit year as heading
        if re.fullmatch(r"\d{4}", line):
            formatted.append(f"\n### {line}\n")
            continue

        # Fix malformed markdown links (double-wrapped)
        line = re.sub(
            r"\[\[([^\]]+)\]\(([^\)]+)\)\]",
            r"[\1](\2)",
            line
        )

        # Fix links like [https://doi.org/...](https://doi.org/...) → [doi](https://...)
        line = re.sub(
            r"\[(https?://[^\]]+)\]\((https?://[^\)]+)\)",
            lambda m: f"[{m.group(2).split('/')[-1]}]({m.group(2)})" if m.group(1) == m.group(2) else m.group(0),
            line
        )

        # Convert bare URLs (not already inside []()) into markdown links
        def convert_url(match):
            url = match.group(0)
            if f"]({url})" in line:
                return url  # already linked
            return f"[{url.split('/')[-1]}]({url})"

        line = re.sub(r"https?://[^\s\)]+", convert_url, line)

        # Remove existing bullet if present
        line = re.sub(r"^[-*]\s+", "", line)

        # Add cleaned line
        formatted.append(f"{line}\n")

    # Write to file
    with open(output_file, "w") as f:
        f.write("\n".join(formatted))

    print(f"✅ Cleaned and correctly formatted output written to: {output_file}")


# Example usage
if __name__ == "__main__":
    input_path = "all-publications.md"
    output_path = "formatted_publications.md"
    format_publications(input_path, output_path)
