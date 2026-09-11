from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import is_energy_card


async def power_heater(ctx):
    """Attach one Fire Energy to each of up to two distinct Benched Pokemon."""
    await ctx.deal_damage(20)

    bench = list(ctx.my_bench())
    energies = [
        card for card in ctx.discard_pile()
        if is_energy_card(card)
        and energy_provides_type(card, PokemonTypes.FIRE.value)
    ]
    energy_count = min(2, len(bench), len(energies))
    if not energy_count:
        return
    selected = await ctx.choose_cards(
        energies,
        energy_count,
        minimum=energy_count,
        prompt="Choose Fire Energy cards",
    )
    targets = await ctx.choose_cards(
        bench,
        len(selected),
        minimum=len(selected),
        prompt="Choose a different Benched Pokémon for each Energy",
    ) if selected else []
    for energy, target in zip(selected, targets):
        await ctx.attach_energy(energy, target)


card = PokemonCardDef(
    guid='c7360839-d6bf-5670-8091-fee67ddde2e1',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name',
    display_name='Volcanion',
    searchable_by=['Volcanion', 'Basic', 'Volcanion'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=721,
    abilities=[
        Attack(
            title='Power Heater',
            game_text='Choose 2 of your Benched Pokémon. Attach a Fire Energy card from your discard pile to each of those Pokémon.',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=power_heater,
        ),
        Attack(
            title='Steam Artillery',
            cost={PokemonTypes.FIRE: 3},
            damage=100,
        ),
    ],
)
