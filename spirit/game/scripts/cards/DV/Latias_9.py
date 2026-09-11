from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def energy_assist(ctx):
    """Attach a basic Energy card from your discard pile to 1 of your Benched
    Pokémon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=1,
        prompt="Choose a basic Energy card from your discard pile to attach.",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)



card = PokemonCardDef(
    guid="ce7ef366-c12c-5bc2-8196-d2e792004a98",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias","Basic","Latias"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="DV",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=energy_assist,
        ),
        Attack(
            title="Sky Heal",
            game_text="If Latios is on your Bench, heal 20 damage from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=bw_legacy_attack,
        ),
    ],
)
