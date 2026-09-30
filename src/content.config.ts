import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { articleSchema, referenceSchema } from "./lib/evidence";
export const collections = {
  articles: defineCollection({
    loader: glob({ pattern: "**/*.mdx", base: "./src/content/articles" }),
    schema: articleSchema,
  }),
  evidence: defineCollection({
    loader: glob({ pattern: "**/*.json", base: "./src/content/evidence" }),
    schema: referenceSchema,
  }),
};
