import discord
from discord.ext import commands
from lisa.settings import BACKEND_URL, __version__
from core.connections import GraphQLQuery

bot = commands.Bot(command_prefix='l>')


@bot.event
async def on_ready():
    print('Runnin smooth!')


@bot.command(aliases=['v'])
async def version(ctx):
    """
    Bot version
    """
    service_version = GraphQLQuery.lisa_service_version()
    response = f'''
    Bot version: {__version__}
    Service version: {service_version}
    '''
    return await ctx.send(response)

@bot.command(aliases=['sent-ext'])
async def sentiment_extraction(ctx, *text):
    """
    Determina em valores numéricos o sentimento que o texto enviado transmite
    """
    text=" ".join(i for i in text)
    sentiment = GraphQLQuery.lisa_sentiment_extraction(text)

    return await ctx.send(sentiment)

@bot.command(aliases=['sent-seg'])
async def sentenceSegmentation(ctx, *text):
    """
    Mostra a quantidade de sentenças de um texto. Apenas os números (a função pode ser alterada e/ou aprimorada)
    """
    text=" ".join(i for i in text)
    sentence = GraphQLQuery.lisa_sentence_segmentation(text)

    return await ctx.send(sentence)

@bot.command(aliases=['isoff'])
async def textOffenseLevel(ctx, *text):
    """
    Determina em números o quão ofensivo é a palavra ou texto redigido
    """
    text=" ".join(i for i in text)
    isoff = GraphQLQuery.lisa_text_offensive_level(text)

    return await ctx.send(isoff)