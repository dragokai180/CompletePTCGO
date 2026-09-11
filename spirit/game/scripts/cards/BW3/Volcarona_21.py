from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, Triggers
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import top_entry
from spirit.game.card_effects.support_common import attach_from_discard, requires_hand
from spirit.game.card_effects.trainers import is_basic_energy_card

async def fiery_dance(ctx):
    """30. Attach a basic Energy card from your discard pile to 1 of your
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
    guid="26507fc2-6bbf-59e7-8035-a0e798e7f732",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona","Stage 1","Volcarona"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    abilities=[
        Attack(
            title="Fiery Dance",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=fiery_dance,
        ),
        Attack(
            title="Heat Wave",
            game_text="The Defending Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)
