import "./globals.css";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

export const metadata = {
  title: "GPT Vlog",
  description: "Next gen vlog",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="mt-6">
        <Navbar />
        {children}
        <Footer />
      </body>
    </html>
  );
}
