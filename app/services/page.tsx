import type { Metadata } from "next";
import Nav from "@/components/Nav";
import { Services } from "@/components/Sections";
import Contact from "@/components/Contact";
import Footer from "@/components/Footer";
import Lightbox from "@/components/Lightbox";

export const metadata: Metadata = {
  title: "Services",
  description:
    "Data engineering, business intelligence, cloud migration, AI and analytics, computer vision, factory automation, managed data operations and staff augmentation from one partner.",
  alternates: { canonical: "/services/" },
};

export default function ServicesPage() {
  return (
    <>
      <Nav />
      <main id="top">
        <section className="page-hero">
          <div className="wrap">
            <span className="eyebrow">Services</span>
            <h1>Eight ways we turn your data into decisions</h1>
            <p>From the first pipeline to the decision on the shop floor. Each service runs on its own or as part of one programme, on the platforms you already use.</p>
          </div>
        </section>
        <Services />
        <Contact />
      </main>
      <Footer />
      <Lightbox />
    </>
  );
}
