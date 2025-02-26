---
title: Academic Open Source Workshop at CHAOSSCon Europe 2025
image: "TBC.png"
date: 2025-02-26
Description: Report from Academic Open Source Workshop, CHAOSScon, Feb 2025
---

## 1. Introduction

[CHAOSScon Europe 2025](https://chaoss.community/chaosscon-2025-eu), co-located with [FOSDEM](https://fosdem.org/2025), took place in Brussels, Belgium, on January 30, 2025. As part of the conference, a dedicated discussion on Academic Open Source was held, sponsored by [CURIOSS](https://curioss.org). The workshop brought together researchers, software developers, and open source advocates to discuss the challenges and opportunities of sustaining open source software in academia. With 12 participants in attendance, the discussions were divided into two sessions. The first session focused on understanding different types of research software, their sustainability, and institutional support. The second session expanded on these topics, addressing funding uncertainties, emergency open sourcing, and legal considerations related to intellectual property. 

This report presents the key themes from both sessions, followed by a summary of challenges, proposed solutions, and actionable next steps. The goal is to provide a comprehensive understanding of the current state of academic open source and to outline a path forward for researchers and institutions looking to support open source practices more effectively. 

## 2. Key Themes at a Glance

The diagram below provides a high-level visual summary of the key themes explored in both sessions of the workshop. While the following sections provide an in-depth discussion of each theme, this overview serves as a quick reference to the key focus areas that shaped the conversation.

<p align="center">
  <img src="/images/news/25-02-26-CHAOSScon-diagram.png" />
</p>
*Figure 1: Key Themes in Academic Open Source*

### 3.1 Framing the Discussion: Projects vs. People 

Participants debated whether the focus of academic open source discussions should be on the software projects themselves or the people behind them. Some argued that understanding software development in academia requires a project-based approach, recognizing the different lifecycles and purposes of research software. Others emphasized the role of individual contributors, particularly the challenges they face in career advancement and funding. 

An important insight was that research software is not solely produced within universities; national labs, private companies, and collaborative research initiatives also play significant roles. This highlighted the need for cross-institutional collaboration and better mechanisms for tracking contributions.

### 3.2 Types of Research Software and Open Source Outputs

Research software was categorized into three main types, reflecting different levels of long-term sustainability and openness:

+ **Open Research Outputs:** Software released primarily for research reproducibility, often made publicly available at the end of a project without long-term maintenance plans. Many researchers follow this approach because they prioritize publishing research over maintaining software.
+ **Iterative Research Software:** Continuously developed with multiple versions released, often within an active research context. However, researchers may or may not be interested in fostering a community around the software, which affects its adoption and sustainability.
+ **Sustained Research Software:** Designed for long-term use, requiring governance structures, ongoing funding, and community involvement. These projects align more closely with open source best practices but demand significant institutional and financial support.

The discussion highlighted that while many projects start as open research outputs, transitioning them into sustained research software requires early planning, dedicated funding, and institutional commitment. Participants also noted that software sustainability is not just about making code available—it requires clear governance, documentation, and an engaged user base to ensure long-term viability.

### 3.3 Measuring Success and Ensuring Sustainability

Participants discussed various ways to define success in academic open source projects. While some emphasized citations and research impact as key indicators, others argued that these do not fully capture a project's value. Alternative measures, such as software adoption, secured funding, and project visibility, were suggested to reflect long-term sustainability and community engagement. 

A major challenge identified was the lack of infrastructure for tracking software usage and real-world impact. Without standardized systems, researchers rely on anecdotal evidence, making it difficult to demonstrate their software’s value to funding agencies. Tracking adoption requires significant manual effort, and without institutional support, many projects struggle to maintain visibility. 

Insights from other fields, such as the life sciences, showed that success can be driven by targeted community engagement and strategic promotion of best practices. Participants highlighted the importance of actively promoting software, documenting its impact, and engaging with users to enhance sustainability and recognition.

### 3.4 Collaboration Across Institutions and Disciplines

The discussion explored the challenges of collaboration in academic open source, particularly the issue of unintended forking, where similar projects emerge independently due to a lack of communication or awareness. Participants noted that many researchers work on open source projects without institutional oversight, sometimes intentionally avoiding affiliation due to bureaucratic concerns. This lack of visibility makes it difficult to identify overlapping efforts, leading to redundancy and inefficiencies.

While forking was generally seen as a challenge, some participants highlighted that it can also be an opportunity for innovation. In one case, a research software project split into two separate forks due to disagreements over direction. Over time, some members reconnected, demonstrating that divergence does not always lead to permanent fragmentation. Productive forks can allow teams to explore different approaches while still benefiting from shared knowledge.
To improve collaboration and reduce unnecessary duplication, participants emphasized the need for better documentation, academic software registries, and structured coordination efforts. Decision-making frameworks were suggested as a way to help research teams navigate potential conflicts before forking occurs. 

### 3.5 Funding and Institutional Support

Securing long-term funding for academic open source projects remains a major challenge. While some funding agencies now require research outputs to be open source, there is often no clear guidance on sustaining these projects beyond initial grants. Many researchers struggle to find continued support, resulting in valuable software being abandoned after funding expires. 

Although FAIR (Findable, Accessible, Interoperable, Reusable) principles are widely promoted, participants expressed concern that these principles are often misunderstood or implemented superficially. Some researchers admitted to copying FAIR compliance statements from past proposals without fully integrating them into their projects. Without proper enforcement or education on best practices, FAIR risks becoming a "tick-box" requirement rather than a meaningful framework for ensuring software sustainability. 

Additionally, participants noted that well-maintained open source software can be a powerful tool for attracting young researchers to fields like high-energy physics. Ensuring that research software is properly documented and openly available helps create a more welcoming environment for new contributors, fostering long-term engagement in open science. 

### 3.6 Bridging Open Source and Research Communities

Attendees discussed the significant gap between traditional academic practices and open source best practices. Many researchers commit to open sourcing their work in grant proposals but do not fully understand what it means. This often results in research outputs that lack key open source elements such as community engagement, governance structures, and long-term sustainability planning.

A major barrier is the reluctance of researchers to embrace open development practices. Unlike in the broader open source community, where projects are typically open from the start, many academics prefer to work privately until publication. Concerns include intellectual property risks, lack of institutional support, and fears that early openness could slow research productivity.

To bridge this gap, participants emphasized the need for institutional recognition of open source contributions. Open source work should be valued in tenure and promotion decisions, and researchers should receive training on best practices for integrating open source into academic workflows. A cultural shift is necessary to move beyond simply making code available toward genuine, long-term open source engagement.

## 4 Key Themes from the Second Session

In this session, participants built upon the discussions from the first session by focusing on the practical challenges of sustaining open source research software, particularly in the context of funding uncertainties, intellectual property (IP) concerns, and institutional policies. The conversation highlighted how researchers often face difficulties in securing long-term financial support, navigating institutional ownership restrictions, and determining the best strategies for making research software openly available. 

This session provided valuable insights into the real-world obstacles researchers encounter when maintaining open source projects, as well as potential solutions for improving institutional support and funding structures. Participants also examined how different academic disciplines and funding bodies approach open source requirements, emphasizing the need for clearer policies and long-term sustainability strategies.

### 4.1 Funding Uncertainties and Emergency Open Sourcing

The second session expanded on the funding challenges discussed earlier, emphasizing the unpredictability of research funding, particularly in the U.S. Some researchers shared experiences of having their funding suddenly discontinued, forcing them to abandon projects or even leave the country. This raised concerns about how to transfer research software across institutions without violating ownership policies.

To mitigate these risks, participants proposed an "in case of emergency" open source plan, encouraging researchers to prepare their software for public release early rather than waiting until the end of a project. This strategy would ensure that critical research tools remain accessible even if funding is lost. However, some participants questioned whether standard open source workflows are too slow for emergency scenarios, suggesting that a streamlined process might be necessary to make software publicly available more quickly.

Legal and institutional barriers were also discussed. Some researchers debated whether simply making the source code available without a license would be sufficient in an emergency, while others warned that this could lead to legal risks and ownership disputes. A potential solution was to involve external collaborators early, as projects with multiple institutional contributors are harder for a single institution to claim full ownership over, potentially allowing continued development even after funding is lost.

### 4.2 Intellectual Property (IP) Concerns and Institutional Barriers

Discussions around intellectual property revealed significant institutional barriers to open sourcing research software. Where universities claim IP ownership of software developed by their researchers, it can make it difficult for developers to share their work openly. In some cases, researchers even avoid associating their work with their institutions, keeping their GitHub profiles unlinked to prevent their contributions from being tracked or claimed.

It was noted that where participants involved external collaborators early in the project lifecycle, it counteracts any one institution to assert sole IP ownership. Additionally, researchers were encouraged to adopt an open source license at the start of development to establish usage rights to avoid any friction with institutions later in the research cycle.

Legal complexities were also discussed, particularly the risks of publishing software without an explicit license. Some warned that failing to include a license could lead universities to re-license or restrict access even after a researcher has left the institution. Participants emphasized the importance of clear licensing strategies and proactive planning to ensure that research software remains accessible and free from unexpected IP claims or uncertainty.

### 4.3 Fear of Being Scooped vs. Benefits of Open Collaboration

A major concern among researchers is the fear that making software open will allow competitors to use their tools to publish findings faster, potentially harming their own research output. Some participants noted that researchers often do not fully understand copyright and intellectual property laws, and only realize their limitations in restricting software use when it is too late.

However, participants also highlighted that scooping is far less common than researchers assume. In practice, most researchers tend to collaborate rather than compete when they discover similar work. Instead of avoiding open source due to fear, researchers were encouraged to engage with the broader open source community, as increased visibility can lead to valuable collaborations rather than competition.

Another key factor was the timing of open source releases. Some researchers delay making their software public because they want to refine documentation and clean up the code first, but this often results in indefinite delays. Participants suggested that researchers should integrate open source practices into their workflows early, ensuring that their software remains in a shareable state throughout its development rather than waiting until the last minute.

## 5. Summary of Challenges, Proposed Solutions, and Next Steps

The workshop discussions identified several key challenges impacting academic open source, particularly in the areas of funding uncertainty, institutional policies, and intellectual property (IP) rights. Participants highlighted difficulties in maintaining long-term sustainability, navigating complex legal frameworks, and aligning research incentives with open source principles. Alongside these challenges, the discussions also produced actionable solutions and recommendations to better support researchers in open-sourcing their work more effectively.

This section summarizes the core challenges, the proposed strategies to address them, and the next steps required to foster sustainable open source practices in academia.

### 5.1 Summary of Challenges

One of the main challenges discussed was legal complexities and IP ownership issues. Researchers often struggle to navigate licensing and IP rights, especially when universities claim ownership of their software, even after they leave the institution. Some researchers intentionally avoid linking their open source work to their institutions to prevent ownership conflicts, fearing bureaucratic restrictions or future legal disputes.

Another significant challenge is institutional barriers to open source engagement. Many universities lack clear policies for recognizing and supporting open source contributions, making it difficult for researchers to justify their work in academic evaluations. In some cases, PhD students and early-career researchers are unaware that their work may be owned by their university, even after graduation. This lack of institutional clarity discourages researchers from investing in long-term open source projects.

Funding uncertainty and sustainability challenges pose additional risks to academic open source projects. Research funding is often short-term, and many projects face abandonment when funding runs out. Even when funding agencies mandate open source, they do not always provide resources for long-term maintenance, leaving researchers without the necessary financial support to sustain their software.

The fear of being scooped and competitive research pressures also impact open source adoption. Some researchers worry that making their software openly available will allow competitors to publish faster, reducing their ability to claim credit for their work. This fear leads many researchers to delay open-sourcing their work until after publication, which in turn limits the potential for early collaboration and community engagement.

Lastly, the lack of emergency strategies for open source release presents a major obstacle. When funding is suddenly cut, researchers often do not have a clear plan for ensuring their software remains accessible. Currently, there is no standardized "Emergency Open Source" framework to help researchers release software quickly while ensuring legal and institutional compliance. The absence of such a framework makes it challenging to preserve research software under unpredictable funding conditions.

### 5.2 Proposed Solutions

One key solution is increasing legal awareness and promoting licensing best practices. Training programs and resources on IP rights and licensing should be developed to help researchers clarify IP ownership with respect to their institution. Additionally, researchers should be encouraged to apply open source licenses at the start of development rather than waiting until later, which can prevent ownership disputes from arising.

Institutional policy reforms are also necessary to promote open source engagement. Universities should develop clearer policies for recognizing open source contributions as part of academic career progression. Furthermore, PhD students and early-career researchers should receive guidance on their rights regarding research software ownership to ensure they understand how their work can be used and shared.

To improve sustainability, funding agencies should offer dedicated financial support for software maintenance, not just initial development. Multi-institutional collaborations can also help ensure that software development is not dependent on a single funding source. By diversifying funding avenues and institutional partnerships, research software can have a longer lifespan and broader impact.

Encouraging open collaboration without fear of being scooped is another priority. Participants emphasized the need to shift the narrative around competition in academia. Many researchers hesitate to share their work due to concerns about being scooped, yet real-world examples suggest that early collaboration often leads to stronger research outcomes. Awareness campaigns should be conducted to highlight cases where open source engagement has benefited researchers rather than harmed their competitive edge.

Lastly, there is a need to develop an "Emergency Open Source" framework. This would provide researchers with a structured approach to releasing software quickly in cases where funding is lost unexpectedly. Encouraging external collaborations early in the project lifecycle could also make it harder for any single institution to claim full ownership, protecting research software from institutional restrictions.

### 5.3 Next Steps

Advocacy efforts should be initiated to encourage universities to adopt open source-friendly policies and clarify IP rights for researchers. By working with institutional decision-makers, researchers can push for more transparent guidelines on software ownership and licensing.

Providing researchers with better legal guidance and tools is also essential. Many researchers lack access to legal expertise when navigating open source licensing, which can create uncertainty and hesitation in sharing their work. Institutions and funding bodies should provide legal support structures to help researchers make informed decisions.

To ensure recognition of open source contributions, universities should establish institutional tracking mechanisms that acknowledge and support academic open source projects without infringing on researcher autonomy. This would allow open source work to be considered in tenure and funding evaluations.

Engagement with funding agencies is another critical step. Funders should be involved in discussions to ensure that open source mandates are paired with sustainable funding models. Currently, many agencies require open source publication but fail to provide the necessary long-term support, leading to software abandonment.

Further discussions and workshops should be held to refine the "Emergency Open Source" framework. This framework would provide a standardized process for quickly making research software available when funding is unexpectedly cut.

Lastly, a follow-up session or working group should be organized to explore additional strategies for helping researchers navigate institutional and funding challenges in open source projects. These discussions will help create concrete action plans for supporting sustainable academic open source initiatives.

## 6. Conclusion

The Academic Open Source Workshop at CHAOSScon provided a platform for researchers, software developers, and open source advocates to discuss the key challenges and opportunities in sustaining research software. The discussions highlighted pressing issues such as funding instability, intellectual property barriers, institutional policies, and sustainability concerns. While these challenges create significant obstacles, participants also identified practical solutions, including clearer licensing strategies, institutional reforms, and better funding mechanisms to ensure long-term software maintenance and accessibility.

A major takeaway from the workshop was the need for proactive engagement with institutions and funding bodies to align policies with the realities of academic open source development. Researchers must be supported not only in releasing their software but also in maintaining it beyond the initial funding cycle. The discussions also underscored the importance of fostering a collaborative, rather than competitive, approach to open source research, enabling knowledge-sharing and long-term project viability.

Moving forward, continued dialogue, advocacy, and structured initiatives—such as institutional policy changes, sustainable funding strategies, and the development of an Emergency Open Source framework—will be essential in creating an environment where academic open source can thrive. This workshop laid the foundation for future efforts to drive meaningful change in how research software is developed, shared, and sustained.

## Acknowledgements

We extend our deepest appreciation to all participants of the Academic Open Source Workshop at [CHAOSScon Europe 2025](https://chaoss.community/chaosscon-2025-eu) for their valuable insights and contributions. Their engagement played a crucial role in shaping the discussions on the sustainability of open source research software.

We also recognize and appreciate the valuable contributions of all the participants, whose engagement enriched the discussions and helped shape the outcomes of this workshop. Special thanks go to Regina Nkenchor who authored this report. 

Finally, we express our gratitude to [CURIOSS](https://curioss.org) for sponsoring the workshop and to CHAOSS for providing the platform to host these important discussions. Their support has been instrumental in fostering collaboration and driving forward the conversation on open source sustainability in academia.

<p align="center">
  <img src="/images/news/25-02-26-CHAOSScon-group-photo.png" />
</p>
*Figure 2: Group photo of the workshop participants at CHAOSScon Europe 2025*
