import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="mt-6 flex fex-row justify-between  ">
      <h1 className="text-3xl">hello</h1>
      <ul className="flex justify-between navbar-item no-decoration shadow-md  ">
        <li>
          <Link
            className=" p-4 border rounded-md border-solid  border-black"
            href="#"
          >
            Home
          </Link>
        </li>
        <li>
          <Link
            href="/about"
            className=" p-4 border rounded-md border-solid border-black"
          >
            about
          </Link>
        </li>
        <li>
          <Link
            href="/contact"
            className="p-4 border rounded-md border-solid border-black"
          >
            contact
          </Link>
        </li>
        <li>
          <Link
            href="/register"
            className="p-4 border rounded-md border-solid border-black"
          >
            register
          </Link>
        </li>
        <li>
          <Link
            href="/login"
            className="p-4 border rounded-md border-solid border-black"
          >
            login
          </Link>
        </li>
      </ul>
    </nav>
  );
}
