import fs from "fs";
import path from "path";
import Link from "next/link";

const getPostMetadata = () => {
  const folder = "./content/opdrachten";
  const files = fs.readdirSync(folder);
  const markdownFiles = files.filter((fn) => fn.endsWith(".md"));
  const slugs = files.map((fn) => fn.replace(".md", ""));
  return slugs;
};

const MdToHtml = () => {
  const metaData = getPostMetadata();
  const postReviews = metaData.map((slug) => (
    <div>
      <Link href="/vakken/[slug]" as={`/vakken/${slug}`}>
        <h1>{slug}</h1>
      </Link>
    </div>
  ));
  return <div>{postReviews}</div>;
};

export default MdToHtml;
