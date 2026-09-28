import streamlit as st
import random
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sahlah 💎 | The Diamond Friendship Card",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ADVANCED CSS & ANIMATIONS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at 50% 20%, #081124 0%, #030712 70%, #010204 100%);
        color: #f8fafc;
    }

    @keyframes floatDiamond {
        0% { transform: translateY(0px) rotate(0deg); filter: drop-shadow(0 0 15px rgba(56, 189, 248, 0.6)); }
        50% { transform: translateY(-12px) rotate(5deg); filter: drop-shadow(0 0 35px rgba(186, 230, 253, 0.9)); }
        100% { transform: translateY(0px) rotate(0deg); filter: drop-shadow(0 0 15px rgba(56, 189, 248, 0.6)); }
    }

    @keyframes flyAndBounce {
        0% { transform: translateY(40px) scale(0.5) rotate(0deg); opacity: 0; }
        30% { transform: translateY(-40px) scale(1.2) rotate(180deg); opacity: 1; }
        60% { transform: translateY(10px) scale(0.9) rotate(270deg); opacity: 1; }
        80% { transform: translateY(-15px) scale(1.1) rotate(320deg); opacity: 1; }
        100% { transform: translateY(0px) scale(1) rotate(360deg); opacity: 1; }
    }

    @keyframes pulseGlow {
        0% { box-shadow: 0 0 20px rgba(56, 189, 248, 0.3); }
        50% { box-shadow: 0 0 50px rgba(186, 230, 253, 0.7); }
        100% { box-shadow: 0 0 20px rgba(56, 189, 248, 0.3); }
    }

    @keyframes shimmerText {
        0% { background-position: -200% center; }
        100% { background-position: 200% center; }
    }

    .floating-diamond {
        font-size: 5rem;
        text-align: center;
        animation: floatDiamond 4s ease-in-out infinite;
        margin: 10px 0;
    }

    .flying-diamond-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 20px 0;
    }

    .fly-d1 { font-size: 2.5rem; animation: flyAndBounce 1.2s ease-out infinite alternate; }
    .fly-d2 { font-size: 3rem; animation: flyAndBounce 1.5s ease-out infinite alternate 0.2s; }
    .fly-d3 { font-size: 2.2rem; animation: flyAndBounce 1.1s ease-out infinite alternate 0.4s; }
    .fly-d4 { font-size: 3.2rem; animation: flyAndBounce 1.6s ease-out infinite alternate 0.1s; }
    .fly-d5 { font-size: 2.7rem; animation: flyAndBounce 1.3s ease-out infinite alternate 0.3s; }

    .card-container {
        background: linear-gradient(145deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.8));
        border: 2px solid rgba(186, 230, 253, 0.4);
        border-radius: 30px;
        padding: 3rem 2rem;
        text-align: center;
        animation: pulseGlow 4s infinite ease-in-out;
        position: relative;
        overflow: hidden;
        margin-bottom: 2rem;
        box-shadow: 0 20px 50px rgba(0,0,0,0.6);
    }

    h1, h2, h3 { font-family: 'Playfair Display', serif; }

    .shimmer-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #93c5fd, #ffffff, #38bdf8, #ffffff, #93c5fd);
        background-size: 200% auto;
        color: transparent;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmerText 4s linear infinite;
        margin-bottom: 0px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #0284c7 0%, #1e40af 100%);
        color: white;
        border: 1px solid rgba(186, 230, 253, 0.5);
        border-radius: 35px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        letter-spacing: 1px;
        box-shadow: 0 0 20px rgba(2, 132, 199, 0.5);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #38bdf8 0%, #2563eb 100%);
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.8);
        border-color: #ffffff;
        transform: scale(1.02);
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "card_state" not in st.session_state: 
    st.session_state.card_state = "closed"
if "proposal_accepted" not in st.session_state: 
    st.session_state.proposal_accepted = False
if "vibe_score" not in st.session_state: 
    st.session_state.vibe_score = None
if "reels" not in st.session_state: 
    st.session_state.reels = ["❓", "❓", "❓"]
if "is_sealed" not in st.session_state: 
    st.session_state.is_sealed = False

# ==========================================
# MAIN APP INTERFACE
# ==========================================

st.markdown('<div class="floating-diamond">💎</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="card-container">
        <p style="color: #bae6fd; font-size: 1.1rem; letter-spacing: 4px; text-transform: uppercase;">✨ THE ULTIMATE DIGITAL FRIENDSHIP MASTERPIECE ✨</p>
        <h1 class="shimmer-title">For Sahlah "Diamond"</h1>
        <p style="color: #cbd5e1; font-size: 1.1rem; margin-top: 15px; line-height: 1.6;">
            A custom-crafted interactive diamond tribute built to honor the absolute best friend in the universe. 
            Brilliant, unbreakable, and entirely irreplaceable.
        </p>
    </div>
""", unsafe_allow_html=True)

# Tabs Control Center
tab1, tab2, tab3, tab4 = st.tabs([
    "💌 Open Friendship Card", 
    "⚡ Diamond Vibe Meter", 
    "🎰 Bestie Slot Machine", 
    "🏆 Official Seal"
])

# ------------------------------------------
# TAB 1: THE INTERACTIVE FRIENDSHIP CARD & PROPOSAL
# ------------------------------------------
with tab1:
    st.markdown("### 💌 Inside Sahlah's Special Card")
    st.write("Click below to unfold the card, launch flying diamonds, and reveal Ariya's message and proposal!")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("✨ Open The Friendship Card"):
            st.session_state.card_state = "opened"
    with col2:
        if st.button("🔄 Reset Card View"):
            st.session_state.card_state = "closed"
            st.session_state.proposal_accepted = False

    if st.session_state.card_state == "opened":
        st.markdown("""
            <div class="flying-diamond-container">
                <span class="fly-d1">💎</span><span class="fly-d2">✨</span>
                <span class="fly-d3">💎</span><span class="fly-d4">✨</span><span class="fly-d5">💎</span>
            </div>
            <p style="text-align: center; color: #7dd3fc; font-weight: 600; letter-spacing: 2px;">✨ Flying Diamond Celebration Unlocked! ✨</p>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div style="background: linear-gradient(135deg, rgba(14, 116, 144, 0.25), rgba(30, 41, 59, 0.9)); 
                        border: 2px solid #38bdf8; padding: 2.5rem; border-radius: 20px; 
                        box-shadow: 0 0 30px rgba(56, 189, 248, 0.4); animation: pulseGlow 3s infinite;">
                <h2 style="color: #7dd3fc; text-align: center; font-family: 'Playfair Display', serif;">To My Dearest Diamond, Sahlah 💎</h2>
                <p style="color: #f1f5f9; font-size: 1.15rem; line-height: 1.8; margin-top: 15px; text-align: center;">
                    "They say diamonds are formed under pressure and are the hardest, most brilliant gems on Earth. 
                    That is why 'Diamond' is your true nickname. You bring clarity, unmatched energy, and a constant 
                    spark to life that makes everything better. Thank you for being an extraordinary best friend."
                </p>
                <p style="text-align: right; color: #bae6fd; font-weight: 600; margin-top: 20px;">— Crafted with pride by Ariya ⚡</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
            <div style="background: linear-gradient(135deg, rgba(30, 27, 75, 0.8), rgba(15, 23, 42, 0.9)); 
                        border: 2px dashed #38bdf8; padding: 2.5rem; border-radius: 25px; text-align: center;">
                <div style="font-size: 3rem;">💍💎</div>
                <h2 style="color: #93c5fd; font-family: 'Playfair Display', serif;">The Official Friendship Proposal</h2>
                <p style="color: #e2e8f0; font-size: 1.1rem; line-height: 1.6; margin-top: 15px;">
                    Do you solemnly swear to remain Ariya's ultimate partner-in-crime, 
                    share infinite laughs, never run out of fun vibes, and remain a 100-carat best friend for life and beyond?
                </p>
        """, unsafe_allow_html=True)

        col_p1, col_p2 = st.columns(2)
        with col_p1:
            if st.button("💖 YES! Absolutely Accept!"):
                st.session_state.proposal_accepted = True
                st.balloons()
        with col_p2:
            if st.button("🤭 Obviously Yes (No Choice!)"):
                st.session_state.proposal_accepted = True
                st.balloons()

        if st.session_state.proposal_accepted:
            st.success("🎉 **OFFICIALLY SEALED!** Friendship Proposal Accepted! The Diamond bond is now locked in eternity! 💎✨")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("🔒 The card is currently sealed. Click **'Open The Friendship Card'** above to launch the flying diamonds!")

# ------------------------------------------
# TAB 2: DIAMOND VIBE METER
# ------------------------------------------
with tab2:
    st.markdown("### ⚡ The Diamond Vibe & Energy Analyzer")
    st.write("Test Sahlah's daily aura score using our high-precision crystal scanner!")

    if st.button("🚀 Scan Diamond's Vibe Levels"):
        with st.spinner("Calibrating crystal frequencies..."):
            time.sleep(0.5)
            st.session_state.vibe_score = random.randint(99999, 9999999)

    if st.session_state.vibe_score:
        st.markdown(f"""
            <div style="background: rgba(15, 23, 42, 0.9); border: 2px solid #38bdf8; padding: 2.5rem; border-radius: 20px; text-align: center; margin-top: 1.5rem;">
                <p style="color: #94a3b8; text-transform: uppercase; letter-spacing: 2px;">Scanned Aura Result</p>
                <h1 style="color: #7dd3fc; font-size: 3.5rem; margin: 10px 0;">✨ {st.session_state.vibe_score:,} Carats ✨</h1>
                <p style="color: #f8fafc; font-size: 1.15rem;">
                    <b>Status:</b> Maximum Overdrive! Breaking cosmic charts with legendary humor and top-tier bestie aura. 🚀💎
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Click the scan button above to calculate today's aura rating!")

# ------------------------------------------
# TAB 3: DIAMOND MATCH SLOT MACHINE GAME
# ------------------------------------------
with tab3:
    st.markdown("### 🎰 The Diamond Match Vibe Check")
    st.write("Spin the reels! Match all 3 Diamonds to unlock Maximum Bestie Luck for the day!")

    emojis = ["💎", "✨", "💙", "🚀", "👑"]
    
    if st.button("🎰 SPIN THE REELS!"):
        with st.spinner("Spinning the crystal slots..."):
            time.sleep(0.5)
            if random.random() > 0.3: 
                st.session_state.reels = ["💎", "💎", "💎"]
            else:
                st.session_state.reels = [random.choice(emojis), random.choice(emojis), random.choice(emojis)]

    st.markdown(f"""
        <div style="background: #0f172a; border: 3px solid #38bdf8; border-radius: 20px; padding: 2rem; display: flex; justify-content: space-evenly; font-size: 4rem; margin: 1.5rem 0; box-shadow: inset 0 0 20px rgba(0,0,0,0.8);">
            <span>{st.session_state.reels[0]}</span>
            <span style="color: #38bdf8;">|</span>
            <span>{st.session_state.reels[1]}</span>
            <span style="color: #38bdf8;">|</span>
            <span>{st.session_state.reels[2]}</span>
        </div>
    """, unsafe_allow_html=True)

    if st.session_state.reels == ["💎", "💎", "💎"]:
        st.success("🎉 **JACKPOT! TRIPLE DIAMOND!** Sahlah's luck and vibe energy are unmatched today! ✨")
        st.balloons()
    elif "❓" not in st.session_state.reels:
        st.info("So close! Spin again to hit the Diamond Jackpot!")

# ------------------------------------------
# TAB 4: OFFICIAL SEAL & CERTIFICATE (FIXED & STREAMLINED)
# ------------------------------------------
with tab4:
    st.markdown("### 🏆 Official 100-Carat Friendship Certificate")
    st.write("Review the certificate below, then click the button to formally stamp and seal it.")

    # Control buttons for sealing
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if not st.session_state.is_sealed:
            if st.button("🔏 Stamp & Seal Certificate"):
                st.session_state.is_sealed = True
                st.balloons()
                st.rerun()
    with col_btn2:
        if st.session_state.is_sealed:
            if st.button("🔄 Unseal Certificate"):
                st.session_state.is_sealed = False
                st.rerun()

    # Status indicator
    if st.session_state.is_sealed:
        st.success("🔒 Certificate status: Officially SEALED by Ariya!")
    else:
        st.warning("⚠️ Certificate status: Unsealed. Click the stamp button above to lock it!")

    # Certificate Container rendered using clean native Streamlit elements (Zero raw HTML block text bugs)
    with st.container():
        st.markdown("""
        <div style="background: linear-gradient(145deg, #090d16, #030712); 
                    border: 3px solid #38bdf8; padding: 3rem; border-radius: 25px; text-align: center; 
                    box-shadow: 0 0 50px rgba(56, 189, 248, 0.4); margin-top: 1rem;">
            <div style="font-size: 3.5rem; margin-bottom: 10px;">💎</div>
            <h1 style="color: #7dd3fc; font-family: 'Playfair Display', serif; font-size: 2.2rem; margin: 0;">Certificate of Supreme Best Friendship</h1>
            <p style="letter-spacing: 4px; color: #94a3b8; font-size: 0.85rem; margin-top: 5px;">100-CARAT UNBREAKABLE CERTIFICATION</p>
            <hr style="border-color: rgba(255,255,255,0.15); margin: 2rem 0;">
            <p style="font-size: 1.1rem; color: #e2e8f0;">This highest honor is formally bestowed upon</p>
            <h2 style="color: #ffffff; text-shadow: 0 0 15px rgba(255,255,255,0.9); font-size: 2.8rem; margin: 10px 0;">Sahlah "Diamond"</h2>
            <p style="font-size: 1.05rem; color: #cbd5e1; max-width: 650px; margin: 0 auto 2rem auto;">
                For holding the cherished nickname <b>Diamond</b>, being an anchor of strength and joy, 
                and shining with peerless brilliance through every single chapter of life.
            </p>
        """, unsafe_allow_html=True)

        # Show official stamp badge if sealed
        if st.session_state.is_sealed:
            st.markdown("""
            <div style="margin: 20px auto; display: inline-block; background: radial-gradient(circle, #fbbf24 0%, #b45309 100%); 
                        border: 3px dashed #fef3c7; border-radius: 50%; width: 120px; height: 120px; 
                        display: flex; flex-direction: column; justify-content: center; align-items: center;
                        box-shadow: 0 0 25px rgba(251, 191, 36, 0.7); transform: rotate(-10deg);">
                <p style="color: white; font-weight: 900; font-size: 0.75rem; margin: 0; text-shadow: 1px 1px 2px black;">APPROVED</p>
                <p style="color: white; font-size: 1.2rem; margin: 0;">💎</p>
                <p style="color: white; font-weight: 900; font-size: 0.75rem; margin: 0; text-shadow: 1px 1px 2px black;">BY ARIYA</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
            <div style="display: flex; justify-content: space-between; margin-top: 3rem; padding: 0 2rem;">
                <div>
                    <p style="border-top: 2px solid #38bdf8; padding-top: 5px; color: #7dd3fc; font-weight: 600; margin: 0;">Ariya</p>
                    <p style="font-size: 0.8rem; color: #64748b; margin: 2px 0 0 0;">Creator & Best Friend</p>
                </div>
                <div>
                    <p style="border-top: 2px solid #38bdf8; padding-top: 5px; color: #7dd3fc; font-weight: 600; margin: 0;">Infinity 💎</p>
                    <p style="font-size: 0.8rem; color: #64748b; margin: 2px 0 0 0;">Valuation Status</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)