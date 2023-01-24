from wordcloud import WordCloud
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

# Data
natophonetics = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima", "M": "Mike",
                 "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-Ray", "Y": "Yankee", "Z": "Zulu"}

leet_dict = {'a': '4', 'b': 'l3',
             'c': '(', 'd': '[)', 'e': '3', 'l': '1', 's': '5', 't': '+', 'w': '\\/\\/', 'o': '0'}


greek_dict = {'a': 'α', 'b': 'β', 'g': 'γ', 'd': 'δ', 'e': 'ε', 'z': 'ζ', 'h': 'η', 'th': 'θ', 'i': 'ι', 'k': 'κ', 'l': 'λ',
              'm': 'μ', 'n': 'ν', 'x': 'ξ', 'o': 'ω', 'p': 'π', 'r': 'ρ', 't': 'τ', 'u': 'υ', 'ph': 'φ', 'ch': 'χ', 'ps': 'ψ', 's': 'σ'}

# functions


def leet_conv(term):
    result = [leet_dict.get(i, i) for i in list(term.lower())]
    return ''.join(result)


def greek_conv(term):
    result = [greek_dict.get(i, i) for i in list(term.lower())]
    return ''.join(result)


def nato_phonetize(term):
    result = [natophonetics.get(i, i) for i in list(term.upper())]
    return ' '.join(result)


def plot_wordcloud(docx):
    mywordcloud = WordCloud().generate(docx)
    fig = plt.figure(figsize=(20, 10))
    plt.imshow(mywordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)


def main():
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        col1, col2 = st.columns(2)
        with col1:
            st.info("Leet-Converter")
        # Form
            with st.form(key="leetform", clear_on_submit=True):
                rawtext = st.text_area("Enter Text Here ")
                convertion_choice = st.selectbox("Choice", ['Normal', 'Greek'])
                submit_button = st.form_submit_button(label="Convert")

        # Result
            if submit_button:
                if rawtext != None:
                    st.info("Result")
                    st.write("Original : {} ".format(rawtext))
                    if convertion_choice == 'Greek':
                        result = leet_conv(rawtext)
                    else:
                        result = greek_conv(rawtext)
                    st.info("Converted")
                    st.code(result)

                    with st.expander("Visualise"):

                        plot_wordcloud(rawtext)

        with col2:
            st.success("Nato-Phonetizer")
            # Form
            with st.form(key="natoform", clear_on_submit=True):
                rawtext = st.text_area("Enter Text Here ")
                submit_button = st.form_submit_button(label="Phonetize")
            if submit_button:
                if rawtext != None:
                    st.info("Result")
                    st.write("Original : {} ".format(rawtext))
                    result = nato_phonetize(rawtext)
                    st.info("Converted")
                    st.code(result)
                    with st.expander("Visualise"):

                        plot_wordcloud(result)
    else:
        st.subheader("About")
        st.text("LeetSpeak App")


if __name__ == "__main__":
    main()
