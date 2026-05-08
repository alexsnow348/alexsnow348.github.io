---
layout: page
title: About
---

<style>
  .about-header {
    margin-bottom: 2rem;
  }

  .about-header h2 {
    font-size: 1.6rem;
    font-weight: 700;
    color: #111;
    margin: 0 0 0.2rem;
    font-family: "Cormorant Garamond", Georgia, serif;
  }

  .about-header .tagline {
    font-size: 0.85rem;
    color: #CE942F;
    font-weight: 600;
    display: block;
    margin-bottom: 0.75rem;
    font-family: "Inter", sans-serif;
    letter-spacing: 0.3px;
  }

  .about-header p {
    font-size: 0.95rem;
    color: #444;
    line-height: 1.85;
    margin: 0;
  }

  .about-body p {
    font-size: 0.925rem;
    color: #444;
    line-height: 1.85;
    margin-bottom: 1.25rem;
  }

  .section-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #aaa;
    display: block;
    border-top: 1px solid #eee;
    padding-top: 2rem;
    margin: 2.5rem 0 1.25rem;
    font-family: "Inter", sans-serif;
  }

  .expertise-list {
    list-style: none;
    padding: 0;
    margin: 0 0 1.5rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
    gap: 1.5rem;
  }

  .expertise-list li h4 {
    font-size: 0.75rem;
    font-weight: 700;
    color: #111;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin: 0 0 0.5rem;
    font-family: "Inter", sans-serif;
  }

  .expertise-list li ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .expertise-list li ul li {
    font-size: 0.82rem;
    color: #666;
    padding: 0.22rem 0;
    border-bottom: 1px solid #f5f5f5;
  }

  .expertise-list li ul li:last-child { border-bottom: none; }

  /* Timeline */
  .timeline { margin: 0; padding: 0; list-style: none; }

  .timeline li {
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 1rem;
    padding: 1rem 0;
    border-bottom: 1px solid #f5f5f5;
    font-size: 0.875rem;
  }

  .timeline li:last-child { border-bottom: none; }

  .timeline-meta { color: #999; }

  .timeline-year {
    font-size: 0.72rem;
    font-weight: 700;
    color: #CE942F;
    display: block;
    font-family: "Inter", sans-serif;
    margin-bottom: 0.1rem;
  }

  .timeline-company {
    font-size: 0.75rem;
    color: #aaa;
    font-family: "Inter", sans-serif;
  }

  .timeline-content { color: #444; line-height: 1.65; }
  .timeline-content strong { color: #111; display: block; margin-bottom: 0.2rem; }
  .timeline-content p { font-size: 0.82rem; margin: 0.3rem 0 0; color: #666; line-height: 1.65; }

  /* Awards */
  .awards-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .awards-list li {
    font-size: 0.875rem;
    color: #444;
    padding: 0.45rem 0;
    border-bottom: 1px solid #f5f5f5;
    display: flex;
    align-items: baseline;
    gap: 0.5rem;
  }

  .awards-list li:last-child { border-bottom: none; }

  .awards-list li::before {
    content: "—";
    color: #CE942F;
    font-size: 0.75rem;
    flex-shrink: 0;
    font-family: "Inter", sans-serif;
  }

  /* Personal */
  .personal-note {
    background: #faf9f7;
    border-left: 3px solid #CE942F;
    padding: 1.25rem 1.5rem;
    border-radius: 0 8px 8px 0;
    margin: 1.25rem 0;
    font-size: 0.9rem;
    color: #555;
    line-height: 1.8;
    font-style: italic;
  }

  /* Connect */
  .connect-block {
    margin-top: 2.5rem;
    padding-top: 2rem;
    border-top: 1px solid #eee;
  }

  .connect-block p {
    font-size: 0.875rem;
    color: #555;
    line-height: 1.75;
    margin-bottom: 1rem;
  }

  .connect-links {
    display: flex;
    gap: 1.25rem;
    flex-wrap: wrap;
  }

  .connect-links a {
    font-size: 0.875rem;
    font-weight: 600;
    color: #111;
    text-decoration: none;
    border-bottom: 2px solid #CE942F;
    padding-bottom: 1px;
    font-family: "Inter", sans-serif;
  }

  .connect-links a:hover { color: #CE942F; text-decoration: none; }
</style>

<div class="about-header">
  <h2>Alex Snow</h2>
  <span class="tagline">MLOps Architect · AI & LLM Consultant · Based in Germany</span>
  <p>I bring <span id="about-years"></span>+ years of hands-on experience across telecom, fintech, and industrial AI to help SMBs and cultural institutions in Germany apply machine learning and large language models practically — from strategy to production-ready systems.</p>
</div>

<div class="about-body">
  <p>My path into AI consulting is rooted in real engineering work: building ML pipelines at scale, leading backend teams shipping data products used by hundreds of thousands of users, and most recently architecting the MLOps infrastructure powering real-time risk assessment in the automotive sector at ControlExpert GmbH.</p>

  <p>Alongside the technical depth, I hold an M.Sc. in Data Analytics from Stiftung Universität Hildesheim and <span id="about-certs"></span>+ certifications spanning deep learning, NLP, LLMOps, and cloud ML platforms. Staying current in AI is not optional — it's a commitment I take seriously.</p>
</div>

<div class="personal-note">
  As a genuine art history enthusiast, I spend time visiting museums, galleries, and Ausstellungen across Germany and Europe. This isn't a positioning strategy — it's how I spend my weekends. It's also why I understand, from the inside, what cultural institutions need from technology: precision, context, and respect for the material.
</div>

<span class="section-label">Experience</span>

<ul class="timeline">
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2026 – Present</span>
      <span class="timeline-company">ControlExpert GmbH</span>
    </div>
    <div class="timeline-content">
      <strong>MLOps Architect</strong>
      <p>Architecting scalable infrastructure for real-time risk assessment and automated claims processing in the automotive sector. Industrialising AI through rigorous CI/CD practices to keep models compliant, accurate, and high-performing.</p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2023 – 2026</span>
      <span class="timeline-company">LPKF Laser & Electronics SE · Garbsen</span>
    </div>
    <div class="timeline-content">
      <strong>MLOps Engineer</strong>
      <p>Implemented the full MLOps lifecycle — model development to deployment and monitoring — in support of the ML team. Built a Svelte-based Image Explorer dashboard with detailed analytics capabilities.</p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2021 – 2023</span>
      <span class="timeline-company">TM Research & Development · Malaysia</span>
    </div>
    <div class="timeline-content">
      <strong>Lead Back End Engineer</strong>
      <p>Led the backend team on MINDS — an AI-driven network diagnostics platform that reduced Technical Helpdesk complaint handling time from 27 hours to 9 hours for Telekom Malaysia. Developed data pre-processing engines and backend API microservices across multiple data sources.</p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2018 – 2021</span>
      <span class="timeline-company">TM Research & Development · Malaysia</span>
    </div>
    <div class="timeline-content">
      <strong>Back End & FinTech Engineer</strong>
      <p>Built the PrimeKeeper Digital Wallet backend including KYC flow and PCI DSS-compliant key management. Previously developed the Enterprise Energy Management System (EENT) — winner of MSC Malaysia Asia Pacific ICT Alliance 2020 Data Innovation Award.</p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2017 – 2018</span>
      <span class="timeline-company">TM Research & Development · Malaysia</span>
    </div>
    <div class="timeline-content">
      <strong>Machine Learning Engineer</strong>
      <p>Developed the Analytics of Customer Experience (ACE) platform — a computer vision system for people counting, emotion, gender, and age detection deployed across 150+ Telekom Malaysia stores nationwide. Won MSC Malaysia Asia Pacific ICT Alliance 2019 Award.</p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2019 – Present</span>
      <span class="timeline-company"><a href="https://www.alexsnowschool.org/" target="_blank">Alex Snow School</a> · Myanmar</span>
    </div>
    <div class="timeline-content">
      <strong>Founder & Educator</strong>
      <p>Founded an award-winning educational initiative for Myanmar youth focused on AI/ML and financial literacy. <a href="https://www.freiheit.org/yangon/falling-walls-lab-myanmar-2020" target="_blank">Winner of Falling Walls Lab Myanmar 2020</a>. Peer-learning programs bridging technical education and real-world application.</p>
    </div>
  </li>
</ul>

<span class="section-label">Education</span>

<ul class="timeline">
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2023 – 2025</span>
      <span class="timeline-company">Stiftung Universität Hildesheim</span>
    </div>
    <div class="timeline-content">
      <strong>M.Sc. Data Analytics, Computer Science</strong>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2014 – 2017</span>
      <span class="timeline-company">Multimedia University</span>
    </div>
    <div class="timeline-content">
      <strong>Bachelor's degree, Computer Science</strong>
    </div>
  </li>
</ul>

<span class="section-label">What I Work With</span>

<ul class="expertise-list">
  <li>
    <h4>LLMs & Frameworks</h4>
    <ul>
      <li>OpenAI GPT-4 / GPT-4o</li>
      <li>Anthropic Claude</li>
      <li>Open-source LLMs</li>
      <li>LangChain / LangGraph</li>
      <li>LlamaIndex</li>
    </ul>
  </li>
  <li>
    <h4>ML & Data Platforms</h4>
    <ul>
      <li>Databricks (MLOps certified)</li>
      <li>Google Cloud ML</li>
      <li>Azure ML</li>
      <li>MLflow · TensorFlow</li>
      <li>Python · Docker · Kubernetes</li>
    </ul>
  </li>
  <li>
    <h4>Use Cases</h4>
    <ul>
      <li>Document intelligence & RAG</li>
      <li>AI agents & automation</li>
      <li>Computer vision</li>
      <li>Collection cataloguing</li>
      <li>Real-time ML pipelines</li>
    </ul>
  </li>
  <li>
    <h4>Industries</h4>
    <ul>
      <li>Art, Museums & Archives</li>
      <li>Automotive & Industrial</li>
      <li>Telecom & FinTech</li>
      <li>Education technology</li>
    </ul>
  </li>
</ul>

<span class="section-label">Honours & Awards</span>

<ul class="awards-list">
  <li><a href="https://www.freiheit.org/yangon/falling-walls-lab-myanmar-2020" target="_blank">Winner, Falling Walls Lab Myanmar 2020</a></li>
  <li><a href="https://drive.google.com/file/d/1E7oaWmE9dL6iKVsMDkV77UqsnjFA_fUY/view?usp=sharing" target="_blank">Gold Medal — Startup Category, RICES MMU 2020</a></li>
  <li>Group Digital Council Award — Best Project</li>
  <li>MSC Malaysia Asia Pacific ICT Alliance 2020 — Data Innovation Award (EENT)</li>
  <li>MSC Malaysia Asia Pacific ICT Alliance 2019 — Digital Marketing Award (ACE)</li>
  <li>Top Albukhary Scholar · Faculty Dean's List · Permata Dunia Awards</li>
</ul>

<span class="section-label">Languages</span>

<ul class="awards-list">
  <li>English — Professional working proficiency</li>
  <li>German — Elementary (advancing)</li>
  <li>Burmese — Native</li>
</ul>

<span class="section-label">Talks & Presentations</span>

<ul class="timeline">
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2025</span>
      <span class="timeline-company">American Center, Yangon</span>
    </div>
    <div class="timeline-content">
      <strong>AI Unplugged: The Art of Prompt Engineering</strong>
      <p>Fundamentals of prompt engineering and the impact of AI on society, delivered to youth audiences.</p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2025</span>
      <span class="timeline-company">Alex Snow School</span>
    </div>
    <div class="timeline-content">
      <strong>AI Tools for Work</strong>
      <p>AI evolution, how models work behind the scenes, and practical AI tools for professional use.</p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2024</span>
      <span class="timeline-company">Alex Snow School</span>
    </div>
    <div class="timeline-content">
      <strong>Knowledge Distillation: Streamlining AI · Becoming an AI Engineer · Life-long Learning</strong>
      <p>Series of technical and career-oriented talks for Myanmar's next generation of engineers.</p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2022</span>
      <span class="timeline-company">Friedrich Naumann Foundation</span>
    </div>
    <div class="timeline-content">
      <strong>Talking about Women in STEM</strong>
      <p>STEM career opportunities and advice, organised by Friedrich Naumann Foundation Yangon.</p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2020</span>
      <span class="timeline-company">Phandeeyer Institute · Alex Snow School</span>
    </div>
    <div class="timeline-content">
      <strong>Age of ML & AI — Preparing for Jobs · How Data Impacts Our Life</strong>
      <p>Career orientation talks on ML/AI roles, skill requirements, and data literacy.</p>
    </div>
  </li>
</ul>

<p style="font-size:0.82rem; color:#aaa; margin-top:0.5rem;">
  <a href="/talks/index.html" style="color:#CE942F; font-weight:600; border-bottom: 1px solid #CE942F; text-decoration:none;">View all talks with videos & slides →</a>
</p>

<span class="section-label">Key Certifications</span>

<ul class="timeline">
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2026</span>
      <span class="timeline-company">Databricks</span>
    </div>
    <div class="timeline-content">
      <strong><a href="https://credentials.databricks.com/c6d55b78-da17-4b40-abde-8c3bba6a3370#acc.cT1BIwqy" target="_blank">Advanced MLOps on Databricks</a></strong>
      <p>Also: <a href="https://credentials.databricks.com/914128bf-9a82-47ff-a6a2-aeda7d12ac49#acc.IQMwaO6t" target="_blank">ML at Scale</a> · <a href="https://credentials.databricks.com/a74f010a-d22f-4f3b-ac29-0d1f465d2fa6#acc.pqBUIady" target="_blank">ML Model Deployment</a></p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2026</span>
      <span class="timeline-company">Coursera</span>
    </div>
    <div class="timeline-content">
      <strong><a href="https://www.coursera.org/account/accomplishments/specialization/certificate/QVI7I522LVCV" target="_blank">Modern and Contemporary Art and Design Specialization</a></strong>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2024</span>
      <span class="timeline-company">Coursera</span>
    </div>
    <div class="timeline-content">
      <strong><a href="https://www.coursera.org/account/accomplishments/specialization/certificate/LS3E2X5NKHNA" target="_blank">LLMOps Specialization</a></strong>
      <p>Also: <a href="https://www.coursera.org/account/accomplishments/certificate/2O8410PNY38V" target="_blank">Operationalizing LLMs on Azure</a> · <a href="https://www.coursera.org/account/accomplishments/certificate/IUKVAFP9B9I4" target="_blank">GenAI & LLMs on AWS</a> · <a href="https://www.coursera.org/account/accomplishments/certificate/KARJYVPJ3VK8" target="_blank">Databricks to Local LLMs</a></p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2023</span>
      <span class="timeline-company">Udacity</span>
    </div>
    <div class="timeline-content">
      <strong><a href="https://www.udacity.com/certificate/e/8c0fc744-cca1-11ed-9c17-cbdede8b15de" target="_blank">DevOps Foundation Nanodegree</a></strong>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2021</span>
      <span class="timeline-company">Coursera</span>
    </div>
    <div class="timeline-content">
      <strong><a href="https://www.coursera.org/account/accomplishments/specialization/certificate/QA3SAR3KF7QR" target="_blank">Natural Language Processing Specialization</a></strong>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2020</span>
      <span class="timeline-company">Coursera</span>
    </div>
    <div class="timeline-content">
      <strong><a href="https://www.coursera.org/account/accomplishments/certificate/WNKV79G9HH3K" target="_blank">Deep Learning Specialization</a></strong>
      <p>Also: <a href="https://www.coursera.org/account/accomplishments/specialization/certificate/HVL3VQBL8QEY" target="_blank">Machine Learning on Google Cloud</a></p>
    </div>
  </li>
  <li>
    <div class="timeline-meta">
      <span class="timeline-year">2018</span>
      <span class="timeline-company">Udacity</span>
    </div>
    <div class="timeline-content">
      <strong><a href="https://graduation.udacity.com/confirm/EMYNXV6R" target="_blank">Computer Vision Nanodegree</a></strong>
      <p>Also: <a href="https://graduation.udacity.com/confirm/DTGNJGEG" target="_blank">Full Stack Web Developer Nanodegree</a></p>
    </div>
  </li>
</ul>

<script>
  document.getElementById('about-years').textContent = new Date().getFullYear() - 2017;
  document.getElementById('about-certs').textContent = 81;
</script>

<div class="connect-block">
  <p>Available for consulting engagements, workshops, and advisory roles across the DACH region. The best first step is a short discovery conversation.</p>
  <div class="connect-links">
    <a href="https://www.linkedin.com/in/wuthmonehninhlaing/" target="_blank">LinkedIn</a>
    <a href="https://github.com/alexsnowschool" target="_blank">GitHub</a>
    <a href="mailto:alexsnow348@gmail.com">Email</a>
    <a href="/own-certifications/">Certifications</a>
  </div>
</div>
