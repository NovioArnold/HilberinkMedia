import "./globals.css";
import Header from "@/app/components/header";

export const metadata = {
  title: "Hilberink Media",
  description: "Hilberink Media is a web development company",
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
