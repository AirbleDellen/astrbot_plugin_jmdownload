from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import astrbot.api.message_components as Comp
import shutil
import os
import jmcomic
from jmcomic import *

@register("jmdownload", "AirbleDellen", "报告塔台准备起飞", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        pass

    @filter.command_group("jm")
    def jm(self):
        pass

    @jm.command("view")
    async def add(self, event: AstrMessageEvent, a: str):
        client = JmOption.default().new_jm_client()
        page = client.search_site(search_query=a)
        album: JmAlbumDetail = page.single_album
        yield event.plain_result(f"作者：{album.author}\n标题：{album.name}\n标签：{album.tags}\n页数：{album.page_count}")
        yield event.plain_result("下载请输入‘jm down 车牌号’指令")

    @jm.command("down")
    async def sub(self, event: AstrMessageEvent, a: str):
        client = JmOption.default().new_jm_client()
        page = client.search_site(search_query=a)
        album: JmAlbumDetail = page.single_album
        yield event.plain_result(f"正在清空跑道{a}:{album.name}")
        jmcomic.download_album(a, extra=jmcomic.Feature.export_pdf)
        shutil.rmtree(album.name)
        yield event.plain_result("正在滑行")
        chain = [
            Comp.File(file=f"[JM{a}]{album.name}.pdf", name=f"{album.name}.pdf")
        ]
        yield event.chain_result(chain)
        os.remove(f"[JM{a}]{album.name}.pdf")
        yield event.plain_result("允许起飞")