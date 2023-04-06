import About from "@/app/components/navbar/navitems/About";
import Code from "@/app/components/navbar/navitems/Code";
import Home from "@/app/components/navbar/navitems/Home";
import Portfolio from "@/app/components/navbar/navitems/Portfolio";

function NavItems() {
  return (
    <div>
      <ul className="navitem">
        <li>
          <Home />
        </li>
        <li>
          <About />
        </li>
        <li>
          <Code />
        </li>
        <li>
          <Portfolio />
        </li>
      </ul>
    </div>
  );
}

export default NavItems;
