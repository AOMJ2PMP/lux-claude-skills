---
name: gartner-review-generator
description: Generate sample answers for Gartner Peer Insights customer review questionnaires for Tencent Cloud products. Use when the user needs to create review samples for Gartner Peer Insights documentation.
---

# Gartner Review Generator

This skill generates high-quality sample answers for Gartner Peer Insights customer review questionnaires, specifically for Tencent Cloud products.

## Purpose

As part of Tencent Cloud's Analyst Relations (AR) team workflow, this skill automates the creation of sample answers for the four main short-answer questions in Gartner Peer Insights reviews:

1. Please provide comments on your overall experience
2. What do you like most about the product or service?
3. What do you dislike most about the product or service?
4. Create a headline summary of your review

## Input Requirements

When the user requests review samples, gather the following information:

1. **Product Name**: The specific Tencent Cloud product (e.g., "TDSQL", "ADP智能体开发平台")
2. **Product URL or Description**: Link to product page or detailed feature description
3. **Target Questions**: Which of the 4 questions need samples (default: all 4)

## Output Format

For each question, provide **ONE sample answer** in the following format:

### [Question Number]. [Question Text]

**[Engaging Subtitle in English]**

[English answer paragraph - 3-5 sentences, natural and specific]

**[同样吸引人的中文小标题]**

[中文回答段落 - 3-5句话，自然且具体]

---

### Formatting Rules

1. **No language indicators**: Never use "English:", "中文:", or similar labels
2. **Subtitle style**: 
   - Question 1: Descriptive phrase (e.g., "Seamless Migration with Enterprise-Grade Reliability")
   - Question 2: Feature-focused label with colon (e.g., "Online Elastic Scaling:")
   - Question 3: Issue-focused label with colon (e.g., "Distributed Query Optimization:")
   - Question 4: No subtitle, just the headline
3. **Length**:
   - Question 1: 3-5 sentences (80-120 words)
   - Question 2: 1-2 sentences (30-50 words)
   - Question 3: 1-2 sentences (30-50 words)
   - Question 4: One concise headline (8-12 words)
4. **Always provide English first, then Chinese**

## Content Guidelines

### Question 1: Overall Experience

- **Subtitle**: Use an engaging descriptive phrase
- **Content**: 
  - Mention specific product capabilities with real-world impact
  - Include concrete metrics or time savings when possible
  - Reference migration experience or integration smoothness
  - Highlight reliability and support responsiveness
- **Avoid**: Generic praise, financial transaction scenarios, overly technical jargon
- **Tone**: Professional, appreciative, specific

### Question 2: What You Like Most

- **Subtitle**: Feature name or capability followed by colon
- **Content**: 
  - Focus on ONE specific feature or capability
  - Explain the practical benefit clearly
  - Include a concrete outcome or metric if possible
- **Avoid**: Multiple features, vague statements
- **Tone**: Enthusiastic but professional

### Question 3: What You Dislike Most

- **Subtitle**: Issue area followed by colon
- **Content**: 
  - Identify a constructive improvement area
  - Frame as "would be better if..." rather than harsh criticism
  - Focus on documentation, learning curve, or minor UX improvements
- **Avoid**: Fundamental product flaws, pricing complaints (unless very mild)
- **Tone**: Constructive, reasonable, still positive overall

### Question 4: Headline Summary

- **No subtitle**
- **Content**: 
  - Create a catchy, benefit-focused headline
  - 8-12 words in English, similar length in Chinese
  - Highlight key differentiators or value propositions
- **Pattern**: [Key benefit] + [product characteristic/architecture]
- **Examples**: 
  - "Elastic distributed database with zero-downtime scaling and MySQL compatibility"
  - "Enterprise-grade AI platform enabling rapid multi-agent deployment"

## Workflow

1. **Gather Requirements**: Ask for product name and URL/description if not provided
2. **Research Product**: If URL provided, fetch and analyze product features and benefits
3. **Generate Samples**: Create ONE sample answer per requested question following the format
4. **Present Results**: Display all samples clearly formatted with proper spacing

## Quality Checklist

Before delivering samples, verify:

- ✅ Each answer has appropriate subtitle (except Q4)
- ✅ English text appears before Chinese text
- ✅ No language labels like "English:" or "中文:"
- ✅ Content is specific with concrete details
- ✅ Tone is professional and authentic
- ✅ Length matches guidelines
- ✅ No copy-paste from existing samples
- ✅ Answers reflect actual product capabilities from research

## Example Interaction

**User**: "I need Gartner review samples for TDSQL database, all 4 questions"

**Skill Response**:
1. Fetch product info from provided URL
2. Generate 4 sample answers following exact format
3. Present complete formatted output

## Important Notes

- **Always research the product** if URL is provided to ensure accuracy
- **Avoid sensitive scenarios**: Don't mention financial transactions, healthcare data specifics, or regulated industries unless the product is specifically designed for those
- **Maintain authenticity**: Write as if from a real technical user's perspective
- **Cultural sensitivity**: Ensure both English and Chinese versions convey equivalent meaning and professionalism
