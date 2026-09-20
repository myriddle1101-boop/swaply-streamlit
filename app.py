from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Swaply · 技能互换", page_icon="↔️", layout="wide")

ASSETS = Path(__file__).parent / "assets"

SKILLS = [
    {
        "title": "周末人像摄影漫步",
        "category": "摄影",
        "mode": "线下",
        "image": ASSETS / "photography.jpg",
        "person": "林悦",
        "avatar": "LY",
        "role": "职业摄影师",
        "years": "5年",
        "level": "专业级",
        "proof": "摄影协会认证",
        "time": "周六 14:00–17:00",
        "location": "South Kensington · 1.2 km",
        "match": 96,
        "intro": "从自然光到构图，一起在街头边拍边学。",
        "detail": "自然光人像、街头构图、相机手动模式与 Lightroom 基础调色。适合刚买相机或希望摆脱自动模式的学习者。",
        "offers": "人像摄影 / Lightroom",
        "wants": "建筑设计 / 作品集",
        "reason": "你会的建筑设计正是林悦想学的，双方周六下午都有空。",
    },
    {
        "title": "零基础弹会第一首歌",
        "category": "音乐",
        "mode": "线上/线下",
        "image": ASSETS / "guitar.jpg",
        "person": "陈墨",
        "avatar": "CM",
        "role": "独立音乐人",
        "years": "7年",
        "level": "进阶",
        "proof": "8次交换好评",
        "time": "周末 / 工作日晚间",
        "location": "Camden · 可线上",
        "match": 91,
        "intro": "不背枯燥乐理，用喜欢的歌认识和弦与节奏。",
        "detail": "从持琴、和弦到节奏型，用你喜欢的一首歌完成第一次弹唱。不需要任何乐理基础。",
        "offers": "民谣吉他 / 编曲入门",
        "wants": "Figma / UI 设计",
        "reason": "你的 Figma 经验符合他的学习目标，可以从一次体验交换开始。",
    },
    {
        "title": "用 Python 读懂一份数据",
        "category": "编程",
        "mode": "线上",
        "image": ASSETS / "python.jpg",
        "person": "Alex",
        "avatar": "AX",
        "role": "数据分析师",
        "years": "4年",
        "level": "专业级",
        "proof": "职业经历已验证",
        "time": "工作日 19:00 后",
        "location": "线上交换",
        "match": 87,
        "intro": "带着真实问题完成清洗、分析和可视化。",
        "detail": "用真实数据完成清洗、探索与可视化。不会只讲语法，而是一起做出一个可展示的小项目。",
        "offers": "Python / 数据可视化",
        "wants": "作品集叙事 / 排版",
        "reason": "你们都偏好项目制学习，且工作日晚间的时间高度重合。",
    },
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] {font-family:'DM Sans','Noto Sans SC',sans-serif;}
.stApp {background:#FFF9ED;}
#MainMenu, footer {visibility:hidden;}
[data-testid="stHeader"] {background:rgba(255,249,237,.88); border-bottom:1px solid #EADFCE;}
.block-container {max-width:1180px; padding-top:1.2rem; padding-bottom:5rem;}
.brand {font-size:1.55rem;font-weight:800;letter-spacing:-.04em}.brand b{color:#FF7200}.brand-mark{display:inline-grid;place-items:center;width:36px;height:36px;background:#FF7200;color:white;border-radius:11px;margin-right:9px}
.hero {text-align:center;padding:3.2rem 0 1.6rem}.eyebrow{display:inline-block;background:#FFF0CC;color:#874500;border:1px solid #FFDA83;padding:.35rem .7rem;border-radius:99px;font-weight:700;font-size:.82rem}.hero h1{font-size:clamp(2.5rem,6vw,4.4rem);line-height:1.04;letter-spacing:-.055em;margin:1rem 0 .7rem}.hero h1 em{font-style:normal;color:#FF7200}.hero p{color:#766D60;font-size:1.1rem}
[data-testid="stTextInputRootElement"] {background:white;border-radius:15px;border-color:#EADFCE;box-shadow:0 12px 34px rgba(128,78,14,.08)}
.skill-card {background:white;border:1px solid #EADFCE;border-radius:0 0 18px 18px;padding:1rem 1.1rem 1.1rem;margin-top:-.5rem;min-height:190px;box-shadow:0 12px 30px rgba(117,70,11,.06)}
.skill-type{font-size:.76rem;color:#C54A00;font-weight:800;letter-spacing:.08em}.skill-title{font-size:1.25rem;font-weight:800;margin:.35rem 0}.skill-intro{color:#766D60;line-height:1.55;min-height:50px}.person{border-top:1px solid #F0E7DA;margin-top:.8rem;padding-top:.8rem;font-size:.88rem}.person span{color:#766D60}.match{background:#FFCA28;color:#5D3400;padding:.26rem .5rem;border-radius:99px;font-size:.75rem;font-weight:800;float:right}
[data-testid="stImage"] img {border-radius:18px 18px 0 0;aspect-ratio:4/3;object-fit:cover;}
.detail-head{background:#282218;color:white;border-radius:20px;padding:1.4rem;margin:.8rem 0 1.2rem}.detail-head small{color:#FFCA28;font-weight:800}.detail-head h2{margin:.35rem 0}.detail-head p{color:#D8D0C4}.stat{background:white;border:1px solid #EADFCE;border-radius:13px;padding:.8rem;min-height:83px}.stat small{display:block;color:#766D60;margin-bottom:.3rem}.swap{background:#282218;color:white;padding:1.15rem;border-radius:15px;margin:1rem 0}.swap b{color:#FFCA28}.section-title{font-weight:800;font-size:1.15rem;margin:1.3rem 0 .45rem}
.stButton>button {border-radius:12px;font-weight:700;border-color:#E3D5C0}.stButton>button[kind="primary"] {background:#FF7200;border-color:#FF7200;color:white}.stButton>button[kind="primary"]:hover{background:#D94D00;border-color:#D94D00}.stPills [data-baseweb="button-group"]{justify-content:center}
div[data-testid="stDialog"] > div {background:#FFF9ED;border-radius:22px}
@media(max-width:640px){.hero{text-align:left;padding-top:2rem}.hero h1{font-size:2.55rem}.block-container{padding-left:1rem;padding-right:1rem}}
</style>
""", unsafe_allow_html=True)

if "selected" not in st.session_state:
    st.session_state.selected = None
if "saved" not in st.session_state:
    st.session_state.saved = set()


@st.dialog("发布我能教的", width="large")
def publish_dialog():
    with st.form("publish_form"):
        a, b = st.columns(2)
        skill = a.text_input("技能名称", "建筑设计")
        b.selectbox("技能分类", ["设计", "摄影", "音乐", "编程", "语言", "运动"])
        st.text_area("简单介绍一下你能教什么", "可以帮助零基础学习者理解空间设计，并完成一个小型作品集项目。")
        a, b = st.columns(2)
        a.selectbox("你的水平", ["能独立教授", "熟练", "专业级"])
        b.selectbox("技能年限", ["5年以上", "3–5年", "1–3年", "1年以内"])
        st.text_input("能力证明（选填）", placeholder="证书、工作经历或作品链接")
        a, b = st.columns(2)
        a.multiselect("空闲时间", ["工作日上午", "工作日下午", "工作日晚间", "周末上午", "周末下午"], ["周末下午"])
        b.text_input("所在地区", "London · South Kensington")
        st.pills("授课方式", ["线下见面", "线上远程"], selection_mode="multi", default=["线下见面"])
        st.text_input("你想交换什么技能？", "人像摄影、吉他")
        st.caption("不会展示价格。对方会用自己能教的技能向你提出交换方案。")
        if st.form_submit_button("预览并发布", type="primary", use_container_width=True):
            st.success(f"“{skill}”已发布，正在为你寻找交换伙伴。")


@st.dialog("筛选技能")
def filter_dialog():
    a, b = st.columns(2)
    a.selectbox("教学方式", ["不限", "线下", "线上"])
    b.selectbox("技能水平", ["不限", "入门教学", "进阶", "专业级"])
    a.selectbox("空闲时间", ["不限", "工作日", "周末", "晚上"])
    b.selectbox("距离", ["不限", "3 km 内", "5 km 内", "仅线上"])
    st.text_input("所在地", "London")
    st.checkbox("优先展示与我双向匹配的人", True)
    if st.button("应用筛选", type="primary", use_container_width=True):
        st.session_state.filter_applied = True
        st.rerun()


top_a, top_b = st.columns([5, 1.2], vertical_alignment="center")
top_a.markdown('<div class="brand"><span class="brand-mark">↔</span>Swap<b>ly</b></div>', unsafe_allow_html=True)
if top_b.button("＋ 发布技能", type="primary", use_container_width=True):
    publish_dialog()

if st.session_state.selected is None:
    st.markdown('<section class="hero"><span class="eyebrow">✦ 技能互换，不谈价格</span><h1>分享你会的，<br><em>遇见你想学的。</em></h1><p>搜索一项技能，找到愿意和你交换的人。</p></section>', unsafe_allow_html=True)
    s1, s2 = st.columns([5, 1])
    query = s1.text_input("search", placeholder="想学什么？试试「摄影」「吉他」「Python」", label_visibility="collapsed")
    if s2.button("☷ 筛选", use_container_width=True):
        filter_dialog()
    category = st.pills("技能分类", ["为你推荐", "摄影", "音乐", "编程", "设计", "语言"], default="为你推荐", label_visibility="collapsed")
    st.markdown("### 值得交换的新技能")
    st.caption("根据你的兴趣、距离与时间为你推荐")

    results = [x for x in SKILLS if (not query or query.lower() in (x["title"] + x["category"] + x["intro"] + x["offers"]).lower()) and (category in (None, "为你推荐") or x["category"] == category)]
    if not results:
        st.info("暂时没有找到相关技能。换个关键词，或发布你能教的技能。")
    else:
        cols = st.columns(3)
        for idx, skill in enumerate(results):
            original_idx = SKILLS.index(skill)
            with cols[idx % 3]:
                st.image(skill["image"], use_container_width=True)
                saved = original_idx in st.session_state.saved
                st.markdown(f'''<div class="skill-card"><span class="skill-type">{skill["category"]} · {skill["mode"]}</span><span class="match">{skill["match"]}% 匹配</span><div class="skill-title">{skill["title"]}</div><div class="skill-intro">{skill["intro"]}</div><div class="person"><b>{skill["person"]}</b> · {skill["role"]}<br><span>⌖ {skill["location"]}</span></div></div>''', unsafe_allow_html=True)
                a, b = st.columns([1, 2])
                if a.button("♥" if saved else "♡", key=f"save_{original_idx}", use_container_width=True):
                    if saved: st.session_state.saved.remove(original_idx)
                    else: st.session_state.saved.add(original_idx)
                    st.rerun()
                if b.button("查看详情 →", key=f"detail_{original_idx}", type="primary", use_container_width=True):
                    st.session_state.selected = original_idx
                    st.rerun()
else:
    skill = SKILLS[st.session_state.selected]
    if st.button("← 返回推荐"):
        st.session_state.selected = None
        st.rerun()
    left, right = st.columns([1.05, 1], gap="large")
    with left:
        st.image(skill["image"], use_container_width=True)
    with right:
        st.markdown(f'<div class="detail-head"><small>{skill["category"]} · {skill["mode"]} · {skill["match"]}% 匹配</small><h2>{skill["title"]}</h2><p>{skill["intro"]}</p></div>', unsafe_allow_html=True)
        st.markdown(f"**{skill['person']}** · {skill['role']}　<span style='color:#FF7200'>✓ 身份与经历已验证</span>", unsafe_allow_html=True)
        a, b = st.columns(2)
        a.markdown(f'<div class="stat"><small>技能水平</small><b>{skill["level"]}</b></div>', unsafe_allow_html=True)
        b.markdown(f'<div class="stat"><small>技能年限</small><b>{skill["years"]}</b></div>', unsafe_allow_html=True)
        a, b = st.columns(2)
        a.markdown(f'<div class="stat"><small>能力证明</small><b>{skill["proof"]}</b></div>', unsafe_allow_html=True)
        b.markdown(f'<div class="stat"><small>空闲时间</small><b>{skill["time"]}</b></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">你可以学到什么</div>', unsafe_allow_html=True)
    st.write(skill["detail"])
    st.markdown(f'<div class="swap"><b>对方能教：</b>{skill["offers"]}<br><br>↔️<br><br><b>对方想学：</b>{skill["wants"]}</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">为什么推荐给你</div>', unsafe_allow_html=True)
    st.write(skill["reason"])
    st.caption(f"⌖ {skill['location']}　·　◷ {skill['time']}")
    a, b = st.columns([1, 2])
    if a.button("♡ 收藏", use_container_width=True):
        st.session_state.saved.add(st.session_state.selected)
        st.toast("已加入收藏")
    if b.button("发起技能交换", type="primary", use_container_width=True):
        st.success(f"已向 {skill['person']} 发起交换邀约，对方接受后即可协商时间与地点。")
