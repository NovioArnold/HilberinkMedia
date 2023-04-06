const Slug = (props: any) => {
  const slug = props.params.slug;
  return (
    <div>
      <p>
        <h1>Post with the name of {slug}</h1>
      </p>
    </div>
  );
};

export default Slug;
