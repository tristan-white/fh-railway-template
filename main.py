from fasthtml.common import *

app = FastHTML(
    # https://fastht.ml/docs/tutorials/by_example.html#styling-basics
    hdrs=(picolink) # comment this out to remove picocss styling
)

@app.route('/')
def get():
    return Div(
        P("Hello World!"),
        A("click me", href="/example")
    )

# For a slightly more complex page, browse to "/example"
@app.route('/example')
def get():
    return (
        Title("Page Title"),
        Body(
            Header(
                H1(Nav(
                    Ul(Li(A("Home", href="/", style="color: inherit"))),
                    Ul(Li(A("Example", href="https://higheraspire.com", cls="secondary", target="_blank")))
                )),
            ),
            Main(
                H1("Congrats! 🎉"),
                P("You've built a website with FastHTML!"),
                P("Here are some helpful links:"),
                Ul(
                    Li(A("FastHTML Docs", href="https://fastht.ml/docs/")),
                    Li(
                        "FastHTML has an active ",
                        A("discord", href="https://discord.gg/qcXvcxMhdP"),
                        ". If you can't find an answer in the docs, try asking there.",
                    ),
                    Li(
                        "If you don't enjoy HTML/CSS, FastHTML integrates nicely with ",
                        A("picocss", href="https://picocss.com/"),
                        ", a small, simple, clean css framework. This page uses picocss. See ",
                        A("this page", href="https://4mrnhq.csb.app/"),
                        " for an example of what it can do.",
                    ),
                    Li(
                        "To connect to this railway app from CLI, install the ", A("railway CLI app", href="https://docs.railway.com/guides/cli#installing-the-cli"),
                        ", then run ",
                        Code("railway link"),
                    ),
                    Li(
                        "Many railway projects use docker, but I've found that FastHTML apps are simple enough that docker isn't strictly necessary. I would suggest using the python package and project manager ",
                        A("uv", href="https://docs.astral.sh/uv/"),
                        " (that is what this template is using)."
                    ),
                    Li(
                        "If this template helped you, please give the ", A("github repo", href="https://github.com/tristan-white/fh-railway-template/"),  " a ⭐ to help others find it!"
                    )
                )
            ),
            cls="container" # this centers the content on the within Body
        )
    )

@app.route('/my-page')
def get():
    return Div(
        P("Try creating a page here!")
    )

serve()