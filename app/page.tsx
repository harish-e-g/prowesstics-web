import Nav from "@/components/Nav";
import Hero from "@/components/Hero";
import { Industries, Commitments, Solutions, Engage, Clients, Results, TechStack } from "@/components/Sections";
import Testimonials from "@/components/Testimonials";
import Contact from "@/components/Contact";
import Footer from "@/components/Footer";
import Lightbox from "@/components/Lightbox";
import { site, products } from "@/content/site";

// Structured data helps Google show the company, products and reviews correctly.
const jsonLd = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": `${site.url}/#org`,
      name: site.legalName,
      alternateName: site.name,
      url: site.url,
      logo: `${site.url}/brand/wordmark.png`,
      email: site.email,
      foundingDate: site.founded,
      description: site.description,
      address: { "@type": "PostalAddress", addressLocality: "Chennai", addressRegion: "Tamil Nadu", addressCountry: "IN" },
    },
    ...products.map((p) => ({
      "@type": "SoftwareApplication",
      name: p.name,
      applicationCategory: "BusinessApplication",
      description: p.body,
      publisher: { "@id": `${site.url}/#org` },
    })),
  ],
};

export default function Home() {
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <Nav />
      <main id="top">
        <Hero />
        <Solutions />
        <Industries />
        <Commitments />
        <Engage />
        <Clients />
        <Results />
        <TechStack />
        <Testimonials />
        <Contact />
      </main>
      <Footer />
      <Lightbox />
    </>
  );
}
