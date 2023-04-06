import Logo from "./Logo";
import Title from "./Title";
import NavItems from "./NavItems";

const Navbar = () => {
  return (
    <nav className="navbar">
      <Logo />
      <Title />
      <NavItems />
    </nav>
  );
};

export default Navbar;
