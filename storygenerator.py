import streamlit as st


def build_story(topic: str, genre: str, length: int) -> str:
    title = topic.strip().title() or "A Wonderful Tale"
    intro = f"Once upon a time, {topic.lower()} became the center of a {genre.lower()} adventure."
    middle = (
        f"Along the winding path, brave hearts discovered hidden wonders, solved a mystery, "
        f"and learned that courage grows when it is shared."
    )
    ending = "And so, the story ended with hope, laughter, and a promise of another adventure tomorrow."

    paragraphs = [
        f"## {title}",
        "",
        f"{intro}",
        f"{middle}",
        f"{ending}",
    ]

    story = "\n\n".join(paragraphs)
    return story[:length]


def main() -> None:
    st.set_page_config(page_title="📖 AI Story Generator", page_icon="📚")

    st.title("📖 AI Story Generator")
    st.write("Generate creative stories using a built-in story engine")

    topic = st.text_input(
        "Story Topic",
        placeholder="A dragon that loves pizza",
    )

    genre = st.selectbox(
        "Genre",
        [
            "Adventure",
            "Fantasy",
            "Sci-Fi",
            "Mystery",
            "Comedy",
            "Horror",
        ],
    )

    length = st.slider("Story Length", 100, 400, 200, step=50)

    if st.button("✨ Generate Story"):
        if topic.strip() == "":
            st.warning("Please enter a story topic.")
            st.stop()

        with st.spinner("Crafting your story..."):
            story = build_story(topic, genre, length)

        st.subheader("📚 Your Story")
        st.write(story)


if __name__ == "__main__":
    main()
