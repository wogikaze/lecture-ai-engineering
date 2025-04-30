import streamlit as st
import pandas as pd

# --- Streamlit configuration ---
st.set_page_config(
    page_title="Neknaj Circuit Game – Docs",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- Helper data -------------------------------------------------------------
FEATURES = [
    {"Feature": "DSL for digital circuits", "Description": "Domain specific language to describe modules, gates, and tests."},
    {"Feature": "Transpile to TypeScript", "Description": "Compile your circuit description to runnable TypeScript."},
    {"Feature": "CLI & Web development", "Description": "Choose between command-line or browser-based workflow."},
]

INSTALL_STEPS = """1. Clone repository  
```bash
git clone https://github.com/neknaj/circuitgame
cd circuitgame
```

2. Build CLI (Rust)  
```bash
cargo build --release
# Binary: ./target/release/circuitgame_bin
```

3. Build Web tool (Node)  
```bash
npm install
node build.js
```"""

USAGE_CLI = """```bash
# Watch file & serve on port 8080
cargo run -- -i spec/sample.ncg -s 8080
# or if installed:
ncg -i spec/sample.ncg -s 8080
```"""

SAMPLE_CODE = """using nor:2->1;

// NOT gate module
module not (x)->(a) {
    a: nor <- x x;
}

// Tests for NOT gate
test not:1->1 {
    t -> f;
    f -> t;
}
"""

# --- Page content ------------------------------------------------------------
st.title("Neknaj Circuit Game")
st.caption("A simulation tool for designing and testing digital circuits.")

st.header("Overview")
st.markdown(
    """Neknaj Circuit Game (NCG) lets you **design**, **compile**, and **test** logic circuits
in a concise textual format. It supports a domain-specific language (DSL) that can be
transpiled to TypeScript, and offers both a Rust-based CLI and a browser editor.""")

st.header("Key Features")
st.dataframe(pd.DataFrame(FEATURES))

st.header("Installation")
st.markdown(INSTALL_STEPS)

st.header("CLI Usage")
st.markdown(USAGE_CLI)

st.header("Language Sample")
st.code(SAMPLE_CODE, language="ncg")

with st.expander("Live Demo (external link)"):
    st.markdown(
        "[Open Web Playground](https://neknaj.github.io/circuitgame/)")

st.header("Resources & Links")
st.markdown(
    """- **Repository**: <https://github.com/neknaj/circuitgame>  
- **Language spec**: <https://raw.githubusercontent.com/neknaj/circuitgame/main/spec/lang.bnf>  
- **Tutorial**: <https://neknaj.github.io/circuitgame/tutorial>  
- **License**: MIT
""")