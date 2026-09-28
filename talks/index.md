---
layout: page
title: Talks
---

<style>
  .talks-intro {
    font-size: 1.05rem;
    line-height: 1.85;
    margin-bottom: 2.5rem;
    max-width: 560px;
    font-style: italic;
    opacity: .85;
  }

  .talk-year-label {
    font-family: "Alegreya SC", Georgia, serif;
    font-weight: 700;
    text-transform: lowercase;
    font-size: 1.05rem;
    letter-spacing: .02rem;
    margin: 2.5rem 0 0.75rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid var(--border);
    display: block;
  }

  .talk-item {
    padding: 1.25rem 0;
    border-bottom: 1px solid var(--border);
  }

  .talk-item:last-child { border-bottom: none; }

  .talk-video {
    position: relative;
    padding-bottom: 56.25%;
    height: 0;
    margin-bottom: 0.85rem;
    border-radius: 4px;
    overflow: hidden;
    background: var(--link-hover-bg);
  }

  .talk-video iframe {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    border: none;
  }

  .talk-item h3.talk-title {
    font-family: inherit;
    text-transform: none;
    letter-spacing: normal;
    font-size: 1.05rem;
    font-weight: 700;
    margin: 0 0 0.25rem;
    line-height: 1.35;
  }

  .talk-meta {
    font-size: 0.8rem;
    opacity: .6;
    margin-bottom: 0.5rem;
  }

  .talk-desc {
    font-size: 0.95rem;
    opacity: .85;
    line-height: 1.75;
    margin: 0 0 0.65rem;
  }

  .talk-links {
    display: flex;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .talk-link {
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--text);
    text-decoration: none;
    border-bottom: 1px solid var(--border);
    padding-bottom: 1px;
  }

  .talk-link:hover {
    background: var(--link-hover-bg);
  }

  .talk-lang {
    font-size: 0.7rem;
    font-weight: 600;
    padding: 0.15rem 0.5rem;
    border-radius: 3px;
    text-transform: lowercase;
    letter-spacing: 0.3px;
    color: var(--text);
    background: var(--link-hover-bg);
    border: 1px solid var(--border);
  }

  /* Posters section */
  .posters-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 0.75rem;
    margin-top: 0.75rem;
  }

  .poster-img {
    width: 100%;
    aspect-ratio: 4/3;
    object-fit: cover;
    border-radius: 4px;
    display: block;
    border: 1px solid var(--border);
  }

  @media (max-width: 600px) {
    .posters-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>

<p class="talks-intro">
  Public talks on AI, machine learning, and career development mostly in Burmese for Myanmar's tech community, with occasional English sessions.
</p>

<span class="talk-year-label">2025</span>

<div class="talk-item">
  <div class="talk-video">
    <iframe src="https://www.youtube.com/embed/w6Sth-Josds" title="AI Unplugged" allowfullscreen></iframe>
  </div>
  <h3 class="talk-title">AI Unplugged: The Art of Prompt Engineering</h3>
  <div class="talk-meta">American Center, Yangon</div>
  <p class="talk-desc">Fundamentals of prompt engineering and AI's impact on society — delivered to youth audiences with a focus on workforce readiness.</p>
  <div class="talk-links">
    <span class="talk-lang">Burmese</span>
  </div>
</div>

<div class="talk-item">
  <div class="talk-video">
    <iframe src="https://www.youtube.com/embed/Fhe63hJNpfE" title="AI Tools for Work" allowfullscreen></iframe>
  </div>
  <h3 class="talk-title">AI Tools for Work</h3>
  <div class="talk-meta">Alex Snow School</div>
  <p class="talk-desc">How AI works behind the scenes and practical tools for professional use — from AI evolution basics to hands-on application.</p>
  <div class="talk-links">
    <span class="talk-lang">Burmese</span>
    <a href="https://drive.google.com/file/d/1rpXtwOLW8D8Y55AR-qBOZyTc8feBgn_h/view?usp=sharing" target="_blank" class="talk-link">Slides &rarr;</a>
  </div>
</div>

<span class="talk-year-label">2024</span>

<div class="talk-item">
  <h3 class="talk-title">The Use of AI/GenAI in Financial Markets</h3>
  <div class="talk-meta">Alex Snow School</div>
  <p class="talk-desc">LSTMs, GANs, and LLMs like FinGPT for sentiment analysis and risk prediction — with a look at ethical and regulatory challenges.</p>
  <div class="talk-links">
    <span class="talk-lang">Burmese</span>
    <a href="https://drive.google.com/file/d/18GRYC2YsePyo6wLdQlYBuR2bflnDSxob/view?usp=sharing" target="_blank" class="talk-link">Slides &rarr;</a>
  </div>
</div>

<div class="talk-item">
  <div class="talk-video">
    <iframe src="https://www.youtube.com/embed/0LtoRcXcudc" title="Knowledge Distillation" allowfullscreen></iframe>
  </div>
  <h3 class="talk-title">Knowledge Distillation: Streamlining AI</h3>
  <div class="talk-meta">Alex Snow School</div>
  <p class="talk-desc">Teacher-student frameworks for creating smaller, efficient AI models — covering distillation schemes and applications in NLP and object detection.</p>
  <div class="talk-links">
    <span class="talk-lang">Burmese</span>
    <a href="https://drive.google.com/file/d/1qoMhFWrcDK3jjOuWnv2863XeJwIs1bJ5/view?usp=drive_link" target="_blank" class="talk-link">Slides &rarr;</a>
  </div>
</div>

<div class="talk-item">
  <div class="talk-video">
    <iframe src="https://www.youtube.com/embed/r1CkNRj6IUI" title="Becoming a Life-long Learner" allowfullscreen></iframe>
  </div>
  <h3 class="talk-title">Becoming a Life-long Learner and Reader</h3>
  <div class="talk-meta">Alex Snow School</div>
  <p class="talk-desc">A philosophy of continuous growth drawing from Richard Hamming — with a structured framework for learning in public.</p>
  <div class="talk-links">
    <span class="talk-lang">Burmese</span>
    <a href="https://drive.google.com/file/d/1vMYo4bSP2HRdlYonGH1FPGVgFIZBlxKP/view?usp=drive_link" target="_blank" class="talk-link">Slides &rarr;</a>
  </div>
</div>

<div class="talk-item">
  <div class="talk-video">
    <iframe src="https://www.youtube.com/embed/JyQ-G134Fz4" title="AI in Daily Life" allowfullscreen></iframe>
  </div>
  <h3 class="talk-title">The Usages of AI in Daily Life</h3>
  <div class="talk-meta">Alex Snow School</div>
  <p class="talk-desc">AI's role in social media, entertainment, education, and healthcare — with practical tips for leveraging it effectively.</p>
  <div class="talk-links">
    <span class="talk-lang">Burmese</span>
    <a href="https://drive.google.com/file/d/1PQG7MvaSdHmIN4ElyBNbpmPIMAhZx2Qk/view?usp=sharing" target="_blank" class="talk-link">Slides &rarr;</a>
  </div>
</div>

<div class="talk-item">
  <div class="talk-video">
    <iframe src="https://www.youtube.com/embed/nFkNfiUXZNg" title="Becoming an AI Engineer" allowfullscreen></iframe>
  </div>
  <h3 class="talk-title">Becoming an AI Engineer</h3>
  <div class="talk-meta">Alex Snow School</div>
  <p class="talk-desc">A practical roadmap for aspiring AI engineers — foundational skills, LLMOps, deployment, and learning resources.</p>
  <div class="talk-links">
    <span class="talk-lang">Burmese</span>
    <a href="https://drive.google.com/file/d/1lWQ5S4v1owEAjWH-3GgzBVIRfUQtdl_4/view?usp=drive_link" target="_blank" class="talk-link">Slides &rarr;</a>
  </div>
</div>

<span class="talk-year-label">2022</span>

<div class="talk-item">
  <h3 class="talk-title">Talking about Women in STEM</h3>
  <div class="talk-meta">Friedrich Naumann Foundation &middot; Yangon</div>
  <p class="talk-desc">Career advice and opportunities in STEM fields, organised by Friedrich Naumann Foundation Yangon.</p>
  <div class="talk-links">
    <span class="talk-lang">Burmese</span>
    <a href="https://soundcloud.com/fnf-mm/episode-11-talking-about-women-in-stem" target="_blank" class="talk-link">Listen on SoundCloud &rarr;</a>
  </div>
</div>

<div class="talk-item">
  <h3 class="talk-title">Training ML Models Using AutoML on GCP</h3>
  <div class="talk-meta">Alex Snow School</div>
  <p class="talk-desc">Introduction to ML pipelines with a hands-on demo predicting loan risk using Google Cloud Vertex AI AutoML.</p>
  <div class="talk-links">
    <span class="talk-lang">Burmese</span>
    <a href="https://drive.google.com/file/d/1mLHQW-5RX5GZexJkwipNVjD4zZ-0VuKi/view?usp=sharing" target="_blank" class="talk-link">Slides &rarr;</a>
  </div>
</div>

<span class="talk-year-label">2021</span>

<div class="talk-item">
  <h3 class="talk-title">Why Study Computer Science?</h3>
  <div class="talk-meta">Albukhary International University &middot; Malaysia</div>
  <p class="talk-desc">Career orientation for CS students — future prospects, job landscape, and what to expect from a CS career.</p>
  <div class="talk-links">
    <span class="talk-lang">English</span>
    <a href="https://drive.google.com/file/d/1dIExMOXvcdwiDlgeXONoLbC93xj0_Asu/view?usp=sharing" target="_blank" class="talk-link">Slides &rarr;</a>
  </div>
</div>

<span class="talk-year-label">2020</span>

<div class="talk-item">
  <h3 class="talk-title">How Data Impacts Our Life</h3>
  <div class="talk-meta">Phandeeyer Institute &middot; Myanmar</div>
  <p class="talk-desc">Data literacy talk for pre-university students at the Phandeeyer Institute Learning Festival.</p>
  <div class="talk-links">
    <span class="talk-lang">Burmese</span>
    <a href="https://drive.google.com/file/d/12u8Z84XNzc4HEBxGWuK4BqYmDjoz38Q_/view?usp=sharing" target="_blank" class="talk-link">Slides &rarr;</a>
  </div>
</div>

<div class="talk-item">
  <div class="talk-video">
    <iframe src="https://www.youtube.com/embed/RUMMgeiEkVk" title="Age of ML & AI" allowfullscreen></iframe>
  </div>
  <h3 class="talk-title">Age of ML &amp; AI — Preparing for Jobs</h3>
  <div class="talk-meta">Alex Snow School</div>
  <p class="talk-desc">ML and AI roles, employment opportunities, required skills, and preparation strategies for the next generation of engineers.</p>
  <div class="talk-links">
    <span class="talk-lang">Burmese</span>
    <a href="https://drive.google.com/file/d/1dXRG6f4BaWc4n4a0XmbRJCUkuACVlQHg/view?usp=sharing" target="_blank" class="talk-link">Slides &rarr;</a>
  </div>
</div>

<span class="talk-year-label">Posters</span>

<div class="posters-grid">
  <img src="/public/img/ai_unplugged_talk.jpg" alt="AI Unplugged talk poster" class="poster-img" loading="lazy">
  <img src="/public/img/ai-tools-for-work.jpg" alt="AI Tools for Work poster" class="poster-img" loading="lazy">
  <img src="/public/img/fin-ai-talk.jpg" alt="Finance AI talk poster" class="poster-img" loading="lazy">
  <img src="/public/img/kd.jpg" alt="Knowledge Distillation poster" class="poster-img" loading="lazy">
  <img src="/public/img/sa-mat.jpg" alt="Talk poster" class="poster-img" loading="lazy">
  <img src="/public/img/woman-in-stem.jpg" alt="Women in STEM poster" class="poster-img" loading="lazy">
  <img src="/public/img/life-long-learner.webp" alt="Life-long learner poster" class="poster-img" loading="lazy">
  <img src="/public/img/brain.jpg" alt="Talk poster" class="poster-img" loading="lazy">
</div>
