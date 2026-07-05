#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("/Users/sjt/Desktop/portfolio/july 4th.html", "r", encoding="utf-8") as f:
    html = f.read()

def rep(old, new, label):
    global html
    if old in html:
        html = html.replace(old, new, 1)
        print(f"✓ {label}")
    else:
        print(f"✗ NOT FOUND: {label}")

# ── Xiaohongshu ──────────────────────────────────────────────────────────
rep(
    '          <div class="timeline-time">2025.2 - 2025.5<br />上海</div>\n'
    '            <div class="timeline-card">\n'
    '              <h3 class="timeline-role">小红书｜交易市场组C端传播实习生</h3>\n'
    '              <ul class="timeline-list">\n'
    '                <li><strong>内容增长</strong>：参与平台级电商项目（春日服装趋势、花朵配饰）传播策略制定，负责传播执行及数据复盘优化。</li>\n'
    '                <li><strong>KOL与社群运营</strong>：搭建分层KOL/KOC运营体系（高点买手/重点买手/社群作者），运营10+个社群（1,300人），累计促产2,000+篇笔记，达成20位明星/核心买手合作，重点笔记23篇，累计实现百万级曝光。</li>\n'
    '                <li><strong>投流与数据优化</strong>：基于CTR/CES等指标优化初始投流与加投策略，优质内容CTR达8%+；参与亿级流量资源统筹（开屏/信息流/搜索等），优化“内容种草–兴趣转化–电商成交”链路，提升服配类目内容渗透率。</li>\n'
    '                <li><strong>活动策划与落地</strong>：策划“春日秀场”全国员工内卖会（线上+线下）。搭建线上H5会场，招商139家商家、筛选300款商品，GMV+78%，订单量+129%；线下负责场地统筹、物料投放规划与现场执行。</li>\n'
    '              </ul>\n'
    '            </div>',

    '          <div class="timeline-time lang-zh">2025.2 - 2025.5<br />上海</div>\n'
    '          <div class="timeline-time lang-en">Feb – May 2025<br />Shanghai</div>\n'
    '            <div class="timeline-card">\n'
    '              <h3 class="timeline-role lang-zh">小红书｜交易市场组C端传播实习生</h3>\n'
    '              <h3 class="timeline-role lang-en">Xiaohongshu | C-End Communications Intern, Transaction Marketplace</h3>\n'
    '              <ul class="timeline-list lang-zh">\n'
    '                <li><strong>内容增长</strong>：参与平台级电商项目（春日服装趋势、花朵配饰）传播策略制定，负责传播执行及数据复盘优化。</li>\n'
    '                <li><strong>KOL与社群运营</strong>：搭建分层KOL/KOC运营体系（高点买手/重点买手/社群作者），运营10+个社群（1,300人），累计促产2,000+篇笔记，达成20位明星/核心买手合作，重点笔记23篇，累计实现百万级曝光。</li>\n'
    '                <li><strong>投流与数据优化</strong>：基于CTR/CES等指标优化初始投流与加投策略，优质内容CTR达8%+；参与亿级流量资源统筹（开屏/信息流/搜索等），优化“内容种草–兴趣转化–电商成交”链路，提升服配类目内容渗透率。</li>\n'
    '                <li><strong>活动策划与落地</strong>：策划“春日秀场”全国员工内卖会（线上+线下）。搭建线上H5会场，招商139家商家、筛选300款商品，GMV+78%，订单量+129%；线下负责场地统筹、物料投放规划与现场执行。</li>\n'
    '              </ul>\n'
    '              <ul class="timeline-list lang-en">\n'
    '                <li><strong>Content Growth</strong>: Contributed to platform-level e-commerce campaign strategy (Spring fashion trends, floral accessories), leading execution and data-driven post-campaign optimization.</li>\n'
    '                <li><strong>KOL &amp; Community Operations</strong>: Built a tiered KOL/KOC system (top buyers / key buyers / community creators), managed 10+ communities (1,300 members), generated 2,000+ posts, secured 20 celebrity/core buyer collaborations with 23 featured posts, driving millions of impressions.</li>\n'
    '                <li><strong>Paid Distribution &amp; Optimization</strong>: Optimized initial and incremental paid distribution based on CTR/CES metrics, achieving 8%+ CTR on top content; coordinated hundred-million-scale traffic resources (splash/feed/search) to optimize the content-to-purchase funnel and increase fashion category penetration.</li>\n'
    '                <li><strong>Event Planning &amp; Execution</strong>: Organized the “Spring Showcase” nationwide employee internal sale (online + offline). Built the online H5 venue, onboarded 139 merchants and curated 300 products, achieving +78% GMV and +129% orders; managed venue logistics, materials, and on-site execution for the offline event.</li>\n'
    '              </ul>\n'
    '            </div>',
    "Experience: Xiaohongshu"
)

# ── Meituan header ────────────────────────────────────────────────────────
rep(
    '                  <span class="project-meta">异地场景下“酒店+X”跨业态神券投放模型构建｜队长</span>\n'
    '                  <h3 class="project-title">第6届美团商业分析精英大赛</h3>',

    '                  <span class="project-meta lang-zh">异地场景下“酒店+X”跨业态神券投放模型构建｜队长</span>\n'
    '                  <span class="project-meta lang-en">“Hotel+X” Cross-Category Coupon Targeting Model | Team Lead</span>\n'
    '                  <h3 class="project-title lang-zh">第6届美团商业分析精英大赛</h3>\n'
    '                  <h3 class="project-title lang-en">6th Meituan Business Analytics Elite Competition</h3>',
    "Project: Meituan header"
)

# ── CMI header ────────────────────────────────────────────────────────────
rep(
    '                  <span class="project-meta">Sarah’s Circle 整合营销咨询｜项目成员</span>\n'
    '                  <h3 class="project-title">西北大学CAUSE MARKETING INITIATIVE</h3>',

    '                  <span class="project-meta lang-zh">Sarah’s Circle 整合营销咨询｜项目成员</span>\n'
    '                  <span class="project-meta lang-en">Integrated Marketing Consulting for Sarah’s Circle | Team Member</span>\n'
    '                  <h3 class="project-title">Northwestern University CAUSE MARKETING INITIATIVE</h3>',
    "Project: CMI header"
)

# ── CMI bullets ───────────────────────────────────────────────────────────
rep(
    '                  <li>为芝加哥非营利组织Sarah’s Circle提供整合营销咨询，涵盖受众分析、媒体渠道审计与策略、网站优化；</li>\n'
    '                  <li>主导Facebook付费广告板块：通过Meta Business Suite数据分析，审计付费社交效率漏洞，设计投放配置指南，涵盖广告活动结构、地理位置A/B测试方案、素材选择逻辑、GA4 Conversion Tracking及阶段性预算scaling决策框架；</li>\n'
    '                  <li>参与网站优化，基于GA4分析各渠道停留时长、点击路径与表现，提出转化路径优化及页面UX改进。</li>',

    '                  <li class="lang-zh">为芝加哥非营利组织Sarah’s Circle提供整合营销咨询，涵盖受众分析、媒体渠道审计与策略、网站优化；</li>\n'
    '                  <li class="lang-zh">主导Facebook付费广告板块：通过Meta Business Suite数据分析，审计付费社交效率漏洞，设计投放配置指南，涵盖广告活动结构、地理位置A/B测试方案、素材选择逻辑、GA4 Conversion Tracking及阶段性预算scaling决策框架；</li>\n'
    '                  <li class="lang-zh">参与网站优化，基于GA4分析各渠道停留时长、点击路径与表现，提出转化路径优化及页面UX改进。</li>\n'
    '                  <li class="lang-en">Provided integrated marketing consulting for Sarah’s Circle, a Chicago nonprofit, covering audience analysis, media channel audit and strategy, and website optimization.</li>\n'
    '                  <li class="lang-en">Led the Facebook paid advertising workstream: audited paid social efficiency gaps via Meta Business Suite, and designed a campaign configuration guide covering campaign structure, geo-based A/B testing, creative selection logic, GA4 Conversion Tracking, and phased budget scaling frameworks.</li>\n'
    '                  <li class="lang-en">Contributed to website optimization by analyzing channel dwell time, click paths, and performance in GA4, proposing conversion path improvements and UX enhancements.</li>',
    "Project: CMI bullets"
)

# ── L'Oréal bullets ───────────────────────────────────────────────────────
rep(
    '                  <li>领导团队全面分析美护发行业市场规模、商业模式、目标人群，充分挖掘市场需求和关键痛点；</li>\n'
    '                  <li>主导选定养发梳赛道进行深度功能探索与竞品分析，设计“养头皮+健发”一体的科技赋能创新产品及推广方案。</li>',

    '                  <li class="lang-zh">领导团队全面分析美护发行业市场规模、商业模式、目标人群，充分挖掘市场需求和关键痛点；</li>\n'
    '                  <li class="lang-zh">主导选定养发梳赛道进行深度功能探索与竞品分析，设计“养头皮+健发”一体的科技赋能创新产品及推广方案。</li>\n'
    '                  <li class="lang-en">Led the team in analyzing market size, business models, and target audiences in the hair and scalp care sector, identifying key market needs and pain points.</li>\n'
    '                  <li class="lang-en">Drove the selection of the scalp-care comb track, conducting deep functional exploration and competitive analysis, and designing a tech-enabled product and go-to-market strategy integrating scalp care and hair health.</li>',
    "Project: L'Oréal bullets"
)

# ── Attention Research header ─────────────────────────────────────────────
rep(
    '                  <span class="project-meta">全国大学生大数据与公共决策大赛排名前20%｜队长</span>\n'
    '                  <h3 class="project-title">“中国政府对于对外开放的关注度”研究</h3>',

    '                  <span class="project-meta lang-zh">全国大学生大数据与公共决策大赛排名前20%｜队长</span>\n'
    '                  <span class="project-meta lang-en">National College Big Data &amp; Public Policy Competition, Top 20% | Team Lead</span>\n'
    '                  <h3 class="project-title lang-zh">“中国政府对于对外开放的关注度”研究</h3>\n'
    '                  <h3 class="project-title lang-en">Research on China’s Government Attention to Opening-Up Policy</h3>',
    "Project: Attention Research header"
)

import os
with open("/Users/sjt/Desktop/portfolio/july 4th.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"\nDone. {os.path.getsize('/Users/sjt/Desktop/portfolio/july 4th.html')//1024}KB")
