from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def celestial_roar(ctx):
    """Discard the top 3 cards of your deck. If any of those cards are Energy
    cards, attach them to this Pokémon."""
    top = ctx.deck_top(3)
    await ctx.discard_cards(top)
    for card in top:
        if is_energy_card(card):
            await ctx.attach_energy(card, ctx.source)



card = PokemonCardDef(
    guid="2593d077-a5d4-57ac-93ba-c4178ffcb790",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    display_name="Rayquaza-EX",
    searchable_by=["Rayquaza-EX","Basic","EX","RayquazaEX"],
    subtypes=["Basic","EX"],
    collector_number=85,
    set_code="BW6",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    abilities=[
        Attack(
            title="Celestial Roar",
            game_text="Discard the top 3 cards of your deck. If any of those cards are Energy cards, attach them to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=celestial_roar,
        ),
        Attack(
            title="Dragon Burst",
            game_text="Discard all basic Fire Energy or all basic Lightning Energy attached to this Pokémon. This attack does 60 damage times the number of Energy you discarded.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=60,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
    ],
)
