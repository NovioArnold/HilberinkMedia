import nextLogo from "../../public/next.svg";
export default function Footer() {
  return (
    <div>
      <div className="p-5 m-5 flex flex-row align-bottom justify-between">
        <h1 className="p-5 text-3xl font-bold ">powered by:</h1>
        <div className="flex flex-row">
          <img src={nextLogo} alt="nextjs" className="h-16 w-16" />
          <img src="/tailwindcss.svg" alt="tailwindcss" className="h-16 w-16" />
        </div>
      </div>
    </div>
  );
}
