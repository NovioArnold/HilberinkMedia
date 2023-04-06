import "./globals.css";
import Header from "@/app/components/header";

export const metadata = {
  title: "Hilberink Media",
  description: "Hilberink Media the 42 WAY",
  keywords:
    "html, css, javascript, typescript, react, nextjs, nodejs, express, python",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="container">
        <Header />
        {children}
      </body>
    </html>
  );
}
