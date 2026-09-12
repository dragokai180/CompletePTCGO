from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def final_wish(ctx):
    """When this Pokémon is Knocked Out by damage from an opponent's attack,
    search your deck for a card and put it into your hand. Shuffle your deck
    afterward."""
    if not ctx.ko_from_attack:
        return
    picks = await ctx.search_deck(
        count=1, minimum=min(1, len(ctx.deck())), prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="7d90b453-bc4c-53a4-8d97-d84ddccc3a46",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy","Basic","Manaphy"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    abilities=[
        Ability(
            title="Final Wish",
            game_text="When this Pokémon is Knocked Out by damage from an opponent's attack, search your deck for a card and put it into your hand. Shuffle your deck afterward.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=final_wish,
        ),
        Attack(
            title="Seafaring",
            game_text="Flip 3 coins. For each heads, attach a Water Energy card from your discard pile to your Benched Pokémon in any way you like.",
            cost={PokemonTypes.WATER: 1},
            effect=bw_legacy_attack,
        ),
    ],
)
