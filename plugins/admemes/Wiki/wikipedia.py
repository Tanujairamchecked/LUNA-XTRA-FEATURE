import wikipedia
from pyrogram import Client,filters
from plugins.admemes.Wiki.pluginhelpers import edit_or_reply
from plugins.admemes.Wiki.basic_helpers import get_text


@Client.on_message(filters.command(["wiki", "wikipedia"]))
async def wikipediasearch(Client, message):
    event = await edit_or_reply(message, "ππ΄π°ππ²π·πΈπ½πΆ...π")
    query = get_text(message)
    if not query:
        await event.edit("πΈπ½ππ°π»πΈπ³ πππ½ππ°π ππ΄π΄ π·π΄π»πΏ πΌπ΄π½π ππΎ πΊπ½πΎπ π·πΎπ ππΎ πππ΄ ππ·πΈπ π²πΎπΌπΌπ°π½π³")
        return
    results = wikipedia.search(query)
    result = ""
    for s in results:
        try:
            page = wikipedia.page(s)
            url = page.url
            result += f"π [{s}]({url}) \n"
        except BaseException:
            pass
    await event.edit(
        "πππππππΏππΌ πππΌππΎπ: {} \n\n Result: \n\n{}".format(query, result),
        disable_web_page_preview=True,
    )
