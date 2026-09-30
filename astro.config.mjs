import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
export default defineConfig({
  site: process.env.SITE_URL || "https://racehorse.hiluco.net",
  integrations: [mdx(), sitemap()],
  build: { inlineStylesheets: "always" },
  output: "static",
  trailingSlash: "always",
});
