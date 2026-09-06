from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _lucky_helmet_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.draw_cards(2)


card = PokemonToolCardDef(
    guid="4baab8cf-6639-5f5c-a7fa-c77bc77b5b74",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyHelmet.Name",
    display_name="Lucky Helmet",
    searchable_by=["Lucky Helmet","Pokémon Tool","Tool","LuckyHelmet"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=158,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Lucky Helmet",
            game_text="If the Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if it is Knocked Out), draw 2 cards.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_lucky_helmet_trigger,
        ),
    ],
)
