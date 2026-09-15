from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import is_basic_energy_card

async def energy_assist(ctx):
    """40. Attach a basic Energy card from your discard pile to 1 of your
    Benched Pokémon."""
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
    guid="f0a30c4d-ed93-5149-bedb-0997da3b7bf2",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name",
    display_name="Leafeon",
    searchable_by=["Leafeon","Stage 1","Leafeon"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Energy Assist",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=energy_assist,
        ),
    ],
)
